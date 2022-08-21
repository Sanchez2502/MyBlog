$ (function($){
    $('form.like').each((index, element) => {
        $(element).on('submit', (e) => {
            e.preventDefault()

            const article_id=$('[name="article_id"]').attr('value');
            var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

            if ($(e.currentTarget).hasClass('form_removelike')){
                $.ajax({
                    type: "DELETE",
                    url: "like/"+article_id+"/",
                    data: $(this).serialize(),
                    headers:{
                        "X-Requested-With": "XMLHttpRequest",
                        "X-CSRFToken": $crf_token
                     },
                    dataType: "json",
                    success: (data) => {
                      console.log(data)
                      $(element).removeClass('form_removelike').addClass('form_addlike');
                      $('#count_of_likes').html(data.count_of_likes);

                    },

                })


            }
            if ($(e.currentTarget).hasClass('form_addlike')){
                $.ajax({
                    type: "POST",
                    url: "like/"+article_id+"/",
                    data: $(this).serialize(),
                    headers:{
                        "X-Requested-With": "XMLHttpRequest",
                        "X-CSRFToken": $crf_token
                     },
                    dataType: 'json',
                    success: (data) => {
                      console.log(data)
                      $(element).removeClass('form_addlike').addClass('form_removelike');
                      $('#count_of_likes').html(data.count_of_likes);

                    },
                    error: (error) => {
                      console.log(error)

                    },

                })


            }

        })
    })


})
$('#form_removelike').submit(function (e) {
        e.preventDefault()
        var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
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

