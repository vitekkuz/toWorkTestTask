function openModifyUserForm(el) {
    $('.alert-danger').attr('class', 'alert alert-danger d-none')

    var cur_id = $(el).attr('id').replace('user_modify_icon_', '')
    // поменяем атрибут action у формы
    var form_user = $('#modify_user_form_id')
    var s = $(form_user).attr('action').toString().replace('-', cur_id)
    var form_user = $('#modify_user_form_id')
    form_user = $(form_user).attr('action', s)

    // подтянем из таблицы данные в поля формы
    var user_data = $(el).parent().parent().children()

    // фамилия
    var form_field = $('#modify_user_form_id').find('input')[1]
    $(form_field).attr('value', $(user_data[1]).text())
    // имя
    var form_field = $('#modify_user_form_id').find('input')[2]
    $(form_field).attr('value', $(user_data[2]).text())
    // отчество
    var form_field = $('#modify_user_form_id').find('input')[3]
    $(form_field).attr('value', $(user_data[3]).text())

    // пол
    var opt = $('#modify_user_form_id').find('select')[1]
      if ($(user_data[4]).text() == 'М')  {$('#modify_user_form_id > div').find('#sexInput').val('М')}
      else  {$('#modify_user_form_id > div').find('#sexInput').val('Ж')}

    // возраст
    var form_field = $('#modify_user_form_id').find('input')[4]
    $(form_field).attr('value', $(user_data[5]).text())
    // номер телефона
    var form_field = $('#modify_user_form_id').find('input')[5]
    $(form_field).attr('value', $(user_data[7]).text())

    // профессия
    var form_field = $('#modify_user_form_id').find('select')[2]
    var cur_prof_user = $(user_data[6]).text()
    $('#modify_user_form_id > div').find('#professionInput').val(cur_prof_user)

    // область
    var form_field = $('#modify_user_form_id').find('select')[3]
    var cur_obl_user = $(user_data[8]).text().split(', ')[0].split(' ')[0]
    $('#modify_user_form_id > div').find('#ariaInput').val(cur_obl_user)

    // район
    var form_field = $('#modify_user_form_id').find('select')[3]
    var cur_district_user = $(user_data[8]).text().split(', ')[1].split(' ')[0]
    $('#modify_user_form_id > div').find('#districtInput').val(cur_district_user)

    // город
    var form_field = $('#modify_user_form_id').find('select')[3]
    var cur_city_user = $(user_data[8]).text().split(', ')[2]
    $('#modify_user_form_id > div').find('#cityInput').val(cur_city_user)
}


function closeModifyUserForm(el) {
    $('.alert-danger').attr('class', 'alert alert-danger d-none')
    $('#modify_user_form_id').attr('action', '/modify_user/-/')
}


$(function ($) {
    $('#modify_user_form_id').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function (response) {

                var row = $('#user_modify_icon_' + response.pk).parent().parent().html(
                `<th scope="row">`+response.pk+`</th>
                <td>` +response.surname + `</td>
                <td>` +response.first_name + `</td>
                <td>` +response.middle_name + `</td>
                <td>` +response.sex + `</td>
                <td>` +response.age + `</td>
                <td>` +response.profession + `</td>
                <td>` +response.phoneNumber + `</td>
                <td>` +response.area + ` область, ` +response.district + ` район, ` +response.city + `</td>
                <td style="text-align: center">
                    <button type="button" class="btn" data-toggle="modal" data-target="#modifyUser" id="user_modify_icon_`+response.pk+`" onclick="openModifyUserForm(this)">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                             fill="currentColor" class="bi bi-pencil-fill" viewBox="0 0 16 16">
                            <path d="M12.854.146a.5.5 0 0 0-.707 0L10.5 1.793 14.207 5.5l1.647-1.646a.5.5 0 0 0 0-.708l-3-3zm.646 6.061L9.793 2.5 3.293 9H3.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.207l6.5-6.5zm-7.468 7.468A.5.5 0 0 1 6 13.5V13h-.5a.5.5 0 0 1-.5-.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.5-.5V10h-.5a.499.499 0 0 1-.175-.032l-.179.178a.5.5 0 0 0-.11.168l-2 5a.5.5 0 0 0 .65.65l5-2a.5.5 0 0 0 .168-.11l.178-.178z"/>
                        </svg>
                    </button>
                </td>>
                <td style="text-align: center"><a data-toggle="modal" data-target="#deleteUser" href="#" id="user_delete_icon_`+response.pk+`" onclick = "openDelUser(this)" >
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                         class="bi bi-trash-fill" viewBox="0 0 16 16">
                        <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                    </svg>
                </a></td>`
                )
                var b = $('#modifyUserWindowClose')
                b.click()
                console.log()
                console.log('Исправлен сотрудник с id: ', response.pk)


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