$(document).ready(function() {
	$("#accounts td").each(function() {
		var value = parseInt($(this).html());
		if (value>0&&value<1000) {
			$(this).addClass("bg-warning");
		}
		if (value<0) {
			$(this).addClass("bg-danger");
		}
	});
});
