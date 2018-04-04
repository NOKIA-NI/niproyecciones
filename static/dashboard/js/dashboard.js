$('#sidebar-toggle').on('click', function (event) {
  $('.sidebar').toggleClass('d-md-block');
  $('#dashboard').toggleClass('content_dashboard');
  $('#nav_dasboard').toggleClass('content_nav');
});

function search_url (form) {
  var current_url = window.location.href
  var url_search_estacion = '/estaciones/search/estacion/'
  if ( current_url.includes('/estaciones/list/estacion/')) {
    form.action = url_search_estacion;
  } else {
    form.action = ''
  }
}
