// Populate map markers, load images
function close_overlay() {
    $('#full_size_overlay').fadeOut();
    $('#overlay_content').fadeOut();
    selected_thumb = 1;
    current_index = 0;
    end_of_list = false;
}

function show_popup(network, site) {
    load_image_overlay(network, site, 0);
}

function load_image_overlay (network, site, index) {
    response_waiting = true;
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

            response_waiting = false;
            view_large('thumb_' + String(selected_thumb), selected_thumb);
        },
        error: function (result) {
            console.error(result.toString());
            response_waiting = false;
        },
        safe: false
    });
}

function load_next(network, site, index) {
    if (!end_of_list && !response_waiting){
        selected_thumb = 1;
        load_image_overlay(network, site, index + 1);
    }
}


function load_prev(network, site, index) {
    if (index > 0 && !response_waiting) {
        selected_thumb = 8;
        load_image_overlay(network, site, index - 1);
    }
}

function view_large(thumb_id, index) {
    if (response_waiting) {return;}

    var prev_id = 'thumb_' + String(selected_thumb);
    var selected_id = 'selected_thumb';

    if (document.getElementById(selected_id) != null) {
        document.getElementById(selected_id).setAttribute("id", prev_id);
    }
    selected_thumb = index;
    document.getElementById('overlay_image').src = document.getElementById(thumb_id).src;
    document.getElementById('overlay_header').innerHTML = document.getElementById(thumb_id).alt;
    document.getElementById(thumb_id).setAttribute("id", selected_id);
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
var response_waiting = false;

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
            var new_index = 0;

            if (e.keyCode == 39){ // right
                if (selected_thumb > 1 && selected_thumb <= thumb_count) {
                    new_index = selected_thumb - 1;
                }
                else if (selected_thumb == 1 && current_index > 0) {
                    $('.load_prev').click();
                }
            }
            else if (e.keyCode == 37){ // left
                if (selected_thumb < thumb_count && !end_of_list) {
                    new_index = selected_thumb + 1;
                }
                else if (selected_thumb >= thumb_count && !end_of_list) {
                    $('.load_next').click();
                }
            }

            if (new_index > 0) {
                var selected_id = 'thumb_' + String(new_index);
                view_large(selected_id, new_index);
            }
            event.preventDefault();
        }
    });
});
