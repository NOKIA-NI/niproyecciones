// event.PreventDefault()
// event.stopPropagation()

$('#table_consumo_nokia').on('click', '.clickable-row', function(event) {
  $(this).addClass('active').siblings().removeClass('active');
  $('#update').removeClass('disabled');
  $('#delete').removeClass('disabled');
  $('#action').removeClass('disabled');
  var data = $(this);
  var id = data[0].cells[0].innerText
  window.url_update = '/consumos/update/consumo/nokia'+ '/' +  id + '/';
  window.url_delete = '/consumos/delete/consumo/nokia'+ '/' +  id + '/';
});

function create_consumo_nokia (url) {
  $('#create_consumo_nokia').load(url, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_consumo_nokia (url_update) {
  $('#update_consumo_nokia').load(url_update, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function delete_consumo_nokia (url_delete) {
  $('#delete_consumo_nokia').load(url_delete, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_url_consumo_nokia (form) {
  form.action = url_update;
}

function delete_url_consumo_nokia (form) {
  form.action = url_delete;
}

$('#table_consumo_claro').on('click', '.clickable-row', function(event) {
  $(this).addClass('active').siblings().removeClass('active');
  $('#update').removeClass('disabled');
  $('#delete').removeClass('disabled');
  $('#action').removeClass('disabled');
  var data = $(this);
  var id = data[0].cells[0].innerText
  window.url_update = '/consumos/update/consumo/claro'+ '/' +  id + '/';
  window.url_delete = '/consumos/delete/consumo/claro'+ '/' +  id + '/';
});

function create_consumo_claro (url) {
  $('#create_consumo_claro').load(url, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_consumo_claro (url_update) {
  $('#update_consumo_claro').load(url_update, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function delete_consumo_claro (url_delete) {
  $('#delete_consumo_claro').load(url_delete, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_url_consumo_claro (form) {
  form.action = url_update;
}

function delete_url_consumo_claro (form) {
  form.action = url_delete;
}
