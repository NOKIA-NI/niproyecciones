// event.PreventDefault()
// event.stopPropagation()
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

function search_url (form) {
  var current_url = window.location.href
  var url_search_estacion = '/estaciones/search/estacion/'
  var url_search_parte = '/partes/search/parte/'
  var url_search_proyeccion = '/proyecciones/search/proyeccion/'
  var url_search_hw_actividad = '/hw_actividades/search/hw/actividad/'
  var url_search_consumo_nokia = '/consumos/search/consumo/nokia/'
  var url_search_consumo_claro= '/consumos/search/consumo/claro/'
  var url_search_llegada= '/llegadas/search/llegada/'
  var url_search_existencia= '/existencias/search/existencia/'
  var url_search_resultado= '/resultados/search/resultado/'
  var url_search_impacto= '/impactos/search/impacto/'

  if (current_url.includes('/estaciones/')) {
    form.action = url_search_estacion;
  } else if (current_url.includes('/partes/')) {
    form.action = url_search_parte;
  } else if (current_url.includes('/proyecciones/')) {
    form.action = url_search_proyeccion;
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
  } else {
    form.action = ''
  }
}

function filter_url (form) {
  var current_url = window.location.href
  var url_filter_estacion = '/estaciones/filter/estacion/'
  var url_filter_parte = '/partes/filter/parte/'
  var url_filter_proyeccion = '/proyecciones/filter/proyeccion/'
  var url_filter_hw_actividad = '/hw_actividades/filter/hw/actividad/'
  var url_filter_consumo_nokia = '/consumos/filter/consumo/nokia/'
  var url_filter_consumo_claro= '/consumos/filter/consumo/claro/'
  var url_filter_llegada= '/llegadas/filter/llegada/'
  var url_filter_existencia= '/existencias/filter/existencia/'
  var url_filter_resultado= '/resultados/filter/resultado/'
  var url_filter_impacto= '/impactos/filter/impacto/'

  if (current_url.includes('/estaciones/')) {
    form.action = url_filter_estacion;
  } else if (current_url.includes('/partes/')) {
    form.action = url_filter_parte;
  } else if (current_url.includes('/proyecciones/')) {
    form.action = url_filter_proyeccion;
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
  } else {
    form.action = ''
  }
}

$("#paginate_by").on('change', function () {
  $(this).submit()
})

$("#week").on('change', function () {
  $(this).submit()
})

var labels = []
var dataCronograma = [];
var dataImpactosSi = [];
var dataImpactosNo = [];
var dataImpactosAccesorios = [];
var dataImpactosModulos = [];
var dataImpactosAntenas = [];
var dataImpactosParteFcImp = [];
var dataImpactosParteFcSal = [];

var ImpactosChart;
var ImpactosGrupoParteChart;
var ImpactosParteChart;

$.ajax({
  method: 'GET',
  url: '/dashboard/impactos',
  success: function(data){
    labels = data.labels
    dataCronograma = data.cronograma
    dataImpactosSi = data.impactos_si
    dataImpactosNo = data.impactos_no
    Impactos()
    ImpactosParte()
  },
  error: function(error){
  }
})

$("#w_fc_impacto").change(function () {
  var w_fc = $(this).val()
  $.ajax({
    method: 'GET',
    url: '/dashboard/impactos',
    data: {
        'w_fc': w_fc
      },
    dataType: 'json',
    success: function(data){
      if (typeof ImpactosChart !== "undefined") {
        ImpactosChart.destroy();
      }
      labels = data.labels
      dataCronograma = data.cronograma
      dataImpactosSi = data.impactos_si
      dataImpactosNo = data.impactos_no
      Impactos()
    },
    error: function(error){
    }
  })
})

