// event.PreventDefault()
// event.stopPropagation()

$('#table_resultado').on('click', '.clickable-row', function(event) {
  $(this).addClass('active').siblings().removeClass('active');
  $('#update').removeClass('disabled');
  $('#delete').removeClass('disabled');
  $('#action').removeClass('disabled');
  var data = $(this);
  var id = data[0].cells[0].innerText
  window.url_update = '/resultados/update/resultado'+ '/' +  id + '/';
  window.url_delete = '/resultados/delete/resultado'+ '/' +  id + '/';
});

function create_resultado (url) {
  $('#create_resultado').load(url, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_resultado (url_update) {
  $('#update_resultado').load(url_update, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function delete_resultado (url_delete) {
  $('#delete_resultado').load(url_delete, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_url_resultado (form) {
  form.action = url_update;
}

function delete_url_resultado (form) {
  form.action = url_delete;
}

function export_resultado (a, arg) {
  a.href = '/resultados/export/resultado'+ '/' +  arg;
}
