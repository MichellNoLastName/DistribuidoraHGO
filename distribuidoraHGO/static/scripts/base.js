//Función para mostrar el spinner de carga
window.onload = ()=> {
    $('#spinner-container').fadeOut('slow',function(){
        $('body').css({ opacity: 0, display: 'block' }).animate({ opacity: 1, top: '+=20' }, 2000);
    });
    $('body').removeClass('hidden');
};

var swiper = new Swiper(".swiper", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
      delay: 4000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
  document.querySelector('.buttonStore').addEventListener('mouseenter', function() {
  swiper.autoplay.stop();
  });

  // Reanudar la animación del Swiper al salir del evento hover en el botón
  document.querySelector('.buttonStore').addEventListener('mouseleave', function() {
  swiper.autoplay.start();
  });
