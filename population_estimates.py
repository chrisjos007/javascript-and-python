import csv
import json
from collections import defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    """ Driver code for running and keeping server running """

    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


def json_saver(dict, filename):
    """ writes a json file from the filename and dictionary passed """

    f = open(filename+".json", 'w')
    f.write(json.dumps(dict))
    f.close()


def india_plot(csv_read):
    """ returns a dictionary of indian population

    key: year
    value: population """

    india_dict = defaultdict(float)

    # creating dictionary
    for line in csv_read:
        if line[0] == "India":
            india_dict[int(line[2])] += float(line[3])
    return india_dict


def asean_plot(csv_read, asean):
    """ Returns the population dictionary of ASEAN nations

    Data considered for the year 2014 for each ASEAN nation """

    asean_dict = defaultdict(float)

    # creating dictionary
    for line in csv_read:
        if line[0] in asean:
            asean_dict[line[0]] += float(line[3])
    return asean_dict


def saarc_plot(csv_read, saarc):
    """ Returns a dictionary of yearwise population of SAARC nations """

    saarc_dict = defaultdict(float)

    # creates a dictionary of total population for each year
    for line in csv_read:
        if line[0] in saarc:
            saarc_dict[line[2]] += float(line[3])
    return saarc_dict


def group_plot_asean(csv_read, asean):
    """ Returns a population dictionary for ASEAN countries

    keys: ASEAN countries
    values: population over the years as list

    Grouped into countries over the years 2004 to 2014"""

    population = defaultdict(list)
    years = [str(i) for i in range(2004, 2015)]    # list of years

    # loop through the year and creates a dictionary of countrywise population
    for year in years:
        for line in csv_read:
            if (line[2] == year) and (line[0] in asean):
                population[line[0]].append(float(line[3]))

    return population


if __name__ == "__main__":
    """ Read in the csv file and create a list from it.

    Using the list, make function calls

    Each call returns the json file for the required plots
    and to run a local server"""

    # list of SAARC nations
    saarc = [
        "Afghanistan",
        "Bangladesh",
        "Bhutan",
        "India",
        "Maldives",
        "Nepal",
        "Pakistan",
        "Sri Lanka"
        ]

    # list of ASEAN nations
    asean = [
        "Singapore",
        "Brunei",
        "Malaysia",
        "Thailand",
        "Cambodia",
        "Indonesia",
        "Laos",
        "Myanmar",
        "Philippines",
        "Viet Nam"
        ]

    # opening the csv file and writing to a list
    with open('population-estimates_csv.csv', 'r') as newfile:
        csv_read = list(csv.reader(newfile, delimiter=','))

    # rename 2 nations to their shorter names
    for line in csv_read:
        if(line[0] == "Lao People's Democratic Republic"):
            line[0] = "Laos"
        if(line[0] == "Brunei Darussalam"):
            line[0] = "Brunei"

    # make function calls for saving to json
    json_saver(india_plot(csv_read), "india_plot")
    json_saver(asean_plot(csv_read, asean), "asean_plot")
    json_saver(saarc_plot(csv_read, saarc), "saarc_plot")
    json_saver(group_plot_asean(csv_read, asean), "asean_group_plot")
    run()
