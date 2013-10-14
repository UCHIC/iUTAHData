jQuery(document).ready(function ($) {
	if (Drupal.settings["site_name"] && Drupal.settings["map_latitude"] && Drupal.settings["map_longitude"]){
		map_latitude = Drupal.settings["map_latitude"];
	    map_longitude = Drupal.settings["map_longitude"];
	    site_name = Drupal.settings["site_name"];

	    centerPoint = new google.maps.LatLng(map_latitude, map_longitude);
        var mapOptions = {
            zoom: 12,
            panControl: false,
            center: centerPoint,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
        var marker = new google.maps.Marker({
            position: centerPoint,
            map: map,
            title: site_name,
            animation: google.maps.Animation.DROP
        });
	}
});