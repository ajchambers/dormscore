// alert("whastup");

"use strict";
console.log(jQuery.fn.jquery);
$(document).ready(function() {
    handleLoginForm();
    handleResetClick();
    handleRegisterSubmit();
});

function handleLoginForm() {
    const check = $("#check");
    const password = $("#password-field");
    const loginForm = $("#login-form");
    const errorMsg = $("#login-error-msg");

    if (check && password && loginForm && errorMsg) {
        check.on('click', togglePassword);

        loginForm.submit(function(e) {
            e.preventDefault();
            toggleError(false);

            const username = $('#username-field').val();
            const enteredPassword = $('#password-field').val();

            if (username === 'user' && enteredPassword === 'password') {
                console.log('Login successful');
                window.location.href = 'about.html';
            } else {
                toggleError(true);
            }
        });
    } else {
        console.error("One or more elements not found");
    }

    function togglePassword() {
        password.attr('type', check.prop('checked') ? "text" : "password");
    }

    function toggleError(showError) {
        errorMsg.css('opacity', showError ? 1 : 0);
    }
}

function handleResetClick() {
    const reset = $("#reset");

    if (reset) {
        reset.click(function() {
            $("#firstname, #lastname, #email, #email2, #password, #phone, #message, #state, #zipcode").val("");

            window.location.hash = '';
            window.location.reload();
            window.scrollTo(0, 0);
        });
    } else {
        console.error("Reset button not found");
    }
}



function handleRegisterSubmit() {
    $("#registration-form").submit(function (e) {
        console.log('handleRegisterSubmit function called');

        let isValid = true;

        
        const email = $("#email").val().trim();
        const email2 = $("#email2").val().trim();
      
        if (email2 !== email) {
            $("#email-match-error").text("Emails do not match.");
            isValid = false;
        } else {
            $("#email-match-error").text("");
        }


        if (!isValid) {
            e.preventDefault(); 
            console.log('Form validation failed');
        } else {
            console.log('Registration successful');
            
        }
    });
}