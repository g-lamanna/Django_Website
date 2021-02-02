const logo_animate = gsap.timeline({defaults:{ease:'power1.out'}});

//Animate logo after browser load
logo_animate.to('.centered-logo',{y:'0%',duration:1.5});


//Intializing AOS
AOS.init({
  duration: 2500,
})





