jQuery(document).ready(function ($) {

    //This function is to solve this problem: when selected the dynamic content (river_info) the home page was selected, because of the similitude of how they work. Thi
    $("#map-canvas").ready(function menuActive() {
        if (document.getElementById("map-canvas")) {
            $("li.active").addClass("dropdown");
            $("li").removeClass("active");
            var dataLI = $('li:contains("Data")');
            dataLI.addClass("active");


        }
    });

    if (document.URL.indexOf("river_info") != -1)
    {
        document.title = "iUTAH | Site Information";
        drawSeries();
    }

    $('#data-watershed-gallery').carousel({
         interval: 4500
       });

    $('#big_image').carousel({
         interval: 4500
       });

    $('#data-watershed-gallery-modal').carousel({
         interval: false
       });

});












