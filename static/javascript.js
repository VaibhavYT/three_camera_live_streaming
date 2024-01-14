function swapCameras(sourceCameraId, targetCameraId) {
  var sourceCamera = document.getElementById(sourceCameraId);
  var targetCamera = document.getElementById(targetCameraId);
  var temp = sourceCamera.innerHTML;
  sourceCamera.innerHTML = targetCamera.innerHTML;
  targetCamera.innerHTML = temp;
}
document.getElementById("second-camera").addEventListener("click", function () {
  swapCameras("first-camera", "second-camera");
});

document.getElementById("third-camera").addEventListener("click", function () {
  swapCameras("first-camera", "third-camera");
});
