// event.PreventDefault()
// event.stopPropagation()

$('#table_estacion').on('click', '.clickable-row', function(event) {
  $(this).addClass('active').siblings().removeClass('active');
  $('#update').removeClass('disabled');
  $('#delete').removeClass('disabled');
  $('#action').removeClass('disabled');
  var data = $(this);
  var id = data[0].cells[0].innerText
  window.url_update = '/estaciones/update/estacion'+ '/' +  id + '/';
  window.url_delete = '/estaciones/delete/estacion'+ '/' +  id + '/';
});

function create_estacion (url) {
  $('#create_estacion').load(url, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_estacion (url_update) {
  $('#update_estacion').load(url_update, function() {
    $(this).modal('show')
  });
  event.stopPropagation()
}

function delete_estacion (url_delete) {
  $('#delete_estacion').load(url_delete, function() {
    $(this).modal('show')
  });
  event.stopPropagation()
}

function update_url_estacion (form) {
  form.action = url_update;
}

function delete_url_estacion (form) {
  form.action = url_delete;
}

$('#table_bitacora_estacion').on('click', '.clickable-row', function(event) {
  $(this).addClass('active').siblings().removeClass('active');
  $('#update').removeClass('disabled');
  $('#delete').removeClass('disabled');
  $('#action').removeClass('disabled');
  var data = $(this);
  var id = data[0].cells[0].innerText
  window.url_update = '/estaciones/update/bitacora/estacion'+ '/' +  id + '/';
  window.url_delete = '/estaciones/delete/bitacora/estacion'+ '/' +  id + '/';
});

function create_bitacora_estacion (url) {
  $('#create_bitacora_estacion').load(url, function() {
    $(this).modal('show');
  });
  event.stopPropagation()
}

function update_bitacora_estacion (url_update) {
  $('#update_bitacora_estacion').load(url_update, function() {
    $(this).modal('show')
  });
  event.stopPropagation()
}

function delete_bitacora_estacion (url_delete) {
  $('#delete_bitacora_estacion').load(url_delete, function() {
    $(this).modal('show')
  });
  event.stopPropagation()
}

function update_url_bitacora_estacion (form) {
  form.action = url_update;
}

function delete_url_bitacora_estacion (form) {
  form.action = url_delete;
}

(function($) {
	$.fn.shorten = function (settings) {
		var config = {
			showChars: 100,
			ellipsesText: "...",
			moreText: "more",
			lessText: "less"
		};
		if (settings) {
			$.extend(config, settings);
		}
		$(document).off("click", '.morelink');
		$(document).on({click: function () {
				var $this = $(this);
				if ($this.hasClass('less')) {
					$this.removeClass('less');
					$this.html(config.moreText);
				} else {
					$this.addClass('less');
					$this.html(config.lessText);
				}
				$this.parent().prev().toggle();
				$this.prev().toggle();
				return false;
			}
		}, '.morelink');
		return this.each(function () {
			var $this = $(this);
			if($this.hasClass("shortened")) return;
			$this.addClass("shortened");
			var content = $this.html();
			if (content.length > config.showChars) {
				var c = content.substr(0, config.showChars);
				var h = content.substr(config.showChars, content.length - config.showChars);
				var html = c + '<span class="moreellipses">' + config.ellipsesText + ' </span><span class="morecontent"><span>' + h + '</span> <a href="#" class="morelink">' + config.moreText + '</a></span>';
				$this.html(html);
				$(".morecontent span").hide();
			}
		});
	};
 })(jQuery);

$(".contenido").shorten({
	"showChars" : 80,
	"moreText"	: "Ver Mas",
	"lessText"	: "... Menos",
});
