$(document).ready(function(){
    $("#inicio").submit(function(event){
        var email = $("#email1").val();
        var password = $("#password1").val();
        $(".error").remove(); // Remove any existing error messages
        var isValid = true;

        // Validations
        if(email === '' || !email.includes('@') || !email.includes('.')){
            $("#error_container").append('<span class="error">Please enter a valid email</span>');
            isValid = false;
        }
        if(password.length < 6){
            $("#error_container").append('<span class="error">Please enter a password with at least 6 characters</span>');
            isValid = false;
        }

        // Prevent form submission if not valid
        if(!isValid){
            event.preventDefault();
        } else {
            alert("Inicio de sesión exitoso");
        }
    });
});