(function($) {

  "use strict";

  // Search Popup
  var searchPopup = function() {
    // open search box
    $('.user-items').on('click', '.search-button', function(e) {
      $('.search-popup').toggleClass('is-visible');
    });

    $('.user-items').on('click', '.btn-close-search', function(e) {
      $('.search-popup').toggleClass('is-visible');
    });
    
    $(".search-popup-trigger").on("click", function(b) {
        b.preventDefault();
        $(".search-popup").addClass("is-visible"),
        setTimeout(function() {
            $(".search-popup").find("#search-popup").focus()
        }, 350)
    }),
    $(".search-popup").on("click", function(b) {
        ($(b.target).is(".search-popup-close") || $(b.target).is(".search-popup-close svg") || $(b.target).is(".search-popup-close path") || $(b.target).is(".search-popup")) && (b.preventDefault(),
        $(this).removeClass("is-visible"))
    }),
    $(document).keyup(function(b) {
        "27" === b.which && $(".search-popup").removeClass("is-visible")
    })
  }

  // Youtube Video
  $(document).ready(function() {

    var $videoSrc;  
    $('.video-btn').click(function() {
        $videoSrc = $(this).data( "src" );
    });

    $('#myModal').on('shown.bs.modal', function (e) {

    $("#video").attr('src',$videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0" ); 
    })

    $('#myModal').on('hide.bs.modal', function (e) {
      $("#video").attr('src',$videoSrc); 
    })

  });

  // Quantity Input - Cart page - Product Details pages
  function quantityInputs() {
    if ( $.fn.inputSpinner ) {
        $("input[type='number']").inputSpinner({
            decrementButton: '<span class="btn btn-dark">-</span>',
            incrementButton: '<span class="btn btn-dark">+</span>',
            groupClass: 'input-spinner',
            buttonsClass: 'btn-spinner',
            buttonsWidth: '26px'
        });
    }
  }

  // init Chocolat light box
  var initChocolat = function() {
  Chocolat(document.querySelectorAll('.image-link'), {
      imageSize: 'contain',
      loop: true,
    })
  }

  var initSwiper = function() {

    var swiper = new Swiper(".main-slider", {
      navigation: {
        nextEl: ".slider-arrow-next",
        prevEl: ".slider-arrow-prev",
      },
      pagination: {
        el: ".main-slider-pagination",
        clickable: true,
      },
    });

    var videos_swiper = new Swiper(".videos-carousel", {
      slidesPerView: 3,
      spaceBetween: 20,
      navigation: {
        nextEl: ".videos-carousel-button-next",
        prevEl: ".videos-carousel-button-prev",
      },
      pagination: {
        el: ".videos-pagination",
        clickable: true,
      },
      breakpoints: {
        0: {
          slidesPerView: 1,
          spaceBetween: 20,
        },
        980: {
          slidesPerView: 3,
          spaceBetween: 20,
        },
      },
    });

    var products_swiper = new Swiper(".products-carousel", {
      slidesPerView: 4,
      spaceBetween: 20,
      navigation: {
        nextEl: ".products-carousel-button-next",
        prevEl: ".products-carousel-button-prev",
      },
      pagination: {
        el: ".products-pagination",
        clickable: true,
      },
      breakpoints: {
        0: {
          slidesPerView: 1,
          spaceBetween: 20,
        },
        600: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        990: {
          slidesPerView: 3,
          spaceBetween: 20,
        },
        1400: {
          slidesPerView: 4,
          spaceBetween: 20,
        },
      },
    });

    var swiper = new Swiper(".testimonial-swiper", {
      loop: true,
      navigation: {
        nextEl: ".swiper-arrow-prev",
        prevEl: ".swiper-arrow-next",
      },
      pagination: {
        el: ".testimonial-pagination",
        clickable: true,
      },
    });

    var swiper = new Swiper(".main-shop-slider", {
      navigation: {
        nextEl: ".main-shop-slider-arrow-next",
        prevEl: ".main-shop-slider-arrow-prev",
      },
      pagination: {
        el: ".main-shop-slider-pagination",
        clickable: true,
      },
      breakpoints: {
        0: {
          slidesPerView: 1,
          spaceBetween: 20,
        },
        600: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        990: {
          slidesPerView: 3,
          spaceBetween: 20,
        },
      },
    });

    var thumb_slider = new Swiper(".thumb-swiper", {
      slidesPerView: 1,
    });
    var large_slider = new Swiper(".large-swiper", {
      spaceBetween: 10,
      effect: 'fade',
      thumbs: {
        swiper: thumb_slider,
      },
    });

  }

  // Sidebar
  $(document).ready(function () {
    $('.closenav').on('click', function () {
        $('.sidenavbar').removeClass('active');
    });

    $('.btn-menu').on('click', function () {
        $('.sidenavbar').addClass('active');
    });

    searchPopup();
    initChocolat();
    initSwiper();
    quantityInputs();
  }); 

  window.addEventListener("load", function () {
    const preloader = document.getElementById("preloader");
    preloader.classList.add("hide-preloader");

    // Initialize Isotope
    $('.entry-container').isotope({
      itemSelector: '.entry-item',
      layoutMode: 'masonry'
    });
    
  });

})(jQuery);
