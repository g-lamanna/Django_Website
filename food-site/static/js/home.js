// const logo_animate = gsap.timeline({defaults:{ease:'power1.out'}});

// Animate logo after browser load
// logo_animate.to('.centered-logo',{y:'0%',duration:1.5});


// Intializing AOS
// AOS.init({
//   duration: 2500,
// })

const jumbotron_background_img = document.querySelector('.jumbotron_background_img');
const slider = document.querySelector('.slider');
const bio_text = document.querySelector('.bio-text')


const tl = new TimelineMax()

tl.fromTo(jumbotron_background_img,1.2,{height:'100%'},{height:'70%', ease:Power2.easeInOut})

