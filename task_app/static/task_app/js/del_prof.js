function openDel(el) {
    $('.alert-danger').attr('class', 'alert alert-danger d-none')
    var cur_prof_txt = $(el).parent().parent().children()[1]
    var cur_prof_id = $(el).parent().parent().children()[0]
    cur_prof_txt = $(cur_prof_txt).html().split(' ')[0]
    cur_prof_id = $(cur_prof_id).html()

    var form_prof = $('#del_prof_form_id')
    console.log($(form_prof).attr('action'))
    var s = $(form_prof).attr('action').toString().replace('0', cur_prof_id)
    form_prof = $('#del_prof_form_id')
    form_prof = $(form_prof).attr('action', s)

    $('#prof_to_del_text').append(cur_prof_txt)
}

function closeDelForm(el) {
    $('.alert-danger').attr('class', 'alert alert-danger d-none')
    $('#prof_to_del_text').html('')
    $('#del_prof_form_id').attr('action', '/del_prof/0/')
}


$(function () {
    $('#del_prof_form_id').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {
                $('.alert-danger').attr('class', 'alert alert-danger d-none')

                // удаляем строку из таблицы
                row_id = response.deleted_pk
                console.log(row_id)
                var row = "#prof_delete_icon_"+row_id
                row = row.replace(' ', '_')

                console.log(row)
                $(row).parent().parent().remove()



                var b = $('#deleteProfessionWindowClose')
                b.click()
                console.log(response)
                console.log('Удалено успешно')
            },
            error: function (response) {
                if (response.status === 400) {
                    $('.alert-danger').text(response.responseJSON.error)
                    $('.alert-danger').removeClass(['d-none'])
                }
                console.log('error: ', response)
            }

        })
    })

})
