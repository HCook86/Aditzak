function display(){
    $("html").css("background-color","red");
}

display();

$(function(){
    eel.expose(say_hello_js);               // Expose this function to Python
    function say_hello_js(x) {
    console.log("Hello from " + x);
    }
    say_hello_js("Javascript World!");
    eel.handleinput("connected!");  // Call a Python function
    
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
