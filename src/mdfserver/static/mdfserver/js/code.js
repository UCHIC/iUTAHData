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
        "LR_FB_C": "https://www.hydroshare.org/resource/965dc124cabc4587955e6f1f722fc33b/",
        "LR_GC_C": "https://www.hydroshare.org/resource/96310f82dd5247ba8201955750093923/",
        "LR_TG_C": "https://www.hydroshare.org/resource/8db626f2625c4b689638f845b75e8e23/",
        "LR_TWDEF_C": "https://www.hydroshare.org/resource/47e6ae5461a7474dbf37abe475a0d6da/",
        "LR_Wilkins_R": "https://www.hydroshare.org/resource/b653f3cf03214e52aa765f6cb65fbc22/",

        "LR_Mendon_AA": "https://www.hydroshare.org/resource/728566f42906412698b09f6fe2f7cd02/",
        "LR_MainStreet_BA": "https://www.hydroshare.org/resource/23650489df6646edaf412cffa9881279/",
        "LR_WaterLab_AA": "https://www.hydroshare.org/resource/ecb77926c2484e068f28acda434f8772/",
        "LR_TG_BA": "https://www.hydroshare.org/resource/5cc3cf79eab2413fa46da70435a43265/",
        "LR_FB_BA": "https://www.hydroshare.org/resource/8971ca6bab084779913f925e0e485008/",
        "BSF_CONF_BA": "https://www.hydroshare.org/resource/94bcad20fbfb4c44ac7f98a0fdfa5e79/",

        "LR_RH_SD": "https://www.hydroshare.org/resource/29ddd49f7e1149c6b14246eada15713b/",
        "LR_SC_SD": "https://www.hydroshare.org/resource/fd7e56d92c06427583cd83eddf4adf42/",


        //Provo River
        "PR_BD_C": "https://www.hydroshare.org/resource/4a5bb3a976004f0ea63991323335b170/",
        "PR_CH_C": "https://www.hydroshare.org/resource/6aa75450ee2744cdb34ed8dde929a84a/",
        "PR_ST_C": "https://www.hydroshare.org/resource/e8d904f8041544eaa7809ae4414be665/",
        "PR_TL_C": "https://www.hydroshare.org/resource/3ebf244bd2084cfaa68b83b7f91e9587/",

        "PR_BJ_AA": "https://www.hydroshare.org/resource/9a25a259ab024411ae85b7b39765de19/",
        "PR_CH_AA": "https://www.hydroshare.org/resource/887180409e4545018c8372f0bd6f8ff3/",
        "PR_LM_BA": "https://www.hydroshare.org/resource/765afb955526499888f283947cbb26d9/",
        "PR_ST_BA": "https://www.hydroshare.org/resource/8ebd6dd4342b408ba5bc5903d698cbe3/",
        "PR_WD_BA": "https://www.hydroshare.org/resource/6f2eadbc6aa34f2fb5ce55cd7e3f234a/",

        "PR_SageCreek_canal": "https://www.hydroshare.org/resource/657b90c8a14c41b98d5fab75951ccc84/",
        "PR_Flood_canal": "https://www.hydroshare.org/resource/b27302c4466945b190c39547b632bd0a/",




        //Red Butte Creek
        "RB_ARBR_C":"https://www.hydroshare.org/resource/916041be57be47a1b19c63f328fb086c/",
        "RB_GIRF_C":"https://www.hydroshare.org/resource/325b21d55b2c49658a91944fabd896cf/",
        "RB_KF_C":"https://www.hydroshare.org/resource/5e80dd7cbaf04a5e98d850609c7e534b/",
        "RB_TM_C":"https://www.hydroshare.org/resource/aff4e6dfc09a4070ac15a6ec0741fd02/",

        "RB_ARBR_AA":"https://www.hydroshare.org/resource/e2043ae155514391b6d7f04af226f221/",
        "RB_CG_BA":"https://www.hydroshare.org/resource/0aef2fa4a34d49adbd7251d1e67a5531/",
        "RB_FD_AA":"https://www.hydroshare.org/resource/7999192b91bf489c981a1059fc95ebc2/",
        "RB_KF_BA":"https://www.hydroshare.org/resource/dd1a2ffbc2e4422682a3fbd552620c32/",
        "RB_RBG_BA":"https://www.hydroshare.org/resource/40655b4fc21142d090a5a4b835c14220/",
        "RB_900W_BA": "https://www.hydroshare.org/resource/1846b79a648a4088aad987cc7241656f/",
        "RB_1300E_A": "https://www.hydroshare.org/resource/c3ecee31a0c64490bf6a2fcb4841cee4/",
        "RB_LKF_A": "https://www.hydroshare.org/resource/a56608d8948c43fdb302e1438cf09169/",

        "RB_CR_SD": "https://www.hydroshare.org/resource/a22bbdfb431c44a68959534c94e96392/",
        "RB_Dent_SD": "https://www.hydroshare.org/resource/bc16655330b64bcaa366d464b00e45f0/",
        "RB_FortD_SD": "https://www.hydroshare.org/resource/9e5e99125d1646c69dde9fc43e137667/",
        "RB_GIRF_SD": "https://www.hydroshare.org/resource/2e9db97be020401c9aa03017cb7ee505/"
    };
    window.open(siteCodeToLink[site], '_blank');
}










