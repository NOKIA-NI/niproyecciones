// event.PreventDefault()
// event.stopPropagation()

$('#table_formato_estacion').on('click', '.clickable-row', function(event) {
    $(this).addClass('active').siblings().removeClass('active');
    $('#update').removeClass('disabled');
    $('#delete').removeClass('disabled');
    $('#action').removeClass('disabled');
    var data = $(this);
    var id = data[0].cells[0].innerText
    window.url_update = '/formato_estacions/update/formato_estacion'+ '/' +  id + '/';
    window.url_delete = '/formato_estacions/delete/formato_estacion'+ '/' +  id + '/';
    window.url_detail = '/formato_estacions/detail/formato_estacion'+ '/' +  id + '/';
  });
  
  function create_formato_estacion (url) {
    $('#create_formato_estacion').load(url, function() {
      $(this).modal('show');
    });
    event.stopPropagation()
  }

  function detail_formato_estacion (url_detail) {
    window.location.href=url_detail;
  }
  
  function update_formato_estacion (url_update) {
    $('#update_formato_estacion').load(url_update, function() {
      $(this).modal('show')
    });
    event.stopPropagation()
  }
  
  function delete_formato_estacion (url_delete) {
    $('#delete_formato_estacion').load(url_delete, function() {
      $(this).modal('show')
    });
    event.stopPropagation()
  }
  
  function update_url_formato_estacion (form) {
    form.action = url_update;
  }
  
  function delete_url_formato_estacion (form) {
    form.action = url_delete;
  }

  $('#table_formato_parte').on('click', '.clickable-row', function(event) {
    $(this).addClass('active').siblings().removeClass('active');
    $('#update').removeClass('disabled');
    $('#delete').removeClass('disabled');
    $('#action').removeClass('disabled');
    var data = $(this);
    var id = data[0].cells[0].innerText
    window.url_update = '/formato_partes/update/formato_parte'+ '/' +  id + '/';
    window.url_delete = '/formato_partes/delete/formato_parte'+ '/' +  id + '/';
    window.url_detail = '/formato_partes/detail/formato_parte'+ '/' +  id + '/';
  });
  
  function create_formato_parte (url) {
    $('#create_formato_parte').load(url, function() {
      $(this).modal('show');
    });
    event.stopPropagation()
  }

  function detail_formato_parte (url_detail) {
    window.location.href=url_detail;
  }
  
  function update_formato_parte (url_update) {
    $('#update_formato_parte').load(url_update, function() {
      $(this).modal('show')
    });
    event.stopPropagation()
  }
  
  function delete_formato_parte (url_delete) {
    $('#delete_formato_parte').load(url_delete, function() {
      $(this).modal('show')
    });
    event.stopPropagation()
  }
  
  function update_url_formato_parte (form) {
    form.action = url_update;
  }
  
  function delete_url_formato_parte (form) {
    form.action = url_delete;
  }