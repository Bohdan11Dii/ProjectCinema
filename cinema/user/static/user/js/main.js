$("#close-sidebar").click(function() {
    $(".page-wrapper").removeClass("toggled");
  });
  $("#show-sidebar").click(function() {
    $(".page-wrapper").addClass("toggled");
  });

// --------------Бокова меню-------------
  $('.list').each(function(index){
        
    var topli = $(this).children(":first-child");
    topli.click(function(){
        var parent = $(this).parent();
        var sublis = parent.find(".sub");
        
        if(sublis.is(':visible')){
            
            sublis.slideUp();
            topli.find('dropdown_i').removeClass('rotatedown');
            
        }else{
            sublis.slideDown();
            
            topli.find('dropdown_i').addClass('rotatedown');
            
        }
    })
    
  });



  if (window.screen.width <= 768){
      $(".page-wrapper").removeClass("toggled");
  }

  window.addEventListener('resize',()=> {
    if (window.screen.width <= 768){
      $(".page-wrapper").removeClass("toggled");
  }
  })

  // -------------Активна сторінка

  let path = location.pathname.split('/')[1]
  // console.log(path);
  let navigationLinks = document.getElementsByClassName('navigation')
  for (const link of navigationLinks) {
    // console.log(link.getAttributeNode('href').value);
    if (link.getAttribute('href').indexOf(path)!== -1){
      link.classList.add('active')
    }
  }



  //-----КНОПКА ПЕРЕМИКАННЯ --------
  $(function () {
    $('.switch-btn').click(function () {
      $(this).toggleClass('switch-on');
      if ($(this).hasClass('switch-on')) {
        $(this).trigger('on.switch');
      } else {
        $(this).trigger('off.switch');
      }
    });
    $('.switch-btn').on('on.switch', function () {
      $($(this).attr('data-id')).removeClass('bl-hide');
    });
    $('.switch-btn').on('off.switch', function () {
      $($(this).attr('data-id')).addClass('bl-hide');
    });
  });