$(document).ready(function(){
	$('a[href^="http"]').attr('target','_blank');
	var class_results_shown='results-arrived';
	search_submit=function(key){
		spawnpoint.children().remove();
		spawnpoint.jQCloud('destroy');
		search_spawn(key);
		$('body').addClass(class_results_shown);
	};
	$('.js-search-submit').on('click', function(){
		var query=search_input.val();
		search_submit(query);
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
	$('.search-field').submit(function( event ) {
		event.preventDefault();
		search_submit(search_input.val());
	});
});
