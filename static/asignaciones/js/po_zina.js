window.url_create= '/asignaciones/create/po/zina/';
$('#table_po_zina').on('change', '.checkeable-row', function() {
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
    window.url_update = '/asignaciones/update/po/zina'+ '/' +  id + '/';
    window.url_delete = '/asignaciones/delete/po/zina'+ '/' +  id + '/';
  });

function create_po_zina (url) {
    $('#create_po_zina').load(url, function() {
        $(this).modal('show');
    });
}

function update_po_zina (url_update) {
    $('#update_po_zina').load(url_update, function() {
        $(this).modal('show')
    });
}

function delete_po_zina (url_delete) {
    $('#delete_po_zina').load(url_delete, function() {
        $(this).modal('show')
    });
}

function update_url_po_zina (form) {
    form.action = url_update;
}

function delete_url_po_zina (form) {
    form.action = url_delete;
}