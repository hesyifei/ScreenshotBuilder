$(document).ready(function() {
	console.log("document ready");


	// Clear event
	$('.image-preview-clear').click(function(){
		$('.image-preview-filename').val("");
		$('.image-preview-clear').hide();
		$('.image-preview-input input:file').val("");
		$(".image-preview-input-title").text("Browse");
	});
	// Create the preview image
	$(".image-preview-input input:file").change(function (){
		var file = this.files[0];
		var reader = new FileReader();
		// Set preview image into the popover data-content
		reader.onload = function (e) {
			$(".image-preview-input-title").text("Change");
			$(".image-preview-clear").show();
			$(".image-preview-filename").val(file.name);
		}
		reader.readAsDataURL(file);
	});


	var request;

	// NOTE: #mainForm is form ID
	$("#mainForm :input").change(function() {

		console.log("submitted #main-form form");
		//event.preventDefault();

		if (request) {
			request.abort();
		}

		$thisForm = $('#mainForm');

		$inputText = $("#inputText");
		$inputImage = $("#inputImage");
		if( (!$.trim($inputText.val())) || (!$.trim($inputImage.val())) ){
			//alert("Input cannot be empty!");
		}else{
			var serializedData = new FormData($thisForm[0]);

			request = $.ajax({
				type: $thisForm.attr('method') || 'POST',
				url: $thisForm.attr('action') || window.location.pathname + window.location.search,
				data: serializedData,
				contentType: false,
				processData: false
			});

			request.done(function (response, textStatus, jqXHR){
				console.log("AJAX get success result: "+response);

				$('#result-image').attr("data-original-image-name", response['oriImgFileName']);
				$('#result-image').attr("src", response['imgBase64']);

			});

			request.fail(function (jqXHR, textStatus, errorThrown){
				console.error("AJAX get error: "+textStatus, errorThrown);
			});

			request.always(function () {
			});
		}
	});

});