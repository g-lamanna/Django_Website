AOS.init();
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


// mapped_regions = [
//   {
//     'wine_id':'map-aglianico',
//     'lat':37.576113,
//     'long':14.061456
//   },
//   {
//     'wine_id':'map-zin',
//     'lat':38.291812,
//     'long':-122.398984
//   },
//   {
//     'wine_id':'map-sango',
//     'lat':41.044835,
//     'long':16.722095
//   },

//   {
//     'wine_id':'map-bord',
//     'lat':44.849239,
//     'long':-0.586217
//   },
//   {
//     'wine_id':'map-chard',
//     'lat':47.143362,
//     'long': 2.550371
//   },
//   {
//     'wine_id':'map-malbec',
//     'lat':-28.465227,
//     'long':-65.794622
//   },
//   {
//     'wine_id':'map-sav-blanc',
//     'lat':47.5532,
//     'long':1.0105
//   }
// ]

mapped_regions = [
  {
    'wine_id':'map-aglianico',
    'lat':37.576113,
    'long':14.061456
  },
  {
    'wine_id':'map-airen',
    'lat':38.92883,
    'long':-2.659336
  },
  {
    'wine_id':'map-albarino',
    'lat':42.856047,
    'long': -8.742383
  },
  {
    'wine_id':'map-assy',
    'lat':36.391797,
    'long':25.459767
  },
  {
    'wine_id':'map-barbera',
    'lat':45.103834,
    'long':7.876042
  },
  {
    'wine_id':'map-blau',
    'lat':46.836469,
    'long':18.701599
  },
  {
    'wine_id':'map-bonarda',
    'lat':-31.577813,
    'long':-68.614164
  },
  {
  'wine_id':'map-bord',
  'lat':44.849239,
  'long':-0.586217
  },
  {
  'wine_id':'map-brach',
  'lat':45.103834,
  'long':7.876042
  },
  {
  'wine_id':'map-cabfranc',
  'lat':44.849239,
  'long':-0.586217
  },
  {
  'wine_id':'map-cabsav',
  'lat':44.849239,
  'long':-0.586217
  },
  {
  'wine_id':'map-carm',
  'lat':-34.552133,
  'long':-71.422518
  },
  {
  'wine_id':'map-cast',
  'lat':39.755536,
  'long': -7.654092
  },
  {
  'wine_id':'map-champ',
  'lat':48.828326,
  'long': 3.941751
  },
  {
  'wine_id':'map-chard',
  'lat':47.143362,
  'long': 2.550371
  },
  {
  'wine_id':'map-chenblanc',
  'lat':-33.940690,
  'long': 18.853293
  },
  {
    'wine_id':'map-cort',
    'lat':45.103834,
    'long':7.876042
  },
  {
    'wine_id':'map-dolce',
    'lat':45.103834,
    'long':7.876042
  },
  {
    'wine_id':'map-fala',
    'lat':40.832962,
    'long':14.624462
  },
  {
    'wine_id':'map-frap',
    'lat':37.576113,
    'long':14.061456
  },
  {
    'wine_id':'map-furmint',
    'lat':46.836469,
    'long':18.701599
  },
  {
    'wine_id':'map-gewu',
    'lat':48.426197,
    'long': 7.388526
  },
  {
    'wine_id':'map-grenache',
    'lat':45.711685,
    'long':4.850225
  },
  {
    'wine_id':'map-gren-blanc',
    'lat':45.711685,
    'long':4.850225
  },
  {
    'wine_id':'map-gruner',
    'lat':48.225174,
    'long': 16.328554
  },
  {
    'wine_id':'map-mad',
    'lat':32.719339,
    'long': -16.930852
  },
  {
    'wine_id':'map-malbec',
    'lat':-32.877996,
    'long': -68.869506
  },
  {
    'wine_id':'map-merlot',
    'lat':44.849239,
    'long':-0.586217
  },
  {
    'wine_id':'map-mona',
    'lat':38.611671, 
    'long':-1.129368
  },
  {
    'wine_id':'map-monte',
    'lat':42.157056, 
    'long': 13.414472
  },
  {
    'wine_id':'map-alex',
    'lat':39.457554,
    'long': -0.431558
  },
  {
    'wine_id':'map-neb',
    'lat':45.103834,
    'long':7.876042
  },
  {
    'wine_id':'map-Negro',
    'lat':41.098215,
    'long': 16.549492
  },
  {
    'wine_id':'map-nero',
    'lat':37.576113,
    'long':14.061456
  },
  {
    'wine_id':'map-nero',
    'lat':37.576113,
    'long':14.061456
  },
  {
    'wine_id':'map-petvert',
    'lat':39.932022,
    'long': -1.690869
  },
  {
    'wine_id':'map-petsirah',
    'lat':38.314469,
    'long': -122.301751
  },
  {
    'wine_id':'map-pinoblanc',
    'lat':48.681802,
    'long': 9.222950
  },
  {
    'wine_id':'map-pinogris',
    'lat':45.561395,
    'long': 11.976847
  },
  {
    'wine_id':'map-pinonoir',
    'lat':47.358254,
    'long': 4.027561
  },
  {
    'wine_id':'map-port',
    'lat': 41.162122,
    'long': -8.608566
  },
  {
    'wine_id':'map-prosecco',
    'lat':45.561395,
    'long': 11.976847
  },
  {
    'wine_id':'map-rhone',
    'lat': 43.640795,
    'long': 4.664700
  },
  {
    'wine_id':'map-riesling',
    'lat':50.169707,
    'long': 8.045252
  },
  {
    'wine_id':'map-sagra',
    'lat':42.890891,
    'long': 12.649009
  },
  {
    'wine_id':'map-sangio',
    'lat':43.377659,
    'long': 10.918665
  },
  {
    'wine_id':'map-savblanc',
    'lat':47.143362,
    'long': 2.550371
  },
  {
    'wine_id':'map-syrah',
    'lat':45.711685,
    'long':4.850225
  },
  {
    'wine_id':'map-touriga',
    'lat':41.427596,
    'long': -7.712398
  },
  {
    'wine_id':'map-trebb',
    'lat':45.696638,
    'long': -0.338826
  },
  {
    'wine_id':'map-verd',
    'lat':41.411597,
    'long': -4.959830
  },
  {
    'wine_id':'map-zin',
    'lat':38.291812,
    'long':-122.398984
  },
]





// Embedded Google Maps
// Initialize and add map
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



