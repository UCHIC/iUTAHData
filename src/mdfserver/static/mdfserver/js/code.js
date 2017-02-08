if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    var mobilelink = document.getElementById('mobilecss');
    mobilelink.setAttribute("rel", "stylesheet");
    mobilelink.setAttribute("type", "text/css");
}

var linkMap = {
        "LR_FB_C": {
            "raw": "https://www.hydroshare.org/resource/965dc124cabc4587955e6f1f722fc33b/",
            "controlled": "https://www.hydroshare.org/resource/08b352fb637c41a2971fa6e1daa20ade/"
        },
        "PR_ST_BA": {
            "raw": "https://www.hydroshare.org/resource/8ebd6dd4342b408ba5bc5903d698cbe3/",
            "controlled": "https://www.hydroshare.org/resource/e640b21cb9b04d20a952cf156459a729/"
        },
        "LR_Mendon_AA": {
            "raw": "https://www.hydroshare.org/resource/728566f42906412698b09f6fe2f7cd02/",
            "controlled": "https://www.hydroshare.org/resource/e55012dcffe64aaba9a9b39f0329b101/"
        },
        "PR_WD_BA": {
            "raw": "https://www.hydroshare.org/resource/6f2eadbc6aa34f2fb5ce55cd7e3f234a/"
        },
        "PR_ST_C": {
            "raw": "https://www.hydroshare.org/resource/e8d904f8041544eaa7809ae4414be665/",
            "controlled": "https://www.hydroshare.org/resource/a4d75f1a6dcd4e758e91e7e8aa5e303c/"
        },
        "RB_ARBR_USGS": {
            "raw": "https://www.hydroshare.org/resource/878093a81b284ac8a4f65948b1c597a2/"
        },
        "PR_SageCreek_canal": {
            "raw": "https://www.hydroshare.org/resource/657b90c8a14c41b98d5fab75951ccc84/"
        },
        "PR_CH_AA": {
            "raw": "https://www.hydroshare.org/resource/887180409e4545018c8372f0bd6f8ff3/",
            "controlled": "https://www.hydroshare.org/resource/3dca5d23a5fd48d8adfed6e97e927221/"
        },
        "RB_FD_AA": {
            "raw": "https://www.hydroshare.org/resource/7999192b91bf489c981a1059fc95ebc2/",
            "controlled": "https://www.hydroshare.org/resource/47244f7407e14529944fe38333fe7612/"
        },
        "RB_RBG_BA": {
            "raw": "https://www.hydroshare.org/resource/40655b4fc21142d090a5a4b835c14220/",
            "controlled": "https://www.hydroshare.org/resource/c0acde2d26a14a0a8a9000304a1b685a/"
        },
        "RB_GIRF_SD": {
            "raw": "https://www.hydroshare.org/resource/2e9db97be020401c9aa03017cb7ee505/"
        },
        "RB_KF_C": {
            "raw": "https://www.hydroshare.org/resource/5e80dd7cbaf04a5e98d850609c7e534b/",
            "controlled": "https://www.hydroshare.org/resource/cde532b5d39141db9c2b22122774afae/"
        },
        "RB_GIRF_C": {
            "raw": "https://www.hydroshare.org/resource/325b21d55b2c49658a91944fabd896cf/",
            "controlled": "https://www.hydroshare.org/resource/e5935762e9054fc49570f02d1a28ed8a/"
        },
        "LR_WaterLab_AA": {
            "raw": "https://www.hydroshare.org/resource/ecb77926c2484e068f28acda434f8772/",
            "controlled": "https://www.hydroshare.org/resource/1b87fe7452624e82a54fa57432b17583/"
        },
        "RB_ARBR_C": {
            "raw": "https://www.hydroshare.org/resource/916041be57be47a1b19c63f328fb086c/",
            "controlled": "https://www.hydroshare.org/resource/6445418c7c0e426d8cb1568d296c02d1/"
        },
        "PR_UM_CUWCD": {
            "raw": "https://www.hydroshare.org/resource/0971b2a50c8f49f98f2a7bda9064143b/"
        },
        "LR_GC_C": {
            "raw": "https://www.hydroshare.org/resource/96310f82dd5247ba8201955750093923/",
            "controlled": "https://www.hydroshare.org/resource/86a27290e1b443a488f0b84cb9e2af91/"
        },
        "RB_TM_C": {
            "raw": "https://www.hydroshare.org/resource/aff4e6dfc09a4070ac15a6ec0741fd02/",
            "controlled": "https://www.hydroshare.org/resource/79ae0f0efe2447fe9a5ab5c15427b2d8/"
        },
        "LR_Wilkins_R": {
            "raw": "https://www.hydroshare.org/resource/b653f3cf03214e52aa765f6cb65fbc22/"
        },
        "PR_WD_USGS": {
            "raw": "https://www.hydroshare.org/resource/56f96886e6194ba28a3a062cf436c8a1/"
        },
        "RB_1300E_A": {
            "raw": "https://www.hydroshare.org/resource/c3ecee31a0c64490bf6a2fcb4841cee4/",
            "controlled": "https://www.hydroshare.org/resource/5057577e8573433d8045b59db91b2550/"
        },
        "RB_900W_BA": {
            "raw": "https://www.hydroshare.org/resource/1846b79a648a4088aad987cc7241656f/",
            "controlled": "https://www.hydroshare.org/resource/9392dbf30acc4133959ae77103ffd5c2/"
        },
        "PR_TC_CUWCD": {
            "raw": "https://www.hydroshare.org/resource/5308027ae2f54be69aff8554a1193a02/"
        },
        "LR_TWDEF_C": {
            "raw": "https://www.hydroshare.org/resource/47e6ae5461a7474dbf37abe475a0d6da/",
            "controlled": "https://www.hydroshare.org/resource/200a03e04591410f8b6310b43558634b/"
        },
        "LR_MainStreet_BA": {
            "raw": "https://www.hydroshare.org/resource/23650489df6646edaf412cffa9881279/",
            "controlled": "https://www.hydroshare.org/resource/98788289144a48e4b5151ab87a1f8ad5/"
        },
        "PR_RW_A": {
            "raw": "https://www.hydroshare.org/resource/8af2f3d23e8d43398ad1b55d69b1a972/"
        },
        "RB_LKF_A": {
            "raw": "https://www.hydroshare.org/resource/a56608d8948c43fdb302e1438cf09169/",
            "controlled": "https://www.hydroshare.org/resource/bb41efc853134d0a90fa1da0041367f5/"
        },
        "LR_RH_SD": {
            "raw": "https://www.hydroshare.org/resource/29ddd49f7e1149c6b14246eada15713b/"
        },
        "PR_KM_B": {
            "raw": "https://www.hydroshare.org/resource/c19b4b0bd0b34eac8f99b51626b7ab08/"
        },
        "PR_Flood_canal": {
            "raw": "https://www.hydroshare.org/resource/b27302c4466945b190c39547b632bd0a/"
        },
        "PR_HD_AA": {
            "raw": "https://www.hydroshare.org/resource/c410ec78d23143268642e2298e884a9b/"
        },
        "RB_KF_BA": {
            "raw": "https://www.hydroshare.org/resource/dd1a2ffbc2e4422682a3fbd552620c32/",
            "controlled": "https://www.hydroshare.org/resource/32176d94cfd74d93b5f7f503522022ac/"
        },
        "RB_ARBR_AA": {
            "raw": "https://www.hydroshare.org/resource/e2043ae155514391b6d7f04af226f221/",
            "controlled": "https://www.hydroshare.org/resource/f83c4a6ddaec4085bd152dd261a1a89c/"
        },
        "PR_CH_CUWCD": {
            "raw": "https://www.hydroshare.org/resource/b5f0873404b941ef982df72e90fc140c/"
        },
        "LR_FB_BA": {
            "raw": "https://www.hydroshare.org/resource/8971ca6bab084779913f925e0e485008/",
            "controlled": "https://www.hydroshare.org/resource/1bb3210918414e13b077e87798d4a696/"
        },
        "PR_TL_C": {
            "raw": "https://www.hydroshare.org/resource/3ebf244bd2084cfaa68b83b7f91e9587/",
            "controlled": "https://www.hydroshare.org/resource/9dea1ecec7ca4c33a4bdbe2b06391dd5/"
        },
        "PR_BD_C": {
            "raw": "https://www.hydroshare.org/resource/4a5bb3a976004f0ea63991323335b170/",
            "controlled": "https://www.hydroshare.org/resource/816f26d1fd9348c3b57c4b66a0fc095a/"
        },
        "LR_SC_SD": {
            "raw": "https://www.hydroshare.org/resource/fd7e56d92c06427583cd83eddf4adf42/"
        },
        "RB_RBR_CUWCD": {
            "raw": "https://www.hydroshare.org/resource/7862ec8fdd5c4ac0a77852eca663ddff/"
        },
        "PR_BJ_AA": {
            "raw": "https://www.hydroshare.org/resource/9a25a259ab024411ae85b7b39765de19/",
            "controlled": "https://www.hydroshare.org/resource/0a5ec097fd894e399379b5183882c820/"
        },
        "PR_YL_R": {
            "raw": "https://www.hydroshare.org/resource/ae8f71e9da1349948d763f854053bd04/"
        },
        "RB_Dent_SD": {
            "raw": "https://www.hydroshare.org/resource/bc16655330b64bcaa366d464b00e45f0/"
        },
        "PR_CH_C": {
            "raw": "https://www.hydroshare.org/resource/6aa75450ee2744cdb34ed8dde929a84a/",
            "controlled": "https://www.hydroshare.org/resource/19b41feee92d40bb99237602487cfd37/"
        },
        "RB_CR_SD": {
            "raw": "https://www.hydroshare.org/resource/a22bbdfb431c44a68959534c94e96392/"
        },
        "BSF_CONF_BA": {
            "raw": "https://www.hydroshare.org/resource/94bcad20fbfb4c44ac7f98a0fdfa5e79/",
            "controlled": "https://www.hydroshare.org/resource/67dc333cb7a9451fab1e926f7bd332bd/"
        },
        "RB_CG_BA": {
            "raw": "https://www.hydroshare.org/resource/0aef2fa4a34d49adbd7251d1e67a5531/",
            "controlled": "https://www.hydroshare.org/resource/4659632bae8a440698b1c6b0f4d3558a/"
        },
        "PR_HD_USGS": {
            "raw": "https://www.hydroshare.org/resource/bddd818ab2074ca9b7335596244b67e4/"
        },
        "RB_FortD_SD": {
            "raw": "https://www.hydroshare.org/resource/9e5e99125d1646c69dde9fc43e137667/"
        },
        "LR_TG_C": {
            "raw": "https://www.hydroshare.org/resource/8db626f2625c4b689638f845b75e8e23/",
            "controlled": "https://www.hydroshare.org/resource/de17599743af4ee7a634eaafd78de8c2/"
        },
        "PR_LM_BA": {
            "raw": "https://www.hydroshare.org/resource/765afb955526499888f283947cbb26d9/",
            "controlled": "https://www.hydroshare.org/resource/61b3ecc69c494522ad64535be3ef93f9/"
        },
        "PR_BJ_CUWCD": {
            "raw": "https://www.hydroshare.org/resource/3d52e02b093742528388fc521826a7de/"
        },
        "LR_TG_BA": {
            "raw": "https://www.hydroshare.org/resource/5cc3cf79eab2413fa46da70435a43265/",
            "controlled": "https://www.hydroshare.org/resource/b93121c191a94abbb288acabba07f954/"
        }
    };

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

    $('area').hover(function showArea() {
            console.log(this.coords);
        }
    );

    if (document.URL.indexOf("river_info") != -1) {
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

    var qualityControlledDownloadButton = $('#quality-controlled-download');
    var rawDownloadButton = $('#raw-quality-download');
    var site = rawDownloadButton.data('site');

    if (linkMap[site] && linkMap[site]['raw']) {
        rawDownloadButton.click(function() {
            data_download_redirect(this.dataset['site'], 'raw')
        });
    } else {
        rawDownloadButton.hide();
    }

    if (linkMap[site] && linkMap[site]['controlled']) {
        qualityControlledDownloadButton.click(function() {
            data_download_redirect(this.dataset['site'], 'controlled')
        });
    } else {
        qualityControlledDownloadButton.hide();
    }

    $('#tsa-visualization').click(function() {
        window.open('http://data.iutahepscor.org/tsa/?view=datasets&sitecode=' + this.dataset['site'], '_blank');
    });
});

function site_selected(element) {
    window.location.href = "../" + element.value;
}

function data_download_redirect(site, quality) {
    window.open(linkMap[site][quality], '_blank');
}
