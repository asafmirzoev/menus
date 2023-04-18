$(document).on('click', '.list-group-item', function () {
	let href = $(this).data('url');
	window.history.pushState({href: href}, '', href);
});