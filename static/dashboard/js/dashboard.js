// event.PreventDefault()
// event.stopPropagation()
$('#sidebar-toggle').on('click', function (event) {
  $('.sidebar').toggleClass('d-md-block');
  $('#dashboard').toggleClass('content_dashboard');
  $('#nav_dasboard').toggleClass('content_nav');
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
var dataImpactos = [];
var dataImpactosOne = [];
var dataImpactosTwo = [];
var dataImpactosThree = [];
var dataImpactosAccesorio = [];
var dataImpactosModulo = [];
var dataImpactosAntena = [];
var labels = []

var ImpactosAccesorioChart;
var ImpactosModuloChart;
var ImpactosAntenaChart;

$.ajax({
  method: 'GET',
  url: '/dashboard/get/data',
  success: function(data){
    labels = data.labels
    dataImpactos = data.impactos
    dataImpactosOne = data.impactos_one
    dataImpactosTwo = data.impactos_two
    dataImpactosThree = data.impactos_three
    Impactos()
    ImpactosGrupoParte()
    ImpactosAccesorio()
    ImpactosModulo()
    ImpactosAntena()
  },
  error: function(error){
  }
})

function Impactos() {
  var ctx = document.getElementById("impactos");
  var ImpactosChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Estaciones - Impactos',
				backgroundColor: '#17a2b8',
        data: dataImpactos,
        lineTension: 0,
        backgroundColor: '#17a2b8',
        borderColor: '#17a2b8',
        borderWidth: 4,
        pointBackgroundColor: '#17a2b8'
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

function ImpactosGrupoParte() {
  var ctx = document.getElementById("impactosGrupoParte");
  var ImpactosGrupoParteChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Estaciones - Accesorios',
				backgroundColor: '#ffc107',
        data: dataImpactosOne,
        lineTension: 0,
        backgroundColor: '#ffc107',
        borderColor: '#ffc107',
        borderWidth: 4,
        pointBackgroundColor: '#ffc107'
      },
      {
        label: 'Estaciones - Modulos',
				backgroundColor: '#28a745',
        data: dataImpactosTwo,
        lineTension: 0,
        backgroundColor: '#28a745',
        borderColor: '#28a745',
        borderWidth: 4,
        pointBackgroundColor: '#28a745'
      },
      {
        label: 'Estaciones - Antenas Y Otros',
				backgroundColor: '#dc3545',
        data: dataImpactosThree,
        lineTension: 0,
        backgroundColor: '#dc3545',
        borderColor: '#dc3545',
        borderWidth: 4,
        pointBackgroundColor: '#dc3545'
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
    url: '/dashboard/get/data',
    data: {
        'parte': parte
      },
    dataType: 'json',
    success: function(data){
      if (typeof ImpactosAccesorioChart !== "undefined") {
        ImpactosAccesorioChart.data.labels.pop();
        ImpactosAccesorioChart.data.datasets.pop();
        ImpactosAccesorioChart.update();
      }
      labels = data.labels
      dataImpactosAccesorio = data.impactos_filter
      ImpactosAccesorio()
    },
    error: function(error){
    }
  })
})

function ImpactosAccesorio() {
  var ctx = document.getElementById("ImpactosAccesorio");
  ImpactosAccesorioChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Estaciones - Accesorios',
				backgroundColor: '#17a2b8',
        data: dataImpactosAccesorio,
        lineTension: 0,
        backgroundColor: '#17a2b8',
        borderColor: '#17a2b8',
        borderWidth: 4,
        pointBackgroundColor: '#17a2b8'
      }
    ]
    },
    options: {
      title: {
						display: true,
						text: 'Proyeccion Impactos [ Estaciones - Accesorios ]'
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

$("#modulo").change(function () {
  var parte = $(this).val()
  $.ajax({
    method: 'GET',
    url: '/dashboard/get/data',
    data: {
        'parte': parte
      },
    dataType: 'json',
    success: function(data){
      if (typeof ImpactosModuloChart !== "undefined") {
        ImpactosModuloChart.data.labels.pop();
        ImpactosModuloChart.data.datasets.pop();
        ImpactosModuloChart.update();
      }
      labels = data.labels
      dataImpactosModulo = data.impactos_filter
      ImpactosModulo()
    },
    error: function(error){
    }
  })
})

function ImpactosModulo() {
  var ctx = document.getElementById("ImpactosModulo");
  ImpactosModuloChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Estaciones - Modulos',
				backgroundColor: '#17a2b8',
        data: dataImpactosModulo,
        lineTension: 0,
        backgroundColor: '#17a2b8',
        borderColor: '#17a2b8',
        borderWidth: 4,
        pointBackgroundColor: '#17a2b8'
      }
    ]
    },
    options: {
      title: {
						display: true,
						text: 'Proyeccion Impactos [ Estaciones - Modulos ]'
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

$("#antena").change(function () {
  var parte = $(this).val()
  $.ajax({
    method: 'GET',
    url: '/dashboard/get/data',
    data: {
        'parte': parte
      },
    dataType: 'json',
    success: function(data){
      if (typeof ImpactosAntenaChart !== "undefined") {
        ImpactosAntenaChart.data.labels.pop();
        ImpactosAntenaChart.data.datasets.pop();
        ImpactosAntenaChart.update();
      }
      labels = data.labels
      dataImpactosAntena = data.impactos_filter
      ImpactosAntena()
    },
    error: function(error){
    }
  })
})

function ImpactosAntena() {
  var ctx = document.getElementById("ImpactosAntena");
  ImpactosAntenaChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Estaciones - Antenas y Otros',
				backgroundColor: '#17a2b8',
        data: dataImpactosAntena,
        lineTension: 0,
        backgroundColor: '#17a2b8',
        borderColor: '#17a2b8',
        borderWidth: 4,
        pointBackgroundColor: '#17a2b8'
      }
    ]
    },
    options: {
      title: {
						display: true,
						text: 'Proyeccion Impactos [ Estaciones - Antenas y Otros ]'
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
