jQuery(document).ready(function ($) {

    // ****** IMAGE GALLERY BEGINS ********

    // Build the array of images
    var images = new Array();
    var i = 0;
    $('.thumbnail').each(function () {
        images[i] = $(this).attr('src');
        i++;
    });

    // Load first image
    $(".display").attr({'src': images[0]});
    highlightSelected();

    function highlightSelected() {
        var x = 0;

        $(".thumbnail").css({'border': '2px solid #404040'});

        $('.thumbnail').each(function () {
            if ($(this).attr('src') == $('.display').attr('src')) {
                $(this).css({'border': '3px solid #A0A0A0' });
            }
        });
    }

    // Next Button handler
    var counter = 0;
    $(".btnNext").click(function next() {
        if (counter < images.length - 1) {
            counter++;
        }
        else {
            counter = 0;
        }
        $(".display").attr({'src': images[counter]});
        highlightSelected();
    })

    // Prev Button trigger
    $(".btnPrev").click(function next() {
        if (counter > 0) {
            counter--;
        }
        else {
            counter = images.length - 1;
        }
        $(".display").attr({'src': images[counter] });
        highlightSelected();
    })

    $(".thumbnail").click(function () {
        $(".thumbnail").css({'border': '2px solid #404040'});
        $(".display").attr({'src': $(this).attr('src') });
        $(this).css({'border': '3px solid #404040' });

        //update counter value
        for (var i = 0; i < images.length; i++) {
            if (images[i] == $(".display").attr('src')) {
                counter = i;
                break;
            }
        }
    })

    // ****** IMAGE GALLERY ENDS ********

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












