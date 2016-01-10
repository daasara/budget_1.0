$(function () {
	var date=$('.date');
	var cal=$('.calendar');
	cal.pickmeup({
		flat: true,
		change:function(formatted){
			date.val(formatted);
		}
	});
});
