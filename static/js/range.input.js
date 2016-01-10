$(function(){
	var date1=$('.start');
	var date2=$('.end');
	var cal=$('.calendar');
	cal.pickmeup({
		flat: true,
		mode: 'range',
		change: function(formatted){
			var range=formatted.toLocaleString().split(',');
			date1.val(range[0]);
			date2.val(range[1]);
		}
	});
});
