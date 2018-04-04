$('#table_parte').on('click', '.clickable-row', function(event) {
  $(this).addClass('active').siblings().removeClass('active');
  $('#update').removeClass('disabled');
  $('#delete').removeClass('disabled');
  $('#action').removeClass('disabled');
  var data = $(this);
  var id = data[0].cells[0].innerText
  window.url_update = '/partes/update/parte'+ '/' +  id + '/';
  window.url_delete = '/partes/delete/parte'+ '/' +  id + '/';
});

function create_parte (url) {
  $('#create_parte').modal('show').load(url)
}

function update_parte (url_update) {
  $('#update_parte').modal('show').load(url_update)
}

function delete_parte (url_delete) {
  $('#delete_parte').modal('show').load(url_delete)
}

function update_url_parte (form) {
  form.action = url_update;
}

function delete_url_parte (form) {
  form.action = url_delete;
}
