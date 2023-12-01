(async () => {
    const topology = await fetch(
        'https://code.highcharts.com/mapdata/custom/world.topo.json'
    ).then(response => response.json());


    // Initialize the chart
    Highcharts.mapChart('grafico_1', {

       chart: {
            map: topology,
            spacingBottom: 20
        },

        title: {
            text: 'Legislación a nivel mundial'
        },

        accessibility: {
            series: {
                descriptionFormat: 'Timezone {series.name} with {series.points.length} countries.'
            },
            point: {
                valueDescriptionFormat: '{point.name}.'
            }
        },

        legend: {
            enabled: true
        },

        mapNavigation: {
            enabled: true,
            buttonOptions: {
                verticalAlign: 'bottom'
            }
        },

        plotOptions: {
            map: {
                allAreas: true,
                joinBy: ['iso-a2', 'code'],
                dataLabels: {
                    enabled: true,
                    color: '#000000',
                    style: {
                        fontWeight: 'bold'
                    },
                    // Only show dataLabels for areas with high label rank
                    format: '{#if (lt point.properties.labelrank 5)}' +
                        '{point.properties.iso-a2}' +
                        '{/if}'
                },
                tooltip: {
                    headerFormat: '',
                    pointFormat: '{point.name}: <b>{series.name}</b>'
                }
            }
        },

        series: [{
            name: 'Países con tipo de ley obligatoria a nivel nacional',
            data: ['CL', 'CN','CO',"CG","IL","MD","MC","NA","NP","NL","ES","SE","TW"].map(code => ({ code }))
        }]
    });

})();