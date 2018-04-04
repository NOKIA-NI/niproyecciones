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
  $('#create_estacion').modal('show').load(url)
}

function update_estacion (url_update) {
  $('#update_estacion').modal('show').load(url_update)
}

function delete_estacion (url_delete) {
  $('#delete_estacion').modal('show').load(url_delete)
}

function update_url_estacion (form) {
  form.action = url_update;
}

function delete_url_estacion (form) {
  form.action = url_delete;
}
