$("a").click(function (e) {
  e.stopPropagation();
});

$(".card").click(function () {
  $(".card-front").toggleClass("card-flip");
  $(".card-back").toggleClass("card-flip");
});
