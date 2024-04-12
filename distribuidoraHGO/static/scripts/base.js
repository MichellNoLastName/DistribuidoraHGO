//Función para mostrar el spinner de carga
window.onload = ()=> {
    $('#spinner-container').fadeOut('slow',function(){
        $('body').css({ opacity: 0, display: 'block' }).animate({ opacity: 1, top: '+=20' }, 2000);
    });
    $('.imageLogo').css({ opacity: 0, display: 'block'}).animate({ opacity: 1, top: '+=10%' }, 3000);
    $('body').removeClass('hidden');

};

const boxes = document.querySelectorAll('.box')

window.addEventListener('scroll', checkBoxes)

checkBoxes()

//Efecto de entrada lateral de los elementos
function checkBoxes() {
    const triggerBottom = window.innerHeight / 5 * 4

    boxes.forEach(box => {
        const boxTop = box.getBoundingClientRect().top

        if(boxTop < triggerBottom) {
            box.classList.add('show')
        } /*else {
            box.classList.remove('show')
        }*/
    })
}

//Paneles Categorias
const panels = document.querySelectorAll('.panel')

panels.forEach(panel => {
    panel.addEventListener('mouseover', () => {
        removeActiveClasses()
        panel.classList.add('active')
    })
})

function removeActiveClasses() {
    panels.forEach(panel => {
        panel.classList.remove('active')
    })
}

//button Search Movil
const search = document.querySelector('.formSearchMovil')
const btn = document.querySelector('.btnSearchMovil')
const input = document.querySelector('.input')

btn.addEventListener('click', () => {
    search.classList.toggle('active')
    input.focus()
})

var swiper = new Swiper(".swiper1", {
    spaceBetween: 30,
    centeredSlides: true,
    speed:1500,
    autoplay: {
      delay: 6000,
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

  let categories1 = {0:'Tubos BD\u00AE VACUTAINER',1:'Agujas BD\u00AE VACUTAINER',2:'Lancetas BD\u00AE'}

  var swiperCategories = new Swiper(".swiperCategories", {
    spaceBetween: 30,
    centeredSlides: true,
    speed:2500,
    autoplay: {
      delay: 3000,
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

    on: {
        slideChange: function () {
          $('#subtitle1').text(categories1[this.activeIndex])
          $('#subtitle1').css({ opacity: 0}).animate({ opacity: 1}, 2500);
          $('#buttonSeeCat1').css({opacity: 0}).animate({opacity: 1},2500);
        },
      },
  });

  let categories2 = {0:'Guantes AMBIDERM\u2122',1:'Gasas Galia\u00AE'}

  var swiperCategories2 = new Swiper(".swiperCategories2", {
    spaceBetween: 30,
    centeredSlides: true,
    speed:2500,
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

    on: {
        slideChange: function () {
          $('#subtitle2').text(categories2[this.activeIndex])
          $('#subtitle2').css({ opacity: 0}).animate({ opacity: 1}, 2500);
          $('#buttonSeeCat2').css({opacity: 0}).animate({opacity: 1},2500);
        },
      },
  });

  let categories3 = {0:'Reactivos',1:'Desinfectantes'}
  setTimeout(()=>{
    var swiperCategories3 = new Swiper('.swiperCategories3',{
        spaceBetween: 30,
    centeredSlides: true,
    speed:2500,
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

    on: {
        slideChange: function () {
          $('#subtitle3').text(categories3[this.activeIndex])
          $('#subtitle3').css({ opacity: 0}).animate({ opacity: 1}, 2500);
          $('#buttonSeeCat3').css({opacity: 0}).animate({opacity: 1},2500);
        },
      },
    })
},1500);

let categories4 = {0:'Parámetros Urinarios',1:'Toxicología'}

  var swiperCategories4 = new Swiper(".swiperCategories4", {
    spaceBetween: 30,
    centeredSlides: true,
    speed:2500,
    autoplay: {
      delay: 3000,
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

    on: {
        slideChange: function () {
          $('#subtitle4').text(categories4[this.activeIndex])
          $('#subtitle4').css({ opacity: 0}).animate({ opacity: 1}, 2500);
          $('#buttonSeeCat4').css({opacity: 0}).animate({opacity: 1},2500);
        },
      },
  });


  document.querySelector('.buttonStore').addEventListener('mouseenter', function() {
  swiper.autoplay.stop();
  });

  // Reanudar la animación del Swiper al salir del evento hover en el botón
  document.querySelector('.buttonStore').addEventListener('mouseleave', function() {
  swiper.autoplay.start();
  });

  //Boton "Ver Mas"
  $('.buttonSeeMore').on('mouseenter',()=>{
    swiperCategories.autoplay.stop();
  })
  $('.buttonSeeMore').on('mouseleave',()=>{
    swiperCategories.autoplay.start();
  })
