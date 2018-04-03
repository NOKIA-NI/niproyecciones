$('#sidebar-toggle').on('click', function (event) {
  $('.sidebar').toggleClass('d-md-block');
  $('#dashboard').toggleClass('content_dashboard');
  $('#nav_dasboard').toggleClass('content_nav');
});

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

function update_url_estacion (form) {
  form.action = url_update;
}

function delete_url_estacion (form) {
  form.action = url_delete;
}

function search_url (form) {
  var current_url = window.location.href
  var url_search_estacion = '/estaciones/search/estacion/'
  if ( current_url.includes('/estaciones/list/estacion/')) {
    form.action = url_search_estacion;
  } else {
    form.action = ''
  }
}
