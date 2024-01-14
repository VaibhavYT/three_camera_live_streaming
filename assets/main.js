var t=0;
function Top_Priority(cameraId) {
    var targetCamera = document.getElementById(cameraId);
    if (t==0) {
        targetCamera.classList.add("top");
        t=1;
    }
    else{
        targetCamera.classList.remove('top');
        t=0;
    }

}