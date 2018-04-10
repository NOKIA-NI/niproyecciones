// event.PreventDefault()
// event.stopPropagation()

$('#table_existencia').on('click', '.clickable-row', function(event) {
  $(this).addClass('active').siblings().removeClass('active');
  $('#update').removeClass('disabled');
  $('#delete').removeClass('disabled');
  $('#action').removeClass('disabled');
  var data = $(this);
  var id = data[0].cells[0].innerText
  window.url_update = '/existencias/update/existencia/nokia'+ '/' +  id + '/';
  window.url_delete = '/existencias/delete/existencia/nokia'+ '/' +  id + '/';
});

function create_existencia (url) {
  $('#create_existencia').load(url, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_existencia (url_update) {
  $('#update_existencia').load(url_update, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function delete_existencia (url_delete) {
  $('#delete_existencia').load(url_delete, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_url_existencia (form) {
  form.action = url_update;
}

function delete_url_existencia (form) {
  form.action = url_delete;
}
