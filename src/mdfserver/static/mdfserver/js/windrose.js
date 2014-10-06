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
                    style: {"line-height": "12px;",
                        "padding": "0px",
                        "padding-top": "2px",
                        "font": "normal .99em arial, sans-serif"
                    }
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
                    itemStyle: {"line-height": "16px;",
                        "padding-bottom": "5px",
                        "padding-top": "2px",
                        "font": "normal .90em arial, sans-serif"
                    },
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

        var windSpeedVals = data[d]['vars'].filter(function (element) {
            return element.code === windspd
        })[0].values;
        var windDirVals = data[d]['vars'].filter(function (element) {
            return element.code === windir
        })[0].values;

        var tableOfFreq = createWindRoseTableData(windSpeedVals, windDirVals);


        console.log(convertFrequenciesToPercentages(tableOfFreq, Math.min(windSpeedVals.length, windDirVals.length)));

        //organize data into table
    });


}

function createWindRoseTableData(windSP, windDir) {
    //Here we organize the data in windspd according to the range object
    //and organize the angles according to its cardinal point
    //this is made in arrays to be outputted to tables later.
    var range = calcRange(windSP);

    var tableOfFreq = {
        "N": [0, 0, 0, 0, 0, 0, 0],//last number is for total
        "NNE": [0, 0, 0, 0, 0, 0, 0],
        "NE": [0, 0, 0, 0, 0, 0, 0],
        "ENE": [0, 0, 0, 0, 0, 0, 0],

        "E": [0, 0, 0, 0, 0, 0, 0],
        "ESE": [0, 0, 0, 0, 0, 0, 0],
        "SE": [0, 0, 0, 0, 0, 0, 0],
        "SSE": [0, 0, 0, 0, 0, 0, 0],

        "S": [0, 0, 0, 0, 0, 0, 0],
        "SSW": [0, 0, 0, 0, 0, 0, 0],
        "SW": [0, 0, 0, 0, 0, 0, 0],
        "WSW": [0, 0, 0, 0, 0, 0, 0],

        "W": [0, 0, 0, 0, 0, 0, 0],
        "WNW": [0, 0, 0, 0, 0, 0, 0],
        "NW": [0, 0, 0, 0, 0, 0, 0],
        "NNW": [0, 0, 0, 0, 0, 0, 0]
    };

    for (var i = 0; i < Math.min(windSP.length, windDir.length); i++) {
        var curDir = windDir[i];
        var curSpeed = windSP[i];

        //getting index for position of value within range:
        tableOfFreq[getAngleCardinal(curDir)][getIndexForRange(range, curSpeed)] += 1;
    }

    return tableOfFreq;

    //CAREFUL: PROCESS ORGANIZATION OF WIND SPEED AND WIND DIRECTION A PAIR AT A TIME TO MAKE SURE
    //THE DIRECTION BELONGS TO THE SPEED

    //call createWindRoseTable with the result data from this function
    //Try to return an object with the data for loose coupling

}

function convertFrequenciesToPercentages(tableOfFreq, datalength) {
    for (var currentDir in tableOfFreq) {
        tableOfFreq[currentDir][6] = 0;
        for (var i = 0; i < tableOfFreq[currentDir].length; i++) {
            if (i !== 6) {
                tableOfFreq[currentDir][i] /= datalength;
                tableOfFreq[currentDir][i] *= 100;
                tableOfFreq[currentDir][i] = parseFloat(tableOfFreq[currentDir][i].toFixed(2));
                tableOfFreq[currentDir][6] += tableOfFreq[currentDir][i];
                tableOfFreq[currentDir][6] = parseFloat(tableOfFreq[currentDir][6].toFixed(2));
            }

        }
    }

    return tableOfFreq;
}

function getIndexForRange(range, windspeed) {
    var testVal = range.step;
    var index = 0;

    while (windspeed > testVal) {
        index += 1;
        testVal += range.step;
        if (index > 5)
            break;
    }

    return index;
}

//This function will take arrays or whatever createWindRoseTableData makes and create the HTML table
//that contains the data for the wind rose
function createWindRoseTable() {
    var element = document.createElement("table");
    element.id = "test_table";
    document.getElementById("spacer").appendChild(element);
}

//This function takes an angle and returns the cardinal point that it belongs to.
function getAngleCardinal(angle) {
    //get special case for N, x <11.25 and x > 348.75
    if (angle < 11.25 || angle > 348.75)
        return "N";

    var cardinal = "nil";

    //check angle range and assign a value to cardinal.
    var cardinalPointsArr
        = [ "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"];

    currCardinalRange = [
        {"min": 11.25, "max": 33.75, "car_point": "NNE"}
    ];

    var step = 22.5;
    cardinalPointsArr.forEach(function (cardinal) {
            currCardinalRange.push(
                {    "min": currCardinalRange[currCardinalRange.length - 1].max + 0.01,
                    "max": currCardinalRange[currCardinalRange.length - 1].max + step,
                    "car_point": cardinal});
        }
    );

    currCardinalRange.forEach(function (cardinalRange) {
        if (angle >= cardinalRange.min && angle <= cardinalRange.max) {
            cardinal = cardinalRange.car_point;
        }
    })

    return cardinal;
}

function calcRange(values) {
    var tempVals = values.slice();
    tempVals.sort();
    var max = Math.round(tempVals[tempVals.length - 1]);


    return {step: Math.round(max / 6), max: max};
}
