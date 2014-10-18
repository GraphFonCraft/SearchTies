$(document).ready(function(){
	$('a[href^="http"]').attr('target','_blank');
	var class_results_shown='results-arrived';
	var spawnpoint=$('.js-results-spawn');
	search_submit=function(key){
		spawnpoint.children().remove();
		spawnpoint.jQCloud('destroy');
		spawnpoint.jQCloud(eval('testdata'+key));
		$('body').addClass(class_results_shown);
	};
	$('.js-search-submit').on('click', function(){
		search_submit(0);
	});
	$('.js-search-suggestion').on('click', function(){
		$('.search-wrapper-target').find('input').val($(this).html());
		search_submit($(this).data('id'));
	});
});
