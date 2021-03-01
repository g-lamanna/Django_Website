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
