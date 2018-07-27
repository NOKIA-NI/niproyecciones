window.url_create = '/consultas/create/consulta/';
$('#table_consulta').on('click', '.checkeable-row', function() {
    $('.checkeable-row').not(this).prop('checked', false);
    if ($('.checkeable-row').is(':checked')) {
        $('#update').removeClass('disabled');
        $('#delete').removeClass('disabled');
        $('#action').removeClass('disabled');
    } else {
        $('#update').addClass('disabled');
        $('#delete').addClass('disabled');
        $('#action').addClass('disabled');
    }
    var data = $(this).parent().parent();
    var id = data[0].cells[1].innerText
    window.url_update = '/consultas/update/consulta'+ '/' +  id + '/';
    window.url_delete = '/consultas/delete/consulta'+ '/' +  id + '/';
  });
  
function create_consulta (url) {
  $('#create_consulta').load(url, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_consulta (url_update) {
  $('#update_consulta').load(url_update, function() {
    $(this).modal('show')
  });
  event.stopPropagation()
}

function delete_consulta (url_delete) {
  $('#delete_consulta').load(url_delete, function() {
    $(this).modal('show')
  });
  event.stopPropagation()
}

function update_url_consulta (form) {
  form.action = url_update;
}

function delete_url_consulta (form) {
  form.action = url_delete;
}