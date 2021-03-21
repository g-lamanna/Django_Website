const press_video = document.getElementById('wine_press_video');
const punch_video = document.getElementById('punch_down_video');

press_video.muted = true;
punch_video.muted = true;

function play_press(){
  press_video.loop = true;
  press_video.play();
}
function play_punch(){
  press_video.loop = true;
  punch_video.play();
}

press_video.addEventListener('scroll',play_press());
punch_video.addEventListener('scroll',play_punch());