function Impactos() {
  var ctx = document.getElementById("impactos");
  ImpactosChart = new Chart(ctx, {
    // plugins: [{
    //   afterDatasetsDraw: function(chart) {
		// 		var ctx = chart.ctx;

		// 		chart.data.datasets.forEach(function(dataset, i) {
		// 			var meta = chart.getDatasetMeta(i);
		// 			if (!meta.hidden) {
		// 				meta.data.forEach(function(element, index) {
		// 					// Draw the text in black, with the specified font
		// 					ctx.fillStyle = 'rgb(0, 0, 0)';

		// 					var fontSize = 14;
		// 					var fontStyle = 'normal';
		// 					var fontFamily = 'Helvetica Neue';
		// 					ctx.font = Chart.helpers.fontString(fontSize, fontStyle, fontFamily);

		// 					// Just naively convert to string for now
		// 					var dataString = dataset.data[index].toString();

		// 					// Make sure alignment settings are correct
		// 					ctx.textAlign = 'center';
		// 					ctx.textBaseline = 'middle';

		// 					var padding = 5;
		// 					var position = element.tooltipPosition();
		// 					ctx.fillText(dataString, position.x, position.y - (fontSize / 2) - padding);
		// 				});
		// 			}
		// 		});
		// 	}
    // }],
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
          type: 'line',
          label: 'Estaciones - Cronogrma',
          // backgroundColor: '#2196F3',
          data: dataCronograma,
          lineTension: 0,
          // backgroundColor: '#2196F3',
          // borderColor: '#2196F3',
          borderWidth: 0,
          // pointBackgroundColor: '#2196F3',
          fill: false,
          showLine: false
        },
        {
        label: 'Estaciones - Impactos No',
				backgroundColor: '#4CAF50',
        data: dataImpactosNo,
        lineTension: 0,
        backgroundColor: '#4CAF50',
        borderColor: '#4CAF50',
        borderWidth: 4,
        pointBackgroundColor: '#4CAF50'
      },
      {
        label: 'Estaciones - Impactos Si',
				backgroundColor: '#F44336',
        data: dataImpactosSi,
        lineTension: 0,
        backgroundColor: '#F44336',
        borderColor: '#F44336',
        borderWidth: 4,
        pointBackgroundColor: '#F44336'
      }
    ]
    },
    options: {
      title: {
						display: true,
						text: 'Proyeccion Impactos [ Estaciones - Impactos ]'
					},
      tooltips: {
						mode: 'index',
						intersect: false
					},
      responsive: true,
      scales: {
        xAxes: [{
          stacked: true,
          scaleLabel: {
						display: true,
						labelString: 'Semanas'
					}
				}],
				yAxes: [{
          stacked: true,
          scaleLabel: {
						display: true,
						labelString: 'Estaciones'
					}
				}]
      },
      legend: {
        display: true,
      }
    }
  });
}

$.ajax({
  method: 'GET',
  url: '/dashboard/impactos/grupo/parte',
  success: function(data){
    labels = data.labels
    dataImpactosAccesorios = data.impactos_accesorios
    dataImpactosModulos = data.impactos_modulos
    dataImpactosAntenas = data.impactos_antenas
    ImpactosGrupoParte()
  },
  error: function(error){
  }
})

$("#w_fc_grupo_parte").change(function () {
  var w_fc = $(this).val()
  $.ajax({
    method: 'GET',
    url: '/dashboard/impactos/grupo/parte',
    data: {
        'w_fc': w_fc
      },
    dataType: 'json',
    success: function(data){
      if (typeof ImpactosGrupoParteChart !== "undefined") {
        ImpactosGrupoParteChart.destroy();
      }
      labels = data.labels
      dataImpactosAccesorios = data.impactos_accesorios
      dataImpactosModulos = data.impactos_modulos
      dataImpactosAntenas = data.impactos_antenas
      ImpactosGrupoParte()
    },
    error: function(error){
    }
  })
})

function ImpactosGrupoParte() {
  var ctx = document.getElementById("impactosGrupoParte");
  ImpactosGrupoParteChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Estaciones - Accesorios',
				backgroundColor: '#4CAF50',
        data: dataImpactosAccesorios,
        lineTension: 0,
        backgroundColor: '#4CAF50',
        borderColor: '#4CAF50',
        borderWidth: 4,
        pointBackgroundColor: '#4CAF50'
      },
      {
        label: 'Estaciones - Modulos',
				backgroundColor: '#FFD600',
        data: dataImpactosModulos,
        lineTension: 0,
        backgroundColor: '#FFD600',
        borderColor: '#FFD600',
        borderWidth: 4,
        pointBackgroundColor: '#FFD600'
      },
      {
        label: 'Estaciones - Antenas Y Otros',
				backgroundColor: '#2196F3',
        data: dataImpactosAntenas,
        lineTension: 0,
        backgroundColor: '#2196F3',
        borderColor: '#2196F3',
        borderWidth: 4,
        pointBackgroundColor: '#2196F3'
      }
    ]
    },
    options: {
      title: {
						display: true,
						text: 'Proyeccion Impactos [ Estaciones - Grupo Partes ]'
					},
      tooltips: {
						mode: 'index',
						intersect: false
					},
      responsive: true,
      scales: {
        xAxes: [{
					stacked: true,
          scaleLabel: {
								display: true,
								labelString: 'Semanas'
							}
				}],
				yAxes: [{
					stacked: true,
          scaleLabel: {
								display: true,
								labelString: 'Estaciones'
							}
				}]
      },
      legend: {
        display: true,
      }
    }
  });
}

