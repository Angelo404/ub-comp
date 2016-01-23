// $(".alert-info").alert();
// window.setTimeout(function() { $(".alert-info").alert('close'); }, 2000);

window.setTimeout(function() {
    $(".alert-info").fadeTo(500, 0).slideUp(500, function(){
        $(this).remove(); 
    });
}, 2000);