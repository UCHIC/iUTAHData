if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
    var mobilelink = document.getElementById('mobilecss');
    mobilelink.setAttribute("rel", "stylesheet");
    mobilelink.setAttribute("type", "text/css");
}

jQuery(document).ready(function ($) {

    //This function is to solve this problem: when selected the dynamic content (river_info) the home page was selected in the navbar, because of the similitude of how the homepage and dynamic pages work.

    // HOW? HOW IN THE NAME OF GOD? WHY?
    // $("#map-canvas").ready(function menuActive() {
    //     if (document.getElementById("map-canvas")) {
    //         $("li.active").addClass("dropdown");
    //         // $("li").removeClass("active");
    //         var dataLI = $('li.dropdown:contains("Data")');
    //         var count = 0;
    //         var toGetOut = [];
    //         var i, len = dataLI.length;
    //         for(i = 0; i<len; i++)
    //         {
    //             if(dataLI[i].getElementsByTagName('a')[0].innerText === "Data ")
    //             {
    //                 dataLI[i].className = dataLI[i].className + " active";
    //             }
    //         }
    //
    //         // $('.dropdown-menu li.active').removeClass("active"); //removes active from data policy menu item.
    //
    //
    //     }
    // });

    $('area').hover(function showArea()
        {
            console.log(this.coords);
        }
    );

    if (document.URL.indexOf("river_info") != -1)
    {
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

function site_selected(element)
{
    window.location.href = "../"+element.value;
}

function raw_data_redirect(site)
{
    var siteCodeToLink = {
        //Logan River
        "LR_FB_C": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-franklin-basin-climate-site-lr-fb-c",
        "LR_GC_C": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-golf-course-climate-site-lr-gc-c",
        "LR_TG_C": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-tony-grove-climate-site-lr-tg-c",
        "LR_TWDEF_C": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-tw-daniels-forest-climate-site-lr-twdef-c",
        "LR_Wilkins_R": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-wilkins-repeater-site-lr-wilkins-r",

        "LR_Mendon_AA": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-logan-river-near-mendon-road-advanced-aquatic-site-lr-mendon-aa",
        "LR_MainStreet_BA": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-logan-river-near-main-street-basic-aquatic-site-lr-mainstreet-ba",
        "LR_WaterLab_AA": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-logan-river-near-the-water-lab-advanced-aquatic-site-lr-waterlab-aa",
        "LR_TG_BA": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-logan-river-near-tony-grove-basic-aquatic-site-lr-tg-ba",
        "LR_FB_BA": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-logan-river-near-franklin-basin-basic-aquatic-site-lr-fb-ba",
        "BSF_CONF_BA": "#",

        "LR_RH_SD": "#",
        "LR_SC_SD": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-spring-creek-storm-drain-lr-sc-sd",


        //Provo River
        "PR_BD_C": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-beaver-divide-climate-site-pr-bd-c",
        "PR_CH_C": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-charleston-climate-site-pr-ch-c",
        "PR_ST_C": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-soapstone-climate-site-pr-st-c",
        "PR_TL_C": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-trial-lake-climate-site-pr-tl-c",

        "PR_BJ_AA": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-provo-river-below-jordanelle-advanced-aquatic-site-pr-bj-aa",
        "PR_CH_AA": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-provo-river-near-charleston-advanced-aquatic-site-pr-ch-aa",
        "PR_LM_BA": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-provo-river-near-lower-midway-basic-aquatic-site-pr-lm-ba",
        "PR_ST_BA": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-provo-river-near-soapstone-basic-aquatic-site-pr-st-ba",
        "PR_WD_BA": "#",

        "PR_SageCreek_canal": "#",
        "PR_Flood_canal": "#",




        //Red Butte Creek
        "RB_ARBR_C":"http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-above-red-butte-reservoir-climate-site-rb-arbr-c",
        "RB_GIRF_C":"http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-the-green-infrastructure-climate-site-rb-girf-c",
        "RB_KF_C":"http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-knowlton-fork-climate-site-rb-kf-c",
        "RB_TM_C":"http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-todd-s-meadow-climate-site-rb-tm-c",

        "RB_ARBR_AA":"http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-above-red-butte-reservoir-advanced-aquatic-site-rb-arbr-aa",
        "RB_CG_BA":"http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-red-butte-creek-near-cottams-grove-basic-aquatic-site-rb-cg-ba",
        "RB_FD_AA":"http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-red-butte-creek-near-foothill-drive-advanced-aquatic-site-rb-fd-aa",
        "RB_KF_BA":"http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-knowlton-fork-basic-aquatic-site-rb-kf-ba",
        "RB_RBG_BA":"http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-red-butte-gate-basic-aquatic-site-rb-rbg-ba",
        "RB_900W_BA": "#",
        "RB_1300E_A": "#",
        "RB_LKF_A": "#",

        "RB_CR_SD": "#",//Change when link is available.
        "RB_Dent_SD": "#",
        "RB_FortD_SD": "http://repository.iutahepscor.org/dataset/iutah-gamut-network-raw-data-at-fort-douglas-storm-drain-rb-fortd-sd",
        "RB_GIRF_SD": "#"
    };
    window.open(siteCodeToLink[site], '_blank');
}










