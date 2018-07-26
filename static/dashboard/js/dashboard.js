$('#sidebar-toggle').on('click', function (event) {
  $('.sidebar').toggleClass('d-md-block');
  $('#dashboard').toggleClass('content_dashboard');
  $('#nav_dasboard').toggleClass('content_nav');
});

$('#filter-toggle').on('click', function (event) {
  $('.filter').toggleClass('d-md-block');
  $('#dashboard').toggleClass('content_dashboard_filter');
  $('#nav_dasboard').toggleClass('content_nav_filter');
});

$('#controlPartesClose').hide()
$('#controlPartes').on('shown.bs.collapse', function() {
  $('#controlPartesOpen').hide()
  $('#controlPartesClose').show()
   }).on('hidden.bs.collapse', function() {
     $('#controlPartesOpen').show()
     $('#controlPartesClose').hide()
   });

$('#formatosClose').hide()
$('#formatos').on('shown.bs.collapse', function() {
  $('#formatosOpen').hide()
  $('#formatosClose').show()
   }).on('hidden.bs.collapse', function() {
     $('#formatosOpen').show()
     $('#formatosClose').hide()
   });

$('#estacionesClose').hide()
$('#estaciones').on('shown.bs.collapse', function() {
  $('#estacionesOpen').hide()
  $('#estacionesClose').show()
   }).on('hidden.bs.collapse', function() {
     $('#estacionesOpen').show()
     $('#estacionesClose').hide()
   });

$('#rastreosClose').hide()
$('#rastreos').on('shown.bs.collapse', function() {
  $('#rastreosOpen').hide()
  $('#rastreosClose').show()
  }).on('hidden.bs.collapse', function() {
    $('#rastreosOpen').show()
    $('#rastreosClose').hide()
  });


function search_url (form) {
  var current_url = window.location.href
  var url_search_estacion = '/estaciones/search/estacion/'
  var url_search_parte = '/partes/search/parte/'
  var url_search_proyeccion_web = '/proyecciones/search/proyeccion/web/'
  var url_search_proyeccion_extra = '/proyecciones/search/proyeccion/extra/'
  var url_search_hw_actividad = '/hw_actividades/search/hw/actividad/'
  var url_search_consumo_nokia = '/consumos/search/consumo/nokia/'
  var url_search_consumo_claro = '/consumos/search/consumo/claro/'
  var url_search_llegada = '/llegadas/search/llegada/'
  var url_search_existencia = '/existencias/search/existencia/'
  var url_search_resultado = '/resultados/search/resultado/'
  var url_search_impacto = '/impactos/search/impacto/'
  var url_search_formato_estacion = '/formatos/search/formato/estacion/'
  var url_search_formato_parte = '/formatos/search/formato/parte/'
  var url_search_formato_claro = '/formatos/search/formato/claro/'
  var url_search_formato_claro_total = '/formatos/search/formato/claro/total/'
  var url_search_formato_claro_kit = '/formatos/search/formato/claro/kit/'
  var url_search_bitacora_estacion = '/estaciones/search/bitacora/estacion/'
  var url_search_proyeccion_estacion = '/estaciones/search/proyeccion/estacion/'
  var url_search_rastreo = '/rastreos/search/rastreo/'
  var url_search_proceso = '/rastreos/search/proceso/'
  var url_search_perfil_rastreo = '/rastreos/search/perfil/rastreo/'
  var url_search_perfil_proceso = '/rastreos/search/perfil/proceso/'
  var url_search_tarea = '/tareas/search/tarea/'
  var url_search_consulta = '/consultas/search/consulta/'

  if (current_url.includes('/bitacora/estacion/')) {
    form.action = url_search_bitacora_estacion;
  } else if (current_url.includes('/proyeccion/estacion/')) {
    form.action = url_search_proyeccion_estacion;
  } else if (current_url.includes('/estacion/')) {
    form.action = url_search_estacion;
  } else if (current_url.includes('/partes/')) {
    form.action = url_search_parte;
  } else if (current_url.includes('/proyeccion/web/')) {
    form.action = url_search_proyeccion_web;
  } else if (current_url.includes('/proyeccion/extra/')) {
    form.action = url_search_proyeccion_extra;
  } else if (current_url.includes('/hw/actividad/')) {
    form.action = url_search_hw_actividad;
  } else if (current_url.includes('/consumo/nokia/')) {
    form.action = url_search_consumo_nokia;
  } else if (current_url.includes('/consumo/claro/')) {
    form.action = url_search_consumo_claro;
  } else if (current_url.includes('/llegada/')) {
    form.action = url_search_llegada;
  } else if (current_url.includes('/existencia/')) {
    form.action = url_search_existencia;
  } else if (current_url.includes('/resultado/')) {
    form.action = url_search_resultado;
  } else if (current_url.includes('/impacto/')) {
    form.action = url_search_impacto;
  } else if (current_url.includes('/consulta/')) {
    form.action = url_search_consulta;
  } else if (current_url.includes('/formato/estacion/')) {
    form.action = url_search_formato_estacion;
  } else if (current_url.includes('/formato/parte/')) {
    form.action = url_search_formato_parte;
  } else if (current_url.includes('/formato/claro/total/')) {
    form.action = url_search_formato_claro_total;
  } else if (current_url.includes('/formato/claro/kit/')) {
    form.action = url_search_formato_claro_kit;
  } else if (current_url.includes('/formato/claro/')) {
    form.action = url_search_formato_claro;
  } else if (current_url.includes('/perfil/rastreo/')) {
    form.action = url_search_perfil_rastreo;
  } else if (current_url.includes('/perfil/proceso/')) {
    form.action = url_search_perfil_proceso;
  } else if (current_url.includes('/rastreo/')) {
    form.action = url_search_rastreo;
  } else if (current_url.includes('/proceso/')) {
    form.action = url_search_proceso;
  } else if (current_url.includes('/tarea/')) {
    form.action = url_search_tarea;
  } else {
    form.action = ''
  }
}

