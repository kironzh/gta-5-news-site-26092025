$('#submit-button').click(
    function() {
        let email = $('#email').val();
        let submitButton = $('#submit-button');
        const CSRF = $('[name=csrfmiddlewaretoken]').val();

        if(!email.includes('@') || !email.includes('.')) {
            submitButton.val('Неправильно введён адрес почты');
            submitButton.css('background-color', 'red'); 
            return;          
        }

        $.ajax({
            url: '/email/',
            method: 'POST',
            dataType: 'JSON',
            data: {
                'email' : email,
                'csrfmiddlewaretoken' : CSRF
            },
            success: function(data) {
                submitButton.val('Отправлено');
                submitButton.prop('disabled', true);
                submitButton.css('background-color', 'green');
            },
            error: function(data) {
                submitButton.val('Что-то не так. Попробуйте ещё раз');
                submitButton.css('background-color', 'red');
            }
        })
    }
)