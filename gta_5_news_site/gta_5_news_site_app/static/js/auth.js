$('#auth-button').click(
    function() {
        let email = $('#email').val();
        let password = $('#password').val();
        let csrf = $('[name=csrfmiddlewaretoken]').val();
        console.log(email)
        if(!email) {
            alert('Введите адрес почты');
        }

        if(!password) {
            alert('Введите пароль');
        }

        $.ajax({
            url: '/auth/',
            type: 'POST',
            dataType: 'json',
            data: {
                'email' : email,
                'password' : password,
                'csrfmiddlewaretoken': csrf
            }
        });
    }
);