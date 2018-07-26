window.url_create= '/rastreos/create/rastreo/';
$('#table_rastreos').on('change', '.checkeable-row', function() {
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
    window.url_update = '/rastreos/update/rastreo'+ '/' +  id + '/';
    window.url_delete = '/rastreos/delete/rastreo'+ '/' +  id + '/';
  });

function create_rastreo (url) {
    $('#create_rastreo').load(url, function() {
        $(this).modal('show');
    });
}

function update_rastreo (url_update) {
    $('#update_rastreo').load(url_update, function() {
        $(this).modal('show')
    });
}

function delete_rastreo (url_delete) {
    $('#delete_rastreo').load(url_delete, function() {
        $(this).modal('show')
    });
}

function update_url_rastreo (form) {
    form.action = url_update;
}

function delete_url_rastreo (form) {
    form.action = url_delete;
}