$ (function($){

    $('#form_removelike').submit(function (e) {
        e.preventDefault()
        var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        $.ajax({
            type: "DELETE",
            url: this.action,
            data: $(this).serialize(),
            headers:{
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": $crf_token
             },
            dataType: "json",
            success: (data) => {
              console.log(this)
              $('#count_of_likes').text(data.count_of_likes);
              $('#form').html(data.form);



            },

        })

    });
    $('#form_addlike').submit(function(e){
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function(data){
                console.log(this)
                $('#count_of_likes').text(data.count_of_likes);
                $('#form').html(data.form);

            },

        })


    });

})

