window.url_create= '/asignaciones/create/asignacion/bulk/';
$('#table_asignacion_bulk').on('change', '.checkeable-row', function() {
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
    window.url_update = '/asignaciones/update/asignacion/bulk'+ '/' +  id + '/';
    window.url_delete = '/asignaciones/delete/asignacion/bulk'+ '/' +  id + '/';
  });

function create_asignacion_bulk (url) {
    $('#create_asignacion_bulk').load(url, function() {
        $(this).modal('show');
    });
}

function update_asignacion_bulk (url_update) {
    $('#update_asignacion_bulk').load(url_update, function() {
        $(this).modal('show')
    });
}

function delete_asignacion_bulk (url_delete) {
    $('#delete_asignacion_bulk').load(url_delete, function() {
        $(this).modal('show')
    });
}

function update_url_asignacion_bulk (form) {
    form.action = url_update;
}

function delete_url_asignacion_bulk (form) {
    form.action = url_delete;
}