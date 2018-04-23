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

var dataImpactosOne = [];
var dataImpactosTwo = [];
var dataImpactosThree = [];
var labels = []

$.ajax({
  method: 'GET',
  url: '/dashboard/get/data',
  success: function(data){
    labels = data.labels
    dataImpactosOne = data.impactos_one
    dataImpactosTwo = data.impactos_two
    dataImpactosThree = data.impactos_three
    setChart()
  },
  error: function(error){
  }
})

function setChart() {
  var ctx = document.getElementById("impactos").getContext('2d');
  var ImpactosChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Antenas',
				backgroundColor: '#007bff',
        data: dataImpactosOne,
        lineTension: 0,
        backgroundColor: '#007bff',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      },
      {
        label: 'Modulos',
				backgroundColor: '#28a745',
        data: dataImpactosTwo,
        lineTension: 0,
        backgroundColor: '#28a745',
        borderColor: '#28a745',
        borderWidth: 4,
        pointBackgroundColor: '#28a745'
      },
      {
        label: 'Antenas Y Otros',
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
