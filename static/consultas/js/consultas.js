// event.PreventDefault()
// event.stopPropagation()

$('#table_consulta').on('click', '.clickable-row', function(event) {
    $(this).addClass('active').siblings().removeClass('active');
    $('#update').removeClass('disabled');
    $('#delete').removeClass('disabled');
    $('#action').removeClass('disabled');
    var data = $(this);
    var id = data[0].cells[0].innerText
    window.url_update = '/consultas/update/consulta'+ '/' +  id + '/';
    window.url_delete = '/consultas/delete/consulta'+ '/' +  id + '/';
    window.url_detail = '/consultas/detail/consulta'+ '/' +  id + '/';
  });
  
  function create_consulta (url) {
    $('#create_consulta').load(url, function() {
      $(this).modal('show');
    });
    event.stopPropagation()
  }

  function detail_consulta (url_detail) {
    window.location.href=url_detail;
  }
  
  function update_consulta (url_update) {
    $('#update_consulta').load(url_update, function() {
      $(this).modal('show')
    });
    event.stopPropagation()
  }
  
  function delete_consulta (url_delete) {
    $('#delete_consulta').load(url_delete, function() {
      $(this).modal('show')
    });
    event.stopPropagation()
  }
  
  function update_url_consulta (form) {
    form.action = url_update;
  }
  
  function delete_url_consulta (form) {
    form.action = url_delete;
  }