
fetch('india_plot.json')
.then(response => response.json())
.then(data => {
    x_values = Object.keys(data)
    y_values = Object.values(data)
    Highcharts.chart('container', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Indian population for each year'
        },
        xAxis: {
            title: {
                text: 'Year'
            },
            categories: x_values
        },
        yAxis: {
            title: {
                text: 'Population'
            }
        },
        series: [{
            name: 'yearwise population',
            data: y_values
        }]
    });
});

fetch('asean_plot.json')
.then(response => response.json())
.then(data => {
    range_values = Object.keys(data)
    count_auth_cap = Object.values(data)
    Highcharts.chart('container-2', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Authorized Company Capital'
        },
        xAxis: {
            title: {
                text: 'Capital'
            },
            categories: range_values
        },
        yAxis: {
            title: {
                text: 'No of Companies'
            }
        },
        series: [{
            name: 'Capital Count',
            data: count_auth_cap
        }]
    });
});

