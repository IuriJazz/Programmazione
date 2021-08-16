$(document).ready(function (){

    console.log('funziona?');

    // FancyBox
    $('[data-fancybox="preview"]').fancybox({
        loop: true
    });

    // Cambia classe play button
    $('.play').on("click",function(){

        if($(this).hasClass('fa-play-circle'))
        {
            $(this).removeClass('fa-play-circle');
            $(this).addClass('fa-pause-circle');
        }
        else
        {
            $(this).removeClass('fa-pause-cirlce');
            $(this).addClass('fa-play-circle');
        }
    });
});

