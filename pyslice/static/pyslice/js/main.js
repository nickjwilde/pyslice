$(document).ready(function(){
    // boilerplate code for csrf and ajax.
    // see https://docs.djangoproject.com/en/dev/ref/csrf/#ajax
    // for info
    function csrfSafeMethod(method){
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings){
            if(!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", $("[name=csrfmiddlewaretoken]").val());
            }
        }
    });

    $("#contactForm").on('submit', function(e){
        e.preventDefault();
        form_data = {
            'name': $("#id_name").val(),
            'email': $("#id_email").val()
        };
        $.ajax({
            url: '/contact/',
            type: 'POST',
            data: form_data,
            success: function(data){
                if (data['status'] == 'failure'){
                    $("#error_text").text(data['errors']);
                    $("#contactFormErrors").fadeIn(600);
                }else{
                    $("#contactFormSuccess").text(data['html']);
                    $("#contactFormSuccess").fadeIn(600);
                    $("#id_name").val('');
                    $("#id_email").val('');
                    $("#contactFormSuccess").delay(3000).fadeOut(600);
                    $("#contactFormErrors").fadeOut(600);
                }
            },
            error: function(data){
                $("#error_text").text(data);
                $("#contactFormErrors").css('display', 'block');
            },
        });
    });

    $(".menu-bars").on('click', function(e){
        $(this).siblings(":not(#logo)").slideToggle();
    });

    $(window).resize(function(){
        $(".menu-bars").siblings().removeAttr('style');
    });


});
