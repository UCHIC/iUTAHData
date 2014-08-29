/**
 * Created by Mario on 6/16/14.
 */

//This function changes the picture in the modal to match the one clicked in the image viewer.
var changeModal = function()
{
    document.getElementsByClassName('item active')[0].classList.remove("active");

    var sel_image = document.getElementsByClassName('item active')[0].children[0].src;
    var modal_content = document.getElementById('carousel_displayer').children;

    modal_content = Array.prototype.slice.call(modal_content);

    modal_content.forEach(function(value, index){
        value.classList.remove("active");

        if(sel_image === value.children[0].src)
        {
            value.className = value.className + " active";
        }

    });

    var myElements = document.querySelectorAll(".modal-dialog.modal-lg");

    for (var i = 0; i < myElements.length; i++) {
        myElements[i].style.width = 'auto';
    }

    /*var sel_image = document.getElementsByClassName('item active')[0];
    var modal = document.getElementById('modal_contents');

    modal.removeChild(modal.firstChild);
    modal.appendChild(sel_image);*/
};