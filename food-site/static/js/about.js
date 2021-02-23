const bio_container = document.querySelector('.bio_container');
const slider = document.querySelector('.slider');
const bio_text = document.querySelector('.bio-text')

const tl = new TimelineMax();

tl.fromTo(bio_container,2,{height:'0%'},{height:'80%', ease: Power2.easeInOut})
.fromTo(bio_text,0.5,{opacity:0},{opacity:1})
.fromTo(slider,1.2,{x:'-100%'},{x:'0%',ease: Power2.easeInOut});