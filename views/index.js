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
    });
    $(document).on('keypress',function(e) {
        if(e.which == 13) {
            $("#btn").click();
        }
    });
}); 

$(function(){
    eel.expose(out);               // Expose this function to Python
    function out(x) {
        $("#output").text(x);
    }
});
