$(document).ready(function(){
	$('a[href^="http"]').attr('target','_blank');
	$('.js-search-submit').on('click', function(){
		var spawnpoint=$('.js-results-spawn'),
			list_wrapper='ul',
			list_item_class='results-item',
			list_class=list_item_class+'s';
		spawnpoint.append('<'+list_wrapper+'>');
		for(var i=0; i<testdata.length; ++i) {
			var item=testdata[i]
			//console.log('part: '+item);
			spawnpoint.find(list_wrapper)
				.addClass(list_class)
				.append(''
					+'<li class="'
						+list_item_class
					+' secondary radius label" data-weight='
						+item.weight
					+' data-source='
						+item.source
					+'>'
					+item.title)
		}
	});
});
