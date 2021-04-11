//Defines array with different texts to display for typewriter.
const type_texts = ['Cabernet Sauvignon','Pinot Noir', 'Petite Sirah','Carmenere','Zinfindel','Muscat of Alexandria',
'Chadonnay','Nebbiolo','Petite Verdot','Riesling'];
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
      "name":"Muscat of Alexandria",
      "overview":`Another important Muscat variety use primarily for dessert wines and off dry white
      wines.  Muscat of Alexandria offers slightly more orange zest and sweet rose notes that Muscat Blanc. `
    },
    {
      "name":"Pinot Gris",
      "overview":`A pink grape mutation of Pinot Noir that's most famous for it's zesty white wines that range
      in style from dry to just plain sweet.`
    },
    {
      "name":"Sagrantino",
      "overview":`A rare, deeply bold, central-italian red that's recently been noted for having 
      some of the highest levels of tannins and antioxidants of any red wine.`
    },
    {
      "name":"Sangiovese",
      "overview":`Sangiovese is Italy's most planted grape and the key variety in Tuscany's renowned
      Chianti.  It's sensetive, tasting quite different depending on where it grows.`
    },
    {
      "name":"Verdejo",
      "overview":`An herbaceous white wine that grows almost exclusively in the Rueda region of Spain.
      Not to be confused with Verdehlo, a Portugese grape used in Madeira.`
    },
    {
      "name":"Aglianico",
      "overview":`Aglianico reigns supreme in southern Italy and is enjoyed the best slow. It's a wine with 
      incredible quality and a unique savory flavor that's best aged. A savory wine like this goes well with 
      gamey dishes or Texas styled barbecues.`
    },
    {
      "name":"Barbera",
      "overview":`If you live in Piedmont, Italy, this is your everyday drinking wine. Barbera is very popular 
      for its affordability, approachability, and lip smacking high acidity. Barbera goes best with roasted dishes, 
      spiced up with cherry, sage, black pepper, and cinnamon. `
    },
    {
      "name":"Bordeaux",
      "overview":`Originating in Bordeaux, France, this is a red blend that's primarily Cabernet Sauvignon and Merlot 
      along with several other grape varieties from the region. This is a perfect wine to have with a steak because 
      of it's high tannins.`
    },
    {
      "name":"Cabernet Franc",
      "overview":`Cabernet Franc is a classic red and the parent grape of both Merlot and Cabernet Sauvignon. Cab Franc 
      has higher acidity than most other wines which makes it a good pairing choice with tomato based dishes, smokey BBQ 
      or rich black lentils.`
    },
    {
      "name":"Carmenere",
      "overview":`Once thought to be nearly extinct Bordeaux variety, we now know that nearly 50% of the merlot planed 
      in Chile is actually Carmenere! The herbal, peppercorn flavors in Carmenere are a great embellishment to roast 
      meats and pretty much anything spiced with cumin.`
    },
    {
      "name":"Chardonnay",
      "overview":`One of the world's most popular grapes, Chardonnay is made in a wide range of styles from sparkling 
      to rich, creamy, white wines aged in oak. Chardonnay pairs well with subtle spices and flavors. For example, 
      try matching it with a creamy, buttery dish with soft textures. Lobster is a winner here.`
    },
    {
      "name":"Gewürztraminer",
      "overview":`Treasured for it's intense floral aromas, Gewürztraminer has thrived for centuries in Europe. 
      This is best enjoyed in its youth when acidity is at its highest. The sweet floral aroma and ginger like 
      spices make this a good wine to pair with Indian or Moroccan cuisine.`
    },
    {
      "name":"Nebbiolo",
      "overview":`Made famous in the Borolo region of Piedmont, Nebbiolo is one of Italy's most popular reds. 
      This is where we have a wonderful dance between succulent aromas and rigorous tannins. You would like to 
      pair this with creamy, high fat dishes like risotto or ravioli. `
    },
    {
      "name":"Petite Verdot",
      "overview":`Considered a minor blending grape in Bordeaux, Petit Verdot has shown promise as a single 
      varietal wine in warmer climates, where it makes smooth full-bodied red. A bold, tannic wine with short 
      finish like Petite Verdot will do well with roasted meats like Cuban style pork or blue cheese burgers.`
    },
    {
      "name":"Pinot Noir",
      "overview":`The world's most popular light bodied red is loved for its red fruit and spice flavors with its 
      soft tannin finish. A versatile red for food pairing, Pinot Noir tastes like it was meant for duck, chicken 
      or pork.`
    },
    {
      "name":"Riesling",
      "overview":`An aromatic white variety that can produce white wines ranging in sttyle from bone-dry to very sweet. 
      Germany is the world's most important producer of Riesling. Off dry Riesling wines make great pairings to spicy 
      Indian and Asian food that include pork, duck, bacon, or shrimp.`
    },
    {
      "name":"Zinfindel",
      "overview":`An editors favorite, this fruit forward yet bold red is loved for its jammy and smokey spice notes. 
      Zinfandel is ideally paired with Moroccan, Turkish and Arabic cuisine which brings out the grape's cinnamon 
      spices. Try it with Asian barbecue.`
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

