function openModifyForm(el) {
    $('.alert-danger').attr('class', 'alert alert-danger d-none')

    var cur_prof_txt = $(el).parent().parent().children()[1]
    var cur_prof_id = $(el).parent().parent().children()[0]
    cur_prof_txt = $(cur_prof_txt).html().split(' (')[0]
    cur_prof_id = $(cur_prof_id).html()
    console.log(cur_prof_txt)

    var form_prof = $('#modify_prof_form_id')
    console.log($(form_prof).attr('action'))
    var s = $(form_prof).attr('action').toString().replace('-', cur_prof_id)
    form_prof = $('#modify_prof_form_id')
    form_prof = $(form_prof).attr('action', s)

    $('#prof_to_modify_text').append(cur_prof_txt)

//    Добавление надписи в input
    var f = $('#modify_prof_form_id')
    var d = $(f).find('input')[1]
    $(d).attr('value', cur_prof_txt)

}

function closeModifyForm(el) {
    $('.alert-danger').attr('class', 'alert alert-danger d-none')
    $('#prof_to_modify_text').html('')
    $('#modify_prof_form_id').attr('action', '/modify_prof/-/')
}


$(function ($) {
    $('#modify_prof_form_id').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {


                // изменяем второй столбец на новое значение
                var element_to_modify = $('#prof_modify_icon_'+response.cur_pk).parents('tr').find('td:first')

                var txt_name = $(element_to_modify).html().split(' (')[0]
                var new_txt = $(element_to_modify).html().replace(txt_name, response.ntext)
                element_to_modify.text(new_txt)




                var b = $('#modifyProfessionWindowClose')
                b.click()
                console.log('Изменено успешно')
            },
            error: function (response) {
                if (response.status === 400)  {
                    $('.alert-danger').text(response.responseJSON.error)
                    $('.alert-danger').toggleClass(['d-none'])
                }
                if (response.status != 400 && response.status != 201) {
                    $('.alert-danger').text('Неизвестная ошибка при изменении')
                    $('.alert-danger').toggleClass(['d-none'])
                }
                console.log('error: ', response)
            }

        })
    })

})
