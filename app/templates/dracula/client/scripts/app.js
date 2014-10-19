$(document).ready(function(){
	$('a[href^="http"]').attr('target','_blank');
	var class_results_shown='results-arrived';
	search_submit=function(key){
		spawnpoint.children().remove();
		spawnpoint.jQCloud('destroy');
		spawnpoint.append('<div class="spin" data-spin />');
		var spin=spawnpoint.find('.spin');
		spin.spin({
			width: 10,
			length: 20,
			radius: 50,
			trail: 30,
			color: 'lightgray',
			hwaccel: true
		});
		setTimeout(function(){
			spin.remove();
			search_spawn(key);
		}, 3000);
		$('body').addClass(class_results_shown);
	};
	$('.js-search-submit').on('click', function(){
		search_submit(0);
	});
	$('.js-search-suggestion').on('click', function(){
		$('.search-wrapper-target').find('input').val($(this).html());
		search_submit($(this).data('query'));
	});
});
