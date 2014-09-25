/**
 * Created by Mario on 9/22/14.
 */

if (document.getElementById("windrose_box") != null) {
    //First correct position of box
    var boxes = document.getElementsByClassName("data_box");
    var found = 0;

    for (var i = 0; i < boxes.length; i++) {
        if (boxes.item(i).id == "windrose_box") {
            found = i;
        }
    }

    var newPos = found;

    while (newPos % 3 != 0 && newPos != 0) {
        newPos = newPos - 1;
    }

    boxes[newPos].parentNode.insertBefore(boxes.item(found), boxes[newPos]);

    //now put the windrose plot in the box and fill it with some beautiful data.

    var windrose = document.getElementById("windrose_box");

    //Check that each wind speed belongs to its wind direction in DataParser.

    //Buld table (display: none) to display the data data from.

    //This is the code to make the windrose plot, it takes the data in the #windrose_box table (which as display set to none)
    jQuery(document).ready(function ($) {
        $(function () {

            // Parse the data from an inline table using the Highcharts Data plugin
            $('#windrose_box').highcharts({
                data: {
                    table: 'freq',
                    startRow: 1,
                    endRow: 17,
                    endColumn: 7
                },

                chart: {
                    polar: true,
                    type: 'column'
                },

                title: {
                    text: 'Wind Speed and Wind Direction (WindSp_Avg & WindDir_Avg)',
                    style: {"line-height": "12px;", "padding": "0px", "padding-top": "2px", "font": "normal .99em arial, sans-serif" }
                },

                /*subtitle: {
                    text: 'Source: or.water.usgs.gov'
                },*/

                pane: {
                    size: '85%',
                    center: ["50%", "50%"]
                },

                legend: {
                    reversed: true,
                    verticalAlign: 'bottom',
                    itemDistance: 6,
                    padding: 1,
                    itemStyle: {"line-height": "16px;", "padding-bottom": "5px", "padding-top": "2px", "font": "normal .90em arial, sans-serif" },
                    //y: 100,
                    layout: 'horizontal'
                },

                xAxis: {
                    tickmarkPlacement: 'on'
                },

                yAxis: {
                    min: 0,
                    endOnTick: false,
                    showLastLabel: true,
                    title: {
                        text: 'Frequency (%)'
                    },
                    labels: {
                        formatter: function () {
                            return this.value + '%';
                        }
                    }
                },

                tooltip: {
                    valueSuffix: '%'
                },

                plotOptions: {
                    series: {
                        stacking: 'normal',
                        shadow: false,
                        groupPadding: 0,
                        pointPlacement: 'on'
                    }
                }
            });

            $('text:contains("Highcharts.com")').remove();

        });
    });
}