$("#accesorio").change(function () {
  var parte = $(this).val()
  $.ajax({
    method: 'GET',
    url: '/dashboard/impactos/parte',
    data: {
        'parte': parte
      },
    dataType: 'json',
    success: function(data){
      if (typeof ImpactosParteChart !== "undefined") {
        ImpactosParteChart.destroy();
      }
      labels = data.labels
      dataImpactosParteFcImp = data.impactos_parte_fc_imp
      dataImpactosParteFcSal = data.impactos_parte_fc_sal
      ImpactosParte()
    },
    error: function(error){
    }
  })
})

$("#modulo").change(function () {
  var parte = $(this).val()
  $.ajax({
    method: 'GET',
    url: '/dashboard/impactos/parte',
    data: {
        'parte': parte
      },
    dataType: 'json',
    success: function(data){
      if (typeof ImpactosParteChart !== "undefined") {
        ImpactosParteChart.destroy();
      }
      labels = data.labels
      dataImpactosParteFcImp = data.impactos_parte_fc_imp
      dataImpactosParteFcSal = data.impactos_parte_fc_sal
      ImpactosParte()
    },
    error: function(error){
    }
  })
})

$("#antena").change(function () {
  var parte = $(this).val()
  $.ajax({
    method: 'GET',
    url: '/dashboard/impactos/parte',
    data: {
        'parte': parte
      },
    dataType: 'json',
    success: function(data){
      if (typeof ImpactosParteChart !== "undefined") {
        ImpactosParteChart.destroy();
      }
      labels = data.labels
      dataImpactosParteFcImp = data.impactos_parte_fc_imp
      dataImpactosParteFcSal = data.impactos_parte_fc_sal
      ImpactosParte()
    },
    error: function(error){
    }
  })
})

function ImpactosParte() {
  var ctx = document.getElementById("ImpactosParte");
  ImpactosParteChart = new Chart(ctx, {
    plugins: [{
      afterDatasetsDraw: function(chart) {
				var ctx = chart.ctx;

				chart.data.datasets.forEach(function(dataset, i) {
					var meta = chart.getDatasetMeta(i);
					if (!meta.hidden) {
						meta.data.forEach(function(element, index) {
							// Draw the text in black, with the specified font
							ctx.fillStyle = 'rgb(0, 0, 0)';

							var fontSize = 14;
							var fontStyle = 'normal';
							var fontFamily = 'Helvetica Neue';
							ctx.font = Chart.helpers.fontString(fontSize, fontStyle, fontFamily);

							// Just naively convert to string for now
							var dataString = dataset.data[index].toString();

							// Make sure alignment settings are correct
							ctx.textAlign = 'center';
							ctx.textBaseline = 'middle';

							var padding = 5;
							var position = element.tooltipPosition();
							ctx.fillText(dataString, position.x, position.y - (fontSize / 2) - padding);
						});
					}
				});
			}
    }],
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Estaciones - Impactos - Parte - fc imp',
				backgroundColor: '#2196F3',
        data: dataImpactosParteFcImp,
        lineTension: 0,
        backgroundColor: '#2196F3',
        borderColor: '#2196F3',
        borderWidth: 4,
        pointBackgroundColor: '#2196F3'
      },
      {
        label: 'Estaciones - Impactos - Parte - fc sal',
				backgroundColor: '#4CAF50',
        data: dataImpactosParteFcSal,
        lineTension: 0,
        backgroundColor: '#4CAF50',
        borderColor: '#4CAF50',
        borderWidth: 4,
        pointBackgroundColor: '#4CAF50'
      }
    ]
    },
    options: {
      title: {
						display: true,
						text: 'Proyeccion Impactos [ Estaciones - Impactos - Parte ]'
					},
      tooltips: {
						mode: 'index',
						intersect: false
					},
      responsive: true,
      scales: {
        xAxes: [{
          ticks: {
            beginAtZero: false
          },
          scaleLabel: {
						display: true,
						labelString: 'Semanas'
					}
				}],
				yAxes: [{
          ticks: {
            beginAtZero: false
          },
          scaleLabel: {
						display: true,
						labelString: 'Estaciones'
					}
				}]
      },
      legend: {
        display: true,
      }
    }
  });
}
