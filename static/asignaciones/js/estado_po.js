window.url_create= '/asignaciones/create/estado/po/';
$('#table_estado_po').on('change', '.checkeable-row', function() {
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
    window.url_update = '/estadoes/update/estado_po'+ '/' +  id + '/';
    window.url_delete = '/estadoes/delete/estado_po'+ '/' +  id + '/';
  });

function create_estado_po (url) {
    $('#create_estado_po').load(url, function() {
        $(this).modal('show');
    });
}

function update_estado_po (url_update) {
    $('#update_estado_po').load(url_update, function() {
        $(this).modal('show')
    });
}

function delete_estado_po (url_delete) {
    $('#delete_estado_po').load(url_delete, function() {
        $(this).modal('show')
    });
}

function update_url_estado_po (form) {
    form.action = url_update;
}

function delete_url_estado_po (form) {
    form.action = url_delete;
}