$(document).ready(function(){
    $(".nav-item a").mouseenter(function(e){
        $(this).children(".fa").toggleClass("spin reverse-spin");
        $(this).children(".menu-text").toggleClass("hidden visible");
    });
    $(".nav-item a").mouseleave(function(e){
        $(this).children(".fa").toggleClass("spin reverse-spin");
        $(this).children(".menu-text").toggleClass("hidden visible");
    });
});
