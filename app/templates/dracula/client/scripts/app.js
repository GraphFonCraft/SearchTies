$(document).ready(function(){
	$('a[href^="http"]').attr('target','_blank');
	var class_results_shown='results-arrived';
	var spawnpoint=$('.js-results-spawn');
	search_submit=function(key){
		var testdata_id;
		switch(key) {
			case 0:
				testdata_id = testdata0;
				break;
			case 1:
				testdata_id = testdata1;
				break;
			case 2:
				testdata_id = testdata2;
				break;
		}
		spawnpoint.children().remove();
		spawnpoint.jQCloud('destroy');
		spawnpoint.jQCloud(testdata_id);
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
