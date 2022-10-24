// $(function() {
// 	var imgWidth = $('.slideshow ul li').width();
// 	setInterval(function() {
// 			$('.slideshow ul').animate({marginLeft: -imgWidth}, 1000,
// 				function() {
// 				$(this).css({marginLeft: 0}).find('li:last').after($(this).find('li:first'));
// 				}
// 			);
// 		}, 5000);
// });
$("#slideshow > div:gt(0)").hide();

setInterval(function() {
  $('#slideshow > div:first')
  .fadeOut(1000)
  .next()
  .fadeIn(1000)
  .end()
  .appendTo('#slideshow');
}, window.caruselspeed_2);