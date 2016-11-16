if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    var mobilelink = document.getElementById('mobilecss');
    mobilelink.setAttribute("rel", "stylesheet");
    mobilelink.setAttribute("type", "text/css");
}

var linkMap = {
    "LR_FB_C": {
        "raw": "https://www.hydroshare.org/resource/965dc124cabc4587955e6f1f722fc33b/",
        "controlled": "https://www.hydroshare.org/resource/703b45a284574f6082ee6485aec7b7cd/"
    },
    "LR_GC_C": {
        "raw": "https://www.hydroshare.org/resource/96310f82dd5247ba8201955750093923/",
        "controlled": "https://www.hydroshare.org/resource/6a5383a2fe444136ac5f70d7c037d8b3/"
    },
    "LR_TG_C": {
        "raw": "https://www.hydroshare.org/resource/8db626f2625c4b689638f845b75e8e23/",
        "controlled": "https://www.hydroshare.org/resource/3460e3873eec479f95dded645d147027/"
    },
    "LR_TWDEF_C": {
        "raw": "https://www.hydroshare.org/resource/47e6ae5461a7474dbf37abe475a0d6da/",
        "controlled": "https://www.hydroshare.org/resource/9c66df7b439348348e191afc19f3dec7/"
    },
    "LR_Wilkins_R": {"raw": "https://www.hydroshare.org/resource/b653f3cf03214e52aa765f6cb65fbc22/"},
    "LR_Mendon_AA": {
        "raw": "https://www.hydroshare.org/resource/728566f42906412698b09f6fe2f7cd02/",
        "controlled": "https://www.hydroshare.org/resource/98164d85b6834e62ac395785c69e8012/"
    },
    "LR_MainStreet_BA": {
        "raw": "https://www.hydroshare.org/resource/23650489df6646edaf412cffa9881279/",
        "controlled": "https://www.hydroshare.org/resource/4f764f61a2214997b36822fa9079d1f0/"
    },
    "LR_WaterLab_AA": {
        "raw": "https://www.hydroshare.org/resource/ecb77926c2484e068f28acda434f8772/",
        "controlled": "https://www.hydroshare.org/resource/f7a37471e4214087a2a1e1eef27ba4cf/"
    },
    "LR_TG_BA": {
        "raw": "https://www.hydroshare.org/resource/5cc3cf79eab2413fa46da70435a43265/",
        "controlled": "https://www.hydroshare.org/resource/378eee7ebce1436eb31ed1f86c86c38d/"
    },
    "LR_FB_BA": {
        "raw": "https://www.hydroshare.org/resource/8971ca6bab084779913f925e0e485008/",
        "controlled": "https://www.hydroshare.org/resource/14dbbe7db81d432dbf3e89c5dffd664b/"
    },
    "BSF_CONF_BA": {
        "raw": "https://www.hydroshare.org/resource/94bcad20fbfb4c44ac7f98a0fdfa5e79/",
        "controlled": "https://www.hydroshare.org/resource/519dacd9ff4849689848288967501d9a/"
    },
    "LR_RH_SD": {"raw": "https://www.hydroshare.org/resource/29ddd49f7e1149c6b14246eada15713b/"},
    "LR_SC_SD": {"raw": "https://www.hydroshare.org/resource/fd7e56d92c06427583cd83eddf4adf42/"},
    "PR_BD_C": {
        "raw": "https://www.hydroshare.org/resource/4a5bb3a976004f0ea63991323335b170/",
        "controlled": "https://www.hydroshare.org/resource/69b9acb7be31425a9a88a7b22ebabdb5/"
    },
    "PR_CH_C": {
        "raw": "https://www.hydroshare.org/resource/6aa75450ee2744cdb34ed8dde929a84a/",
        "controlled": "https://www.hydroshare.org/resource/7cd9690ea13146b0b69a992285768158/"
    },
    "PR_ST_C": {
        "raw": "https://www.hydroshare.org/resource/e8d904f8041544eaa7809ae4414be665/",
        "controlled": "https://www.hydroshare.org/resource/2b7bf06d8459416db634fb055738415e/"
    },
    "PR_TL_C": {
        "raw": "https://www.hydroshare.org/resource/3ebf244bd2084cfaa68b83b7f91e9587/",
        "controlled": "https://www.hydroshare.org/resource/47fd99fb355a443d836be63c34edc5bb/"
    },
    "PR_BJ_AA": {
        "raw": "https://www.hydroshare.org/resource/9a25a259ab024411ae85b7b39765de19/",
        "controlled": "https://www.hydroshare.org/resource/729bd8f04be24f22b8b1674613e40ebc/"
    },
    "PR_CH_AA": {
        "raw": "https://www.hydroshare.org/resource/887180409e4545018c8372f0bd6f8ff3/",
        "controlled": "https://www.hydroshare.org/resource/626fb9bfe5d5487f86a5389fdd531a34/"
    },
    "PR_LM_BA": {
        "raw": "https://www.hydroshare.org/resource/765afb955526499888f283947cbb26d9/",
        "controlled": "https://www.hydroshare.org/resource/d1ef91c2a8804eaf935fedfeb908a254/"
    },
    "PR_ST_BA": {
        "raw": "https://www.hydroshare.org/resource/8ebd6dd4342b408ba5bc5903d698cbe3/",
        "controlled": "https://www.hydroshare.org/resource/e738791729874dbbac16c0f70f800abc/"
    },
    "PR_WD_BA": {"raw": "https://www.hydroshare.org/resource/6f2eadbc6aa34f2fb5ce55cd7e3f234a/"},
    "PR_SageCreek_canal": {"raw": "https://www.hydroshare.org/resource/657b90c8a14c41b98d5fab75951ccc84/"},
    "PR_Flood_canal": {"raw": "https://www.hydroshare.org/resource/b27302c4466945b190c39547b632bd0a/"},
    "RB_ARBR_C": {
        "raw": "https://www.hydroshare.org/resource/916041be57be47a1b19c63f328fb086c/",
        "controlled": "https://www.hydroshare.org/resource/bf999980819f4d828711e42af4ee2d76/"
    },
    "RB_GIRF_C": {
        "raw": "https://www.hydroshare.org/resource/325b21d55b2c49658a91944fabd896cf/",
        "controlled": "https://www.hydroshare.org/resource/7603db0efe6046ac88d0bbe563319d44/"
    },
    "RB_KF_C": {
        "raw": "https://www.hydroshare.org/resource/5e80dd7cbaf04a5e98d850609c7e534b/",
        "controlled": "https://www.hydroshare.org/resource/f57fb5cc885f4e8bb87c2f6aa0e5da94/"
    },
    "RB_TM_C": {
        "raw": "https://www.hydroshare.org/resource/aff4e6dfc09a4070ac15a6ec0741fd02/",
        "controlled": "https://www.hydroshare.org/resource/9e1fe805c26240418fc06114dac7fc4d/"
    },
    "RB_ARBR_AA": {
        "raw": "https://www.hydroshare.org/resource/e2043ae155514391b6d7f04af226f221/",
        "controlled": "https://www.hydroshare.org/resource/e850a73ab5e749e78edd83edbc45b945/"
    },
    "RB_CG_BA": {
        "raw": "https://www.hydroshare.org/resource/0aef2fa4a34d49adbd7251d1e67a5531/",
        "controlled": "https://www.hydroshare.org/resource/56d1dd04958543a986915ed0146303b7/"
    },
    "RB_FD_AA": {
        "raw": "https://www.hydroshare.org/resource/7999192b91bf489c981a1059fc95ebc2/",
        "controlled": "https://www.hydroshare.org/resource/a8fcd401bc9147a49efce38c23cd1667/"
    },
    "RB_KF_BA": {
        "raw": "https://www.hydroshare.org/resource/dd1a2ffbc2e4422682a3fbd552620c32/",
        "controlled": "https://www.hydroshare.org/resource/2ff70dd80f5644f09c483508a176d303/"
    },
    "RB_RBG_BA": {
        "raw": "https://www.hydroshare.org/resource/40655b4fc21142d090a5a4b835c14220/",
        "controlled": "https://www.hydroshare.org/resource/b3556173dded44cd966a9ea69634bcd1/"
    },
    "RB_900W_BA": {
        "raw": "https://www.hydroshare.org/resource/1846b79a648a4088aad987cc7241656f/",
        "controlled": "https://www.hydroshare.org/resource/7d72b7af9b2940e7b513e99b0b733788/"
    },
    "RB_1300E_A": {
        "raw": "https://www.hydroshare.org/resource/c3ecee31a0c64490bf6a2fcb4841cee4/",
        "controlled": "https://www.hydroshare.org/resource/98bf881068e6451ebd5cb82c54f41a5c/"
    },
    "RB_LKF_A": {"raw": "https://www.hydroshare.org/resource/a56608d8948c43fdb302e1438cf09169/"},
    "RB_CR_SD": {"raw": "https://www.hydroshare.org/resource/a22bbdfb431c44a68959534c94e96392/"},
    "RB_Dent_SD": {"raw": "https://www.hydroshare.org/resource/bc16655330b64bcaa366d464b00e45f0/"},
    "RB_FortD_SD": {"raw": "https://www.hydroshare.org/resource/9e5e99125d1646c69dde9fc43e137667/"},
    "RB_GIRF_SD": {"raw": "https://www.hydroshare.org/resource/2e9db97be020401c9aa03017cb7ee505/"}
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










