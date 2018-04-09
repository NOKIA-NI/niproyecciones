// event.PreventDefault()
// event.stopPropagation()

$('#table_estacion').on('click', '.clickable-row', function(event) {
  $(this).addClass('active').siblings().removeClass('active');
  $('#update').removeClass('disabled');
  $('#delete').removeClass('disabled');
  $('#action').removeClass('disabled');
  var data = $(this);
  var id = data[0].cells[0].innerText
  window.url_update = '/estaciones/update/estacion'+ '/' +  id + '/';
  window.url_delete = '/estaciones/delete/estacion'+ '/' +  id + '/';
});

function create_estacion (url) {
  $('#create_estacion').load(url, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_estacion (url_update) {
  $('#update_estacion').load(url_update, function() {
    $(this).modal('show')
  });
  event.stopPropagation()
}

function delete_estacion (url_delete) {
  $('#delete_estacion').load(url_delete, function() {
    $(this).modal('show')
  });
  event.stopPropagation()
}

function update_url_estacion (form) {
  form.action = url_update;
}

function delete_url_estacion (form) {
  form.action = url_delete;
}
