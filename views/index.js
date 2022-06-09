function display(){
    
}

display();

$(function(){
    eel.expose(say_hello_js);               // Expose this function to Python
    function say_hello_js(x) {
    console.log("Hello from " + x);
    }
    say_hello_js("Javascript World!");
    
    $("#btn").click(function(){
        eel.handleinput($("#inp").val());
        $('#inp').val('');
        $('#output').html('');
        $('#errors').html('');
    });
    $(document).on('keypress',function(e) {
        if(e.which == 13) {
            $("#btn").click();
        }
    });
}); 

$(function(){
    eel.expose(error);               // Expose this function to Python
    function error(error) {
        var display = 
            '<div id="flash" class="alert alert-warning alert-dismissible fade show" role="alert">' +
                '<strong>' + error + '</strong>' +
                '<a data-bs-dismiss="alert" aria-label="Close" id="flash-icon"><i class="bi bi-x-lg"></i></a>'+
            '</div>';
        $("#errors").html(display);
    }
});

$(function(){
    eel.expose(out);               // Expose this function to Python
    function out(x) {
        x = JSON.parse(x)
        $("#aditza").text(x.Aditza);
        $("#modua").text(x.Modua);
        $("#kasua").text(x.Kasua);
        $("#nor").text(x.Nor);
        $("#nori").text(x.Nori);
        $("#nork").text(x.Nork);
        $("#denbora").text(x.Denbora);
    }
});
