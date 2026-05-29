$('#auth-button').click(
    function() {
        let email = $('#email').val();
        let password = $('#password').val();
        let csrf = $('[name=csrfmiddlewaretoken]').val();
        let authButton = $('#auth-button');
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
            },
            success: function() {
                window.location.href = '/';
            },
            error: function(xhr) {
                if(xhr.responseJSON) {
                    authButton.attr('data-bs-content', xhr.responseJSON.message);

                    let popover = bootstrap.Popover.getInstance(authButton[0]);
                    if(popover) popover.dispose();
                    popover = new bootstrap.Popover(authButton[0]);
                    popover.show();
                }
            }
        });
    }
);