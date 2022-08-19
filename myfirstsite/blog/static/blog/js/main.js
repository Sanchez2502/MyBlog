$ (function($){
    $('#form_addlike').submit(function(e){
        e.preventDefault()
        var count_of_likes = $('[name="count_of_likes"]').attr('value');
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function(data){
                $('#count_of_likes').html(data);
            },

        })


    }),
    $('#form_removelike').submit(function (e) {
        e.preventDefault()
        var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        var count_of_likes = $('[name="count_of_likes"]').attr('value');
        $.ajax({
            type: "DELETE",
            url: this.action,
            data: $(this).serialize(),
            headers:{
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": $crf_token
             },
            dataType: "json",
            isLoaded: true,
            success: (data) => {
              $('#count_of_likes').html(data);
            },

        })

    })

})

