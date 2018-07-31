window.url_create= '/asignaciones/create/asignacion/antena/';
$('#table_asignacion_antena').on('change', '.checkeable-row', function() {
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
    window.url_update = '/asignaciones/update/asignacion_antena'+ '/' +  id + '/';
    window.url_delete = '/asignaciones/delete/asignacion_antena'+ '/' +  id + '/';
  });

function create_asignacion_antena (url) {
    $('#create_asignacion_antena').load(url, function() {
        $(this).modal('show');
    });
}

function update_asignacion_antena (url_update) {
    $('#update_asignacion_antena').load(url_update, function() {
        $(this).modal('show')
    });
}

function delete_asignacion_antena (url_delete) {
    $('#delete_asignacion_antena').load(url_delete, function() {
        $(this).modal('show')
    });
}

function update_url_asignacion_antena (form) {
    form.action = url_update;
}

function delete_url_asignacion_antena (form) {
    form.action = url_delete;
}