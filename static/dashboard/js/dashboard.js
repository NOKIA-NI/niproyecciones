$('#sidebar-toggle').on('click', function (event) {
  $('.sidebar').toggleClass('d-md-block');
  $('#dashboard').toggleClass('content_dashboard');
  $('#nav_dasboard').toggleClass('content_nav');
});

function search_url (form) {
  var current_url = window.location.href
  var url_search_estacion = '/estaciones/search/estacion/'
  var url_search_parte = '/partes/search/parte/'
  if (current_url.includes('/estaciones/')) {
    form.action = url_search_estacion;
  } else if (current_url.includes('/partes/')) {
    form.action = url_search_parte;
  } else {
    form.action = ''
  }
}
