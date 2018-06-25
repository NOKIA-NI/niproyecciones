$("#week").on('change', function () {
    $(this).submit()
  })
  
  var labels = [];
  var dataCronograma = [];
  var dataImpactosSi = [];
  var dataImpactosAntena = [];
  var dataImpactosModuloAccesorio = [];
  var dataImpactosModuloAccesorioAntena = [];
  var dataImpactosNo = [];
  var dataImpactosAccesorios = [];
  var dataImpactosModulos = [];
  var dataImpactosAntenas = [];
  var dataImpactosParteFcImp = [];
  var dataImpactosParteFcSal = [];
  var dataSitioslsm55 = [];
  var dataSitioslsm165 = [];
  var dataSitioslsm170 = [];
  var dataSitioslsm531 = [];
  var dataSitiosbulk = [];
  var dataAirscale167 = [];
  var dataSitioslsmmixto381 = [];
  var dataSitioslsmmixto114 = [];
  var dataSitioslsmmixto78 = [];
  var dataReemplazositioslsm170 = [];
  var dataSitiossatelitaleslsm36 = [];
  var dataReemplazossitiossatelitaleslsm36 = [];
  var dataPartessitioslsm302 = [];
  var dataPendientepedido = [];
  var dataCustomClearance = [];
  var dataCompleteSites = [];
  var dataWaitingCspConfiguration = [];
  var dataPendingProjectHwRequest = [];
  var dataToDispatch = [];
  var dataWaitingFactoryFeedback = [];
  
  var ImpactosChart;
  var CronogramaBolsasChart;
  var CronogramaStatusNokiaChart;
  var ImpactosGrupoParteChart;
  var ImpactosParteChart;
  
  $.ajax({
    method: 'GET',
    url: '/dashboard/impactos',
    success: function(data){
      labels = data.labels
      dataCronograma = data.cronograma
      dataImpactosSi = data.impactos_si
      dataImpactosAntena = data.impactos_antena
      dataImpactosModuloAccesorio = data.impactos_modulo_accesorio
      dataImpactosModuloAccesorioAntena = data.impactos_modulo_accesorio_antena
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
        dataImpactosAntena = data.impactos_antena
        dataImpactosModuloAccesorio = data.impactos_modulo_accesorio
        dataImpactosModuloAccesorioAntena = data.impactos_modulo_accesorio_antena
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
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          type: 'line',
          label: 'Cronogrma',
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
          label: 'Impactos No',
                  backgroundColor: '#2196F3',
          data: dataImpactosNo,
          lineTension: 0,
          backgroundColor: '#2196F3',
          borderColor: '#2196F3',
          borderWidth: 4,
          pointBackgroundColor: '#2196F3'
        },
        // {
        //   type: 'line',
        //   label: 'Impactos Si',
              // 	// backgroundColor: '#FFFF00',
        //   data: dataImpactosSi,
        //   lineTension: 0,
        //   // backgroundColor: '#FFFF00',
        //   // borderColor: '#FFFF00',
        //   borderWidth: 0,
        //   // pointBackgroundColor: '#FFFF00'
        //   fill: false,
        //   showLine: false
        // },
        {
          label: 'Impactos Antena',
                  backgroundColor: '#F44336',
          data: dataImpactosAntena,
          lineTension: 0,
          backgroundColor: '#F44336',
          borderColor: '#F44336',
          borderWidth: 4,
          pointBackgroundColor: '#F44336'
        },
        {
          label: 'Modulo-Accesorio',
                  backgroundColor: '#28a745',
          data: dataImpactosModuloAccesorio,
          lineTension: 0,
          backgroundColor: '#28a745',
          borderColor: '#28a745',
          borderWidth: 4,
          pointBackgroundColor: '#28a745'
        },
        {
          label: 'Impactos Modulo-Accesorio-Antena',
                  backgroundColor: '#6f42c1',
          data: dataImpactosModuloAccesorioAntena,
          lineTension: 0,
          backgroundColor: '#6f42c1',
          borderColor: '#6f42c1',
          borderWidth: 4,
          pointBackgroundColor: '#6f42c1'
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
    url: '/dashboard/cronograma/bolsas',
    success: function(data){
      labels = data.labels
      dataSitioslsm55 = data.sitioslsm55
      dataSitioslsm165 = data.sitioslsm165
      dataSitioslsm170 = data.sitioslsm170
      dataSitioslsm531 = data.sitioslsm531
      dataSitiosbulk = data.sitiosbulk
      dataAirscale167 = data.airscale167
      dataSitioslsmmixto381 = data.sitioslsmmixto381
      dataSitioslsmmixto114 = data.sitioslsmmixto114
      dataSitioslsmmixto78 = data.sitioslsmmixto78
      dataReemplazositioslsm170 = data.reemplazositioslsm170
      dataSitiossatelitaleslsm36 = data.sitiossatelitaleslsm36
      dataReemplazossitiossatelitaleslsm36 = data.reemplazossitiossatelitaleslsm36
      dataPartessitioslsm302 = data.partessitioslsm302
      dataPendientepedido = data.pendientepedido
      CronogramaBolsas()
    },
    error: function(error){
    }
  })
  
  $("#w_fc_cronograma_bolsa").change(function () {
    var w_fc = $(this).val()
    $.ajax({
      method: 'GET',
      url: '/dashboard/cronograma/bolsas',
      data: {
          'w_fc': w_fc
        },
      dataType: 'json',
      success: function(data){
        if (typeof CronogramaBolsasChart !== "undefined") {
          CronogramaBolsasChart.destroy();
        }
        labels = data.labels
        dataSitioslsm55 = data.sitioslsm55
        dataSitioslsm165 = data.sitioslsm165
        dataSitioslsm170 = data.sitioslsm170
        dataSitioslsm531 = data.sitioslsm531
        dataSitiosbulk = data.sitiosbulk
        dataAirscale167 = data.airscale167
        dataSitioslsmmixto381 = data.sitioslsmmixto381
        dataSitioslsmmixto114 = data.sitioslsmmixto114
        dataSitioslsmmixto78 = data.sitioslsmmixto78
        dataReemplazositioslsm170 = data.reemplazositioslsm170
        dataSitiossatelitaleslsm36 = data.sitiossatelitaleslsm36
        dataReemplazossitiossatelitaleslsm36 = data.reemplazossitiossatelitaleslsm36
        dataPartessitioslsm302 = data.partessitioslsm302
        dataPendientepedido = data.pendientepedido
        CronogramaBolsas()
      },
      error: function(error){
      }
    })
  })
  
  function CronogramaBolsas() {
    var ctx = document.getElementById("cronogramaBolsas");
    CronogramaBolsasChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'LSM 55',
                  backgroundColor: '#ffc107',
          data: dataSitioslsm55,
          lineTension: 0,
          backgroundColor: '#ffc107',
          borderColor: '#ffc107',
          borderWidth: 4,
          pointBackgroundColor: '#ffc107'
        },
        {
          label: 'LSM 165',
                  backgroundColor: '#fd7e14',
          data: dataSitioslsm165,
          lineTension: 0,
          backgroundColor: '#fd7e14',
          borderColor: '#fd7e14',
          borderWidth: 4,
          pointBackgroundColor: '#fd7e14'
        },
        {
          label: 'LSM 170',
                  backgroundColor: '#28a745',
          data: dataSitioslsm170,
          lineTension: 0,
          backgroundColor: '#28a745',
          borderColor: '#28a745',
          borderWidth: 4,
          pointBackgroundColor: '#28a745'
        },
        {
          label: 'LSM 531',
                  backgroundColor: '#dc3545',
          data: dataSitioslsm531,
          lineTension: 0,
          backgroundColor: '#dc3545',
          borderColor: '#dc3545',
          borderWidth: 4,
          pointBackgroundColor: '#dc3545'
        },
        {
          label: 'Bulk',
                  backgroundColor: '#17a2b8',
          data: dataSitiosbulk,
          lineTension: 0,
          backgroundColor: '#17a2b8',
          borderColor: '#17a2b8',
          borderWidth: 4,
          pointBackgroundColor: '#17a2b8'
        },
        {
          label: 'Airscale 167',
                  backgroundColor: '#20c997',
          data: dataAirscale167,
          lineTension: 0,
          backgroundColor: '#20c997',
          borderColor: '#20c997',
          borderWidth: 4,
          pointBackgroundColor: '#20c997'
        },
        {
          label: 'LSM 381 Mixto (Airscale + FSMF)',
                  backgroundColor: '#6f42c1',
          data: dataSitioslsmmixto381,
          lineTension: 0,
          backgroundColor: '#6f42c1',
          borderColor: '#6f42c1',
          borderWidth: 4,
          pointBackgroundColor: '#6f42c1'
        },
        {
          label: 'LSM 114 Mixto (Airscale + FSMF)',
                  backgroundColor: '#3E2723',
          data: dataSitioslsmmixto114,
          lineTension: 0,
          backgroundColor: '#3E2723',
          borderColor: '#3E2723',
          borderWidth: 4,
          pointBackgroundColor: '#3E2723'
        },
        {
          label: 'LSM 78 Mixto (Airscale + FSMF)',
                  backgroundColor: '#3F51B5',
          data: dataSitioslsmmixto114,
          lineTension: 0,
          backgroundColor: '#3F51B5',
          borderColor: '#3F51B5',
          borderWidth: 4,
          pointBackgroundColor: '#3F51B5'
        },
        {
          label: 'Reemplazos LSM 170',
                  backgroundColor: '#e83e8c',
          data: dataReemplazositioslsm170,
          lineTension: 0,
          backgroundColor: '#e83e8c',
          borderColor: '#e83e8c',
          borderWidth: 4,
          pointBackgroundColor: '#e83e8c'
        },
        {
          label: 'Satelitales LSM 36',
                  backgroundColor: '#6c757d',
          data: dataSitiossatelitaleslsm36,
          lineTension: 0,
          backgroundColor: '#6c757d',
          borderColor: '#6c757d',
          borderWidth: 4,
          pointBackgroundColor: '#6c757d'
        },
        {
          label: 'Reemplazos Satelitales LSM 36',
                  backgroundColor: '#343a40',
          data: dataReemplazossitiossatelitaleslsm36,
          lineTension: 0,
          backgroundColor: '#343a40',
          borderColor: '#343a40',
          borderWidth: 4,
          pointBackgroundColor: '#343a40'
        },
        {
          label: 'Partes LSM 302',
                  backgroundColor: '#007bff',
          data: dataPartessitioslsm302,
          lineTension: 0,
          backgroundColor: '#007bff',
          borderColor: '#007bff',
          borderWidth: 4,
          pointBackgroundColor: '#007bff'
        },
        {
          label: 'Pendiente Pedido',
                  backgroundColor: '#FFFF00',
          data: dataPendientepedido,
          lineTension: 0,
          backgroundColor: '#FFFF00',
          borderColor: '#FFFF00',
          borderWidth: 4,
          pointBackgroundColor: '#FFFF00'
        }
      ]
      },
      options: {
        title: {
                          display: true,
                          text: 'Proyeccion Cronograma [ Estaciones - Bolsas ]'
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
    url: '/dashboard/cronograma/status/nokia',
    success: function(data){
      labels = data.labels
      dataCustomClearance = data.custom_clearance
      dataCompleteSites = data.complete_sites
      dataWaitingCspConfiguration = data.waiting_csp_configuration
      dataPendingProjectHwRequest = data.pending_project_hw_request
      dataToDispatch = data.to_dispatch
      dataWaitingFactoryFeedback = data.waiting_factory_feedback
      CronogramaStatusNokia()
    },
    error: function(error){
    }
  })
  
  $("#w_fc_cronograma_status_nokia").change(function () {
    var w_fc = $(this).val()
    $.ajax({
      method: 'GET',
      url: '/dashboard/cronograma/status/nokia',
      data: {
          'w_fc': w_fc
        },
      dataType: 'json',
      success: function(data){
        if (typeof CronogramaStatusNokiaChart !== "undefined") {
          CronogramaStatusNokiaChart.destroy();
        }
        labels = data.labels
        dataCustomClearance = data.custom_clearance
        dataCompleteSites = data.complete_sites
        dataWaitingCspConfiguration = data.waiting_csp_configuration
        dataPendingProjectHwRequest = data.pending_project_hw_request
        dataToDispatch = data.to_dispatch
        dataWaitingFactoryFeedback = data.waiting_factory_feedback
        CronogramaStatusNokia()
      },
      error: function(error){
      }
    })
  })
  
  function CronogramaStatusNokia() {
    var ctx = document.getElementById("cronogramaStatusNokia");
    CronogramaStatusNokiaChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
            label: 'Complete Sites',
            backgroundColor: '#007bff',
            data: dataCompleteSites,
            lineTension: 0,
            backgroundColor: '#007bff',
            borderColor: '#007bff',
            borderWidth: 4,
            pointBackgroundColor: '#007bff'
          },
          {
          label: 'Custom Clearance',
                  backgroundColor: '#FFCDD2',
          data: dataCustomClearance,
          lineTension: 0,
          backgroundColor: '#FFCDD2',
          borderColor: '#FFCDD2',
          borderWidth: 4,
          pointBackgroundColor: '#FFCDD2'
        },
        {
          label: 'Waiting CSP Configuration',
                  backgroundColor: '#dc3545',
          data: dataWaitingCspConfiguration,
          lineTension: 0,
          backgroundColor: '#dc3545',
          borderColor: '#dc3545',
          borderWidth: 4,
          pointBackgroundColor: '#dc3545'
        },
        {
          label: 'Pending Project HW Request',
                  backgroundColor: '#28a745',
          data: dataPendingProjectHwRequest,
          lineTension: 0,
          backgroundColor: '#28a745',
          borderColor: '#28a745',
          borderWidth: 4,
          pointBackgroundColor: '#28a745'
        },
        {
          label: 'To Dispatch',
                  backgroundColor: '#6f42c1',
          data: dataToDispatch,
          lineTension: 0,
          backgroundColor: '#6f42c1',
          borderColor: '#6f42c1',
          borderWidth: 4,
          pointBackgroundColor: '#6f42c1'
        },
        {
          label: 'Waiting Factory Feedback',
                  backgroundColor: '#FFFF00',
          data: dataWaitingFactoryFeedback,
          lineTension: 0,
          backgroundColor: '#FFFF00',
          borderColor: '#FFFF00',
          borderWidth: 4,
          pointBackgroundColor: '#FFFF00'
        }
      ]
      },
      options: {
        title: {
                          display: true,
                          text: 'Proyeccion Cronograma [ Estaciones - Status Nokia ]'
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