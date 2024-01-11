(function($) {
    "use strict";
    jQuery.noConflict();
    //when dom is ready
    $(document).ready(function(){

		// on scroll event start
		$(window).on('scroll', function() {
			if ($(window).scrollTop() > 55) {
					$('#back-to-top').addClass('reveal');
			} else {
					$('#back-to-top').removeClass('reveal');
			}
		});
		// on scroll event end

		// banner-slider start
		$('.owl-carousel.hero-slider').owlCarousel({
			loop:true,
			slideSpeed: 1000,
			margin:10,
			navigation: true,
			pagination: false,
            items:1,
            transitionStyle : "fade",
            navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            itemsDesktop: [1199, 1],
            itemsDesktopSmall: [980, 1],
            itemsTablet: [768, 1],
            itemsMobile: [479, 1],
	  });
	  // banner-slider end

    	// feedback-carousel start
		$(".feedback-carousel").owlCarousel({
            singleItem: true,
        });
        $(".p-carousel").owlCarousel({
            items: 4
        });
    	// feedback-carousel end

    	// animated counter start
    	$('.counter-box').appear(function(){
            var datacount = $(this).attr('data-count');
            $(this).find('.counter').delay(6000).countTo({
                from: 0,
                to: datacount,
                speed: 5000,
                refreshInterval: 50,
            });
        });
    	// animated counter end

        // bootstrap accordion start
        $('#accordion1').collapse();
        // bootstrap accordion end

        // dropdown menu on mouse hover start
        $(".dropdown").on('mouseenter',function() {
            $('.nav > .dropdown-menu', this).not('.in .dropdown-menu').stop(true, true).show("400");
            $(this).addClass('open');
        }).on('mouseleave', function() {
            $('.nav > .dropdown-menu', this).not('.in .dropdown-menu').stop(true, true).hide("400");
            $(this).removeClass('open');
        });
        // dropdown menu on mouse hover end

        // back to top start
        $('#back-to-top').on('click', function(){
            $("html, body").animate({scrollTop: 0}, 500);
            return false;
        });
        // back to top end

    });
    //dom ready end

})(jQuery);