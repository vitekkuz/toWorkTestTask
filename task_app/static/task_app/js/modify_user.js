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


//$(function ($) {
//    $('#modify_user_form_id').submit(function (e) {
//        e.preventDefault()
//        $.ajax({
//            type: this.method,
//            url: this.action,
//            data: $(this).serialize(),
//            dataType: 'json',
//            success: function (response) {
//
//})