//Defines array with different texts to display for typewriter.
const type_texts = ['Cabernet Sauvignon','Pinot Noir', 'Petite Sirah','Carmenere','Zinfindel'];
let count = 0;
let index = 0;
let current_text = '';
let letters = 0;

(function type(){
  if (count === type_texts.length){
    count = 0;
  }
  current_text = type_texts[count];
  letter = current_text.slice(0,++index)

  document.querySelector('.typing').textContent = letter;
  if(letter.length === current_text.length){
    count++;
    index = 0;
  }

  setTimeout(type, 250);


}());

const get_random_wine = () =>{
  generator_list = [
    {
      "name":"Cabernet Sauvignon",
      "overview":`World's most popular wine is a natural cross between 
      Cabernet france and Sauvignon Blanc that originates in Bordeaux. 
      Wines are concentrated and age worthy.`
    },
    {
      "name":"Cabernet Franc",
      "overview":`World's most popular wine is a natural cross between 
      Cabernet france and Sauvignon Blanc `
    },
    {
      "name":"Merlot",
      "overview":`d Sauvignon Blanc that originates in Bordeaux. 
      Wines are concentrated and age worthy.`
    }
  
  ];
  //Generates random dictionary to be cycled through
  const random = Math.floor(Math.random()*generator_list.length)
  let name = document.querySelector('.wine_name');
  let overview = document.querySelector('.wine_overview');
  name.innerHTML = Object.values(generator_list[random])[0];
  overview.innerHTML = Object.values(generator_list[random])[1];
  document.querySelector('.wine-scenery').style.display = 'block';
};

//Executes function on 'onclick' event
document.getElementById('generate_wine').onclick = get_random_wine;

