$('#reg-button').click(
    function() {
        let email = $('#email').val();
        let password = $('#password').val();
        let first_name = $('#first_name').val();
        let csrf = $('[name=csrfmiddlewaretoken]').val();
        console.log(email)
        if(!email) {
            alert('Введите адрес почты');
        }

        if(!password) {
            alert('Введите пароль');
        }

        $.ajax({
            url: '/reg/',
            type: 'POST',
            dataType: 'json',
            data: {
                'email' : email,
                'password' : password,
                'first_name' : first_name,
                'csrfmiddlewaretoken': csrf
            }, 

            success: function(data) {
                window.location.href = '/';
            },

        });
    }
);