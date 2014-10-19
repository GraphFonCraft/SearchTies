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
		}, 1000);
		$('body').addClass(class_results_shown);
	};
	$('.js-search-submit').on('click', function(){
		search_submit(0);
	});
	$('.js-search-suggestion').on('click', function(){
		el=$(this);
		search_submit_helper(el);
		search_submit(el.data('query'));
	});
	$('.js-results-item').on('click', function(){
		el=$(this);
		search_submit_helper(el);
		search_submit(el.html());
		console.log('i am a love');
	});
});
