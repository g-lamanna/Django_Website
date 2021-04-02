// slider

const buttonsWrapper = document.querySelector(".map");
const slides = document.querySelector(".inner");

buttonsWrapper.addEventListener("click", e => {
  if (e.target.nodeName === "BUTTON") {
    Array.from(buttonsWrapper.children).forEach(item =>
      item.classList.remove("active")
    );
    if (e.target.classList.contains("first")) {
      slides.style.transform = "translateX(-0%)";
      e.target.classList.add("active");
    } else if (e.target.classList.contains("second")) {
      slides.style.transform = "translateX(-23.33333333333333%)";
      e.target.classList.add("active");
    } else if (e.target.classList.contains('third')){
      slides.style.transform = 'translatex(-48.6666666667%)';
      e.target.classList.add('active');
    }
  }
});

// const logo_animate = gsap.timeline({defaults:{ease:'power1.out'}});

// Animate logo after browser load
// logo_animate.to('.centered-logo',{y:'0%',duration:1.5});


// Intializing AOS
// AOS.init({
//   duration: 2500,
// })

// const jumbotron_background_img = document.querySelector('.jumbotron_background_img');
// const slider = document.querySelector('.slider');
// const bio_text = document.querySelector('.bio-text')


// const tl = new TimelineMax()

// tl.fromTo(jumbotron_background_img,1.2,{height:'100%'},{height:'70%', ease:Power2.easeInOut})

