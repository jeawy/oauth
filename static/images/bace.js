
$('.nav_li').click(function(){
    $(this).children('.menu_hide_list').toggle();
  });
$('.menu_hide_list').parent().css('position','relative');