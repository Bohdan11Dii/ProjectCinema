$("#input-generate").click(function(){
	$(".input-password").val(generatePassword());
	return false;
    
});


function generatePassword(){
	var length = 8,
	charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@-#$";
	if(window.crypto && window.crypto.getRandomValues) {
		return Array(length)
			.fill(charset)
			.map(x => x[Math.floor(crypto.getRandomValues(new Uint32Array(1))[0] / (0xffffffff + 1) * (x.length + 1))])
			.join('');    
	} else {
		res = '';
		for (var i = 0, n = charset.length; i < length; ++i) {
			res += charset.charAt(Math.floor(Math.random() * n));
		}
		return res;
	}
}

// let speed = document.getElementById('input-password')
// console.log(speed);
// speed.addEventListener('change', (e) => {
// 	console.log(e.target.value)
// })

// $('.responsive').slick({
// 	dots: true,
// 	infinite: false,
// 	speed: speed,
// 	slidesToShow: 4,
// 	slidesToScroll: 4,
// 	responsive: [
// 	  {
// 		breakpoint: 1024,
// 		settings: {
// 		  slidesToShow: 3,
// 		  slidesToScroll: 3,
// 		  infinite: true,
// 		  dots: true
// 		}
// 	  },
// 	  {
// 		breakpoint: 600,
// 		settings: {
// 		  slidesToShow: 2,
// 		  slidesToScroll: 2
// 		}
// 	  },
// 	  {
// 		breakpoint: 480,
// 		settings: {
// 		  slidesToShow: 1,
// 		  slidesToScroll: 1
// 		}
// 	  }
// 	  // You can unslick at a given breakpoint now by adding:
// 	  // settings: "unslick"
// 	  // instead of a settings object
// 	]
//   });