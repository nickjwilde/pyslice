$(document).ready(function(){
    $(".nav-item a").mouseover(function(e){
        $(this).children(".fa").addClass("spin");
        $(this).children(".fa").removeClass("reverse-spin");
        $(this).children(".menu-text").removeClass("hidden");
        $(this).children(".menu-text").addClass("visible");
    });
    $(".nav-item a").mouseleave(function(e){
        $(this).children(".fa").removeClass("spin");
        $(this).children(".fa").addClass("reverse-spin");
        $(this).children(".menu-text").addClass("hidden");
        $(this).children(".menu-text").removeClass("visible");
    });
});
