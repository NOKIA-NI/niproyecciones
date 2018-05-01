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
  } else {
    form.action = ''
  }
}

var labels = []
var dataImpactos = [];
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
    dataImpactos = data.impactos
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
      dataImpactos = data.impactos
      Impactos()
    },
    error: function(error){
    }
  })
})

function Impactos() {
  var ctx = document.getElementById("impactos");
  ImpactosChart = new Chart(ctx, {
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
        label: 'Estaciones - Impactos',
				backgroundColor: '#2196F3',
        data: dataImpactos,
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
						text: 'Proyeccion Impactos [ Estaciones - Impactos ]'
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
        display: false,
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
				backgroundColor: '#FF9800',
        data: dataImpactosModulos,
        lineTension: 0,
        backgroundColor: '#FF9800',
        borderColor: '#FF9800',
        borderWidth: 4,
        pointBackgroundColor: '#FF9800'
      },
      {
        label: 'Estaciones - Antenas Y Otros',
				backgroundColor: '#F44336',
        data: dataImpactosAntenas,
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
