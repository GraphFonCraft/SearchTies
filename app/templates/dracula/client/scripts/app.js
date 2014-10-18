$(document).ready(function(){
	$('a[href^="http"]').attr('target','_blank');
	var class_results_shown='results-arrived';
	$('.js-search-submit').on('click', function(){
		var spawnpoint=$('.js-results-spawn');
		spawnpoint.jQCloud(testdata);
		$('.search-wrapper-target').find('input').val(testdata_query);
		$('body').addClass(class_results_shown);
	});
});
