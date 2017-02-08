// Populate map markers, load images
function close_overlay() {
    $('#full_size_overlay').fadeOut();
    $('#overlay_content').fadeOut();
}

function load_image_overlay (network, site, index) {
    current_index = index;
    $.ajax({
        url: "view_images",
        data: {'network': network, 'site': site, 'index': index},
        success: function (result) {
            $('#overlay_container').html(result.toString());
            if ($('#full_size_overlay').is(':hidden')) {
                $('#full_size_overlay').fadeIn();
                $('#overlay_content').fadeIn();
            }
        },

        safe: false
    });
}

function load_next(network, site, index) {
    if (!end_of_list){
        load_image_overlay(network, site, index + 1);
    }
}


function load_prev(network, site, index) {
    if (index > 0) {
        load_image_overlay(network, site, index - 1);
    }
}

function view_large(thumb_id) {
    selected_thumb = thumb_id;
    document.getElementById('overlay_image').src = document.getElementById('thumb_' + String(thumb_id)).src;
    document.getElementById('overlay_header').innerHTML = document.getElementById('thumb_' + String(thumb_id)).alt;
}

var add_site_to_map = function (network, name, lat, lon) {
    if (map == null) {
        initialize_map();
    }

    var subtext = document.getElementById('subtext_' + network + '_' + name).innerHTML;
    var contentString = '<div onclick="load_image_overlay(\'' + network + '\', \'' + name + '\', 0)">' +
        '<div id="infowindow_text">' + subtext + '</div>' +
        '<img id="infowindow" src="' + document.getElementById(network + '_' + name).src + '">' +
        '</div>';

    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(lat, lon),
        map: map,
        title: name
    });

    google.maps.event.addListener(marker, 'click', function () {
        infowindow.setContent(contentString);
        infowindow.open(map, this);
    });
};

var map = null;
var selected_thumb = 1;
var thumb_count = 8;
var current_index = 0;
var end_of_list = false;

var infowindow = new google.maps.InfoWindow({
    content: ''
});

function initialize_map() {
    var myCenter = new google.maps.LatLng(41.3, -111.79);
    var mapOptions = {
        center: myCenter,
        zoom: 7,
        mapTypeId: google.maps.MapTypeId.TERRAIN
    };

    map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
}

$(document).ready(function () {
    $('#full_size_overlay').hide();
    $('#overlay_content').hide();

    if (map == null) {
        initialize_map();
    }

    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function (xhr, settings) {
        }
    });

    $(document).keydown(function (e) {
        if (!$('#full_size_overlay').is(':hidden')) {
            if (e.keyCode == 37){ // left
                if (selected_thumb > 1 && selected_thumb <= thumb_count) {
                    view_large(selected_thumb - 1);
                }
                else if (selected_thumb == 1 && current_index > 0) {
                    $('.load_prev').click();
                    selected_thumb = 8;
                }
            }
            else if (e.keyCode == 39){ // right
                if (selected_thumb < thumb_count && !end_of_list) {
                    view_large(selected_thumb + 1);
                }
                else if (selected_thumb == thumb_count && !end_of_list) {
                    $('.load_next').click();
                    selected_thumb = 1;
                }
            }
            // else if (e.keyCode == 40 && !end_of_list) { // down
            //     $('.load_next').click();
            //     selected_thumb = 1;
            // }
            // else if (e.keyCode == 38) { // up
            //     $('.load_prev').click();
            //     selected_thumb = 1;
            // }

            event.preventDefault();
        }
    });
});
