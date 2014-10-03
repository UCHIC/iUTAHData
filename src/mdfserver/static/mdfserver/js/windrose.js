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

    drawWindRose();
}

function drawWindRose() {
    var windspd = "WindSp_Avg";
    var windir = "WindDir_Avg";

    //get data
    var myRegexp = new RegExp("river_info/(.[^/]*)/", "g");
    var database = myRegexp.exec(document.URL)[1];

    filenames = {"iUTAH_Logan_OD": "Logan", "iUTAH_Provo_OD": "Provo", "iUTAH_RedButte_OD": "RedButte"};
    var site = filenames[database];

    //categorize data
     $.getJSON("/mdf/static/mdfserver/json/" + site + "Site.json").done(function (data) {
        var captureRegex = new RegExp(database + "/(.[^/]*)/", "g");
        d = captureRegex.exec(document.URL)[1];
         console.log(d);

         console.log(data[d]);
         console.log(data[d]['vars']);

         var windSpeedVals = data[d]['vars'].filter(function(element){return element.code === windspd})[0].values;
         var windDirVals = data[d]['vars'].filter(function(element){return element.code === windir})[0].values;

        var range = calcRange(windSpeedVals);


        /*var graphCounter = -1;
        var include = "none";
        if (d == "RB_ARBR_AA") {
            include = "RB_ARBR_USGS";
        } else if (d == "PR_BJ_AA") {
            include = "PR_BJ_CUWCD";
        } else if (d == "PR_CH_AA") {
            include = "PR_CH_CUWCD";
        } else if (d == "PR_LM_BA") {
            include = "PR_UM_CUWCD";
        }

        for (var i = 0; i < data[d].vars.length; i++) {
            //console.log(data[d].vars[i]['values']);
            var myData = [];
            var counter = 0;
            data[d].vars[i]['values'].forEach(function (value) {
                myData.push({"value": value, "index": ++counter});
            });

            var svg = d3.select("#graph" + ++graphCounter).append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

            x.domain(d3.extent(myData, function (d) {
                return d.index;
            }));
            y.domain(d3.extent(myData, function (d) {
                return d.value;
            }));

            svg.append("path")
                .datum(myData)
                .attr("class", "line")
                .attr("d", line);
        }


        if (include != "none") {
            graphCounter = -1;
            for (var i = 0; i < data[include].vars.length; i++) {
                var myData = [];
                var counter = 0;
                data[include].vars[i]['values'].forEach(function (value) {
                    myData.push({"value": value, "index": ++counter});
                });

                var svg = d3.select("#graphx" + ++graphCounter).append("svg")
                    .attr("width", width + margin.left + margin.right)
                    .attr("height", height + margin.top + margin.bottom)
                    .append("g")
                    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

                x.domain(d3.extent(myData, function (include) {
                    return include.index;
                }));
                y.domain(d3.extent(myData, function (include) {
                    return include.value;
                }));

                svg.append("path")
                    .datum(myData)
                    .attr("class", "line")
                    .attr("d", line);
            }
        }*/
    });

    //organize data into table


}

function calcRange(values)
{
    values.sort();
    var max = values[values.length - 1];


    return {step: max/6, max: max};
}
