window.url_create_rastreo = '/rastreos/create/rastreo/';
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

window.url_create_proceso = '/rastreos/create/proceso/';
$('#table_procesos').on('change', '.checkeable-row', function() {
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
    window.url_update = '/rastreos/update/proceso'+ '/' +  id + '/';
    window.url_delete = '/rastreos/delete/proceso'+ '/' +  id + '/';
  });


function create_proceso (url) {
    $('#create_proceso').load(url, function() {
        $(this).modal('show');
    });
}

function update_proceso (url_update) {
    $('#update_proceso').load(url_update, function() {
        $(this).modal('show')
    });
}

function delete_proceso (url_delete) {
    $('#delete_proceso').load(url_delete, function() {
        $(this).modal('show')
    });
}

function update_url_proceso(form) {
    form.action = url_update;
}

function delete_url_proceso (form) {
    form.action = url_delete;
}

$('#table_perfil_procesos').on('change', '.checkeable-row', function() {
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
    window.url_update = '/rastreos/update/perfil/proceso'+ '/' +  id + '/';
  });