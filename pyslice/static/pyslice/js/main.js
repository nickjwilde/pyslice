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
                    $("#error_text").html(data['html']);
                    $("#contactFormErrors").css('display', 'block');
                }else{
                    $("#main-body").html(data['html']);
                }
                console.log(data);
            },
            error: function(data){
                $("#error_text").text(data);
                $("#contactFormErrors").css('display', 'block');
                console.log(data);
            },
        });
    });




    $(".nav-item a").mouseenter(function(e){
        $(this).children(".fa").toggleClass("spin reverse-spin");
        $(this).children(".menu-text").toggleClass("hidden visible");
    });
    $(".nav-item a").mouseleave(function(e){
        $(this).children(".fa").toggleClass("spin reverse-spin");
        $(this).children(".menu-text").toggleClass("hidden visible");
    });
});
