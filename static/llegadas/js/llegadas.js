// event.PreventDefault()
// event.stopPropagation()

$('#table_llegada').on('click', '.clickable-row', function(event) {
  $(this).addClass('active').siblings().removeClass('active');
  $('#update').removeClass('disabled');
  $('#delete').removeClass('disabled');
  $('#action').removeClass('disabled');
  var data = $(this);
  var id = data[0].cells[0].innerText
  window.url_update = '/llegadas/update/llegada'+ '/' +  id + '/';
  window.url_delete = '/llegadas/delete/llegada'+ '/' +  id + '/';
});

function create_llegada (url) {
  $('#create_llegada').load(url, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_llegada (url_update) {
  $('#update_llegada').load(url_update, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function delete_llegada (url_delete) {
  $('#delete_llegada').load(url_delete, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_url_llegada (form) {
  form.action = url_update;
}

function delete_url_llegada (form) {
  form.action = url_delete;
}
