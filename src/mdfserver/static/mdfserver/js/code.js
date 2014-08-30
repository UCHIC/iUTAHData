jQuery(document).ready(function ($) {

    //This function is to solve this problem: when selected the dynamic content (river_info) the home page was selected in the navbar, because of the similitude of how the homepage and dynamic pages work.
    $("#map-canvas").ready(function menuActive() {
        if (document.getElementById("map-canvas")) {
            $("li.active").addClass("dropdown");
            $("li").removeClass("active");
            var dataLI = $('li.dropdown:contains("Data")');
            var count = 0;
            var toGetOut = [];
            var i, len = dataLI.length;
            for(i = 0; i<len; i++)
            {
                if(dataLI[i].getElementsByTagName('a')[0].innerText === "Data ")
                {
                    dataLI[i].className = dataLI[i].className + " active";
                }
            }

            $('.dropdown-menu li.active').removeClass("active"); //removes active from data policy menu item.


        }
    });

    $('area').hover(function showArea()
        {
            console.log(this.coords);
        }
    );

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

    //Adding Dataset Repository Link
    $('.nav>li>a:contains("Data")')
        .parent()
        .find('ul')
        .children().eq(0).after('<li><a href="http://repository.iutahepscor.org">Dataset Repository</a></li>');
    //end adding Dataset Link


});

function site_selected(element)
{
    console.log(element.value);
    window.location.href = "../"+element.value;
}












