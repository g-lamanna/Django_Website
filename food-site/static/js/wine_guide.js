new WOW().init();

// info_test = document.querySelector('.rolling');

// info_icon = document.querySelectorAll('.rolling');
// console.log(info_icon.length);
// for (i=0;i<info_icon.length;i++) {
//   info_icon[i].addEventListener('click',function () {
//     info_test.style.backgroundColor = 'rgb(83, 8, 202)'
//     info_test.style.fontSize = '5px'
//     info_test.style.width = '100%'
//     info_test.style.height = '100%'
//     info_test.style.borderRadius = '20px'
//     info_test.style.padding = '20px'
//     info_test.style.margin = '20px'
//     info_test.style.color = "rgb(200,200,200)"
//     document.querySelector('.ball').style.display='none'
//     document.querySelector('.balls').style.display = 'block'

//   });
// }


document.querySelectorAll('.rolling').forEach(info_icon =>{
  info_icon.addEventListener('mousedown', function() {

    info_icon.style.backgroundColor = 'rgb(83, 8, 202)'
    info_icon.style.fontSize = '5px'
    info_icon.style.width = '100%'
    info_icon.style.height = '100%'
    info_icon.style.borderRadius = '15px'

    info_icon.style.color = "#0fffb7"



  })
})


document.querySelectorAll('.rolling').forEach(info_icon=>{
  info_icon.addEventListener('mouseup', function() {

    info_icon.style.backgroundColor = ''
    info_icon.style.fontSize = ''
    info_icon.style.width = ''
    info_icon.style.height = ''
    info_icon.style.borderRadius = ''
    info_icon.style.padding = ''
    info_icon.style.margin = ''
    info_icon.style.color = ""
    hidden_info_icon.style.display=''
    display_icon.style.display = ''
  })
})

let hidden_info_icon = document.querySelector('.ball');
let display_icon = document.querySelector('.balls')
let info_icon = document.querySelector('.rolling')

mapped_regions = [
  {
    'wine_id':'map-cab',
    'lat':44.849239,
    'long':-0.586217
  },
  {
    'wine_id':'map-zin',
    'lat':38.291812,
    'long':-122.398984
  },
  {
    'wine_id':'map-sango',
    'lat':41.044835,
    'long':16.722095
  }
]


//Embedded Google Maps
//Initialize and add map
function initMap(){

  for(i = 0; i < mapped_regions.length; i++){
          //The location of region
  let region = {lat:Object.values(mapped_regions[i])[1], lng:Object.values(mapped_regions[i])[2]};
  //The map, centered at the region, in this test case, Bordeaux, France.
  let map = new google.maps.Map(document.getElementById(Object.values(mapped_regions[i])[0]),{
    zoom:6,
    center:region,
  });
  //The marker, position at specified region
  const marker  = new google.maps.Marker({
    position:region,
    map:map,
  });
     
  }
}


