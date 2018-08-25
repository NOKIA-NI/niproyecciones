window.url_create_tarea = '/tareas/create/tarea/';
$('#table_tareas').on('change', '.checkeable-row', function() {
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
    window.url_update = '/tareas/update/tarea'+ '/' +  id + '/';
    window.url_delete = '/tareas/delete/tarea'+ '/' +  id + '/';
  });

function create_tarea (url) {
    $('#create_tarea').load(url, function() {
        $(this).modal('show');
    });
}

function update_tarea (url_update) {
    $('#update_tarea').load(url_update, function() {
        $(this).modal('show')
    });
}

function delete_tarea (url_delete) {
    $('#delete_tarea').load(url_delete, function() {
        $(this).modal('show')
    });
}

function update_url_tarea (form) {
    form.action = url_update;
}

function delete_url_tarea (form) {
    form.action = url_delete;
}

function run_tarea (tarea_url, tarea_id) {
    $.ajax({
        method: 'GET',
        url: tarea_url,
        data: {
            'tarea_id': tarea_id
        },
        dataType: 'json',
        success: function(data){
            if (data.task_id != null) {
                var task_id = data.task_id
                get_task_status(task_id, tarea_id);
            }
        },
        error: function(error){
            console.log(error)
        }
    })
}

function get_task_status (task_id, tarea_id) {
    $.ajax({
        method: 'GET',
        url: '/tareas/get/task/status/',
        data: {
            'task_id': task_id
        },
        dataType: 'json',
        success: function(data){
            if (data.state == 'PENDING' || data.state == 'STARTED' || data.state == 'PROGRESS') {
                $('#'+tarea_id).html(data.state);
            }
            if (data.state == 'SUCCESS' || 'FAILURE') {
                $('#'+tarea_id).html(data.state);
            }
            if (data.state != 'SUCCESS') {
                $('#'+tarea_id).html(data.state);
                setTimeout(function () {
                    get_task_status (task_id, tarea_id)
                }, 1000);
            }
        },
        error: function(error){
            console.log(error)
        }
    })
}