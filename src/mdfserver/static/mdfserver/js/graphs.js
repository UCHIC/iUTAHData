/**
 * Created by Mario on 5/30/14.
 */

function drawSeries() {
    var margin = {top: 3, right: 3, bottom: 3, left: 3},
        width = $("#graph0").width() - margin.left - margin.right,
        height = $("#graph0").height() - margin.top - margin.bottom;

    var parseDate = d3.time.format("%d-%b-%y").parse;

    var x = d3.time.scale()
        .range([0, width]);

    var y = d3.scale.linear()
        .range([height, 0]);

    var line = d3.svg.line()
        .x(function (d) {
            return x(d.index);
        })
        .y(function (d) {
            return y(d.value);
        });

    var myRegexp = new RegExp("river_info/(.[^/]*)/", "g");
    var database = myRegexp.exec(document.URL)[1];

    filenames = {"iUTAH_Logan_OD": "Logan", "iUTAH_Provo_OD": "Provo", "iUTAH_RedButte_OD": "RedButte"};
    var site = filenames[database];

    //console.log("database: " + database + "\n");
    //console.log("site: " + site + "\n");



    $.getJSON("/mdf/static/mdfserver/json/" + site + "Site.json").done(function (data) {
        var graphCounter = -1;
        var captureRegex = new RegExp(database + "/(.[^/]*)/", "g");
        d = captureRegex.exec(document.URL)[1];
        //console.log("site:" + d);
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
    });



}



