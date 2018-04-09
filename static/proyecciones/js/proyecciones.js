// event.PreventDefault()
// event.stopPropagation()

$('#table_proyeccion').on('click', '.clickable-row', function(event) {
  $(this).addClass('active').siblings().removeClass('active');
  $('#update').removeClass('disabled');
  $('#delete').removeClass('disabled');
  $('#action').removeClass('disabled');
  var data = $(this);
  var id = data[0].cells[0].innerText
  window.url_update = '/proyecciones/update/proyeccion'+ '/' +  id + '/';
  window.url_delete = '/proyecciones/delete/proyeccion'+ '/' +  id + '/';
});

function create_proyeccion (url) {
  $('#create_proyeccion').load(url, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_proyeccion (url_update) {
  $('#update_proyeccion').load(url_update, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function delete_proyeccion (url_delete) {
  $('#delete_proyeccion').load(url_delete, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_url_proyeccion (form) {
  form.action = url_update;
}

function delete_url_proyeccion (form) {
  form.action = url_delete;
}