function filter_url (form) {
  var current_url = window.location.href
  var url_filter_estacion = '/estaciones/filter/estacion/'
  var url_filter_parte = '/partes/filter/parte/'
  var url_filter_proyeccion_web = '/proyecciones/filter/proyeccion/web/'
  var url_filter_proyeccion_extra = '/proyecciones/filter/proyeccion/extra/'
  var url_filter_hw_actividad = '/hw_actividades/filter/hw/actividad/'
  var url_filter_consumo_nokia = '/consumos/filter/consumo/nokia/'
  var url_filter_consumo_claro= '/consumos/filter/consumo/claro/'
  var url_filter_llegada= '/llegadas/filter/llegada/'
  var url_filter_existencia= '/existencias/filter/existencia/'
  var url_filter_resultado= '/resultados/filter/resultado/'
  var url_filter_impacto= '/impactos/filter/impacto/'
  var url_filter_formato_estacion = '/formatos/filter/formato/estacion/'
  var url_filter_formato_parte = '/formatos/filter/formato/parte/'
  var url_filter_formato_claro = '/formatos/filter/formato/claro/'
  var url_filter_formato_claro_total = '/formatos/filter/formato/claro/total/'
  var url_filter_formato_claro_kit = '/formatos/filter/formato/claro/kit/'
  var url_filter_bitacora_estacion = '/estaciones/filter/bitacora/estacion/'
  var url_filter_proyeccion_estacion = '/estaciones/filter/proyeccion/estacion/'
  var url_filter_rastreo = '/rastreos/filter/rastreo/'
  var url_filter_proceso = '/rastreos/filter/proceso/'
  var url_filter_perfil_rastreo = '/rastreos/filter/perfil/rastreo/'
  var url_filter_perfil_proceso = '/rastreos/filter/perfil/proceso/'
  var url_filter_tarea = '/tareas/filter/tarea/'
  var url_filter_consulta = '/consultas/filter/consulta/'

  if (current_url.includes('/bitacora/estacion/')) {
    form.action = url_filter_bitacora_estacion;
  } else if (current_url.includes('/proyeccion/estacion/')) {
    form.action = url_filter_proyeccion_estacion;
  } else if (current_url.includes('/estacion/')) {
    form.action = url_filter_estacion;
  } else if (current_url.includes('/partes/')) {
    form.action = url_filter_parte;
  } else if (current_url.includes('/proyeccion/web/')) {
    form.action = url_filter_proyeccion_web;
  } else if (current_url.includes('/proyeccion/extra/')) {
    form.action = url_filter_proyeccion_extra;
  } else if (current_url.includes('/hw/actividad/')) {
    form.action = url_filter_hw_actividad;
  } else if (current_url.includes('/consumo/nokia/')) {
    form.action = url_filter_consumo_nokia;
  } else if (current_url.includes('/consumo/claro/')) {
    form.action = url_filter_consumo_claro;
  } else if (current_url.includes('/llegada/')) {
    form.action = url_filter_llegada;
  } else if (current_url.includes('/existencia/')) {
    form.action = url_filter_existencia;
  } else if (current_url.includes('/resultado/')) {
    form.action = url_filter_resultado;
  } else if (current_url.includes('/impacto/')) {
    form.action = url_filter_impacto;
  } else if (current_url.includes('/consulta/')) {
    form.action = url_filter_consulta;
  } else if (current_url.includes('/formato/estacion/')) {
    form.action = url_filter_formato_estacion;
  } else if (current_url.includes('/formato/parte/')) {
    form.action = url_filter_formato_parte;
  } else if (current_url.includes('/formato/claro/total/')) {
    form.action = url_filter_formato_claro_total;
  } else if (current_url.includes('/formato/claro/kit/')) {
    form.action = url_filter_formato_claro_kit;
  } else if (current_url.includes('/formato/claro/')) {
    form.action = url_filter_formato_claro;
  } else if (current_url.includes('/perfil/rastreo/')) {
    form.action = url_filter_perfil_rastreo;
  } else if (current_url.includes('/perfil/proceso/')) {
    form.action = url_filter_perfil_proceso;
  } else if (current_url.includes('/rastreo/')) {
    form.action = url_filter_rastreo;
  } else if (current_url.includes('/proceso/')) {
    form.action = url_filter_proceso;
  } else if (current_url.includes('/tarea/')) {
    form.action = url_filter_tarea;
  } else {
    form.action = ''
  }
}

$("#paginate_by").on('change', function () {
  $(this).submit()
})

if (window.location.href.includes('/perfil/rastreo/')) {
  $('#dashboard').removeClass('content_dashboard');
}

if (window.location.href.includes('/perfil/proceso/')) {
  $('#dashboard').removeClass('content_dashboard');
}
