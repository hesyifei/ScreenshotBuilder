var generateImageUrl = "/generateImage";

$(document).ready(function() {
	console.log("document ready");

	if (!("FormData" in window)) {
		// FormData is not supported; degrade gracefully/ alert the user as appropiate
		alert("FormData is not supported on your browser! Please try a modern browser!")
	}

	$(".screenshot-input-image input:file").change(function (){
		var file = this.files[0];
		var reader = new FileReader();
		reader.readAsDataURL(file);

		console.log('inputImage changed');

		var $thisForm = $(this).closest('form')[0];
		uploadScreenshotInfo($thisForm, $($($thisForm.closest("div.screenshot-input-form")).find("#inputText")).val(), true);
	});


	var inputTextTypeWatchOptions = {
		callback: function (value) {
			console.log('inputText changed: (' + (this.type || this.nodeName) + ') ' + value);
			uploadScreenshotInfo($(this), value, false);
		},
		wait: 750,
		highlight: true,
		allowSubmit: false,
		captureLength: 0
	}
	$("#inputText").typeWatch(inputTextTypeWatchOptions);

});


function uploadScreenshotInfo($currentThis, inputText, containScreenshot) {
	console.log($currentThis);

	inputTextVal = inputText;
	inputPrefix = $("#inputPrefix").val();
	if(inputPrefix.length == 0){
		return;
	}

	if(containScreenshot){
		serializedData = new FormData($currentThis);
		serializedData.append('inputText', inputTextVal);
		serializedData.append('inputPrefix', inputPrefix);
	}else{
		serializedData = {
			'inputText': inputTextVal,
			'inputPrefix': inputPrefix
		}
	}
	console.log(serializedData);


	if(containScreenshot){
		request = $.ajax({
			type: "POST",
			url: generateImageUrl,
			data: serializedData,
			contentType: false,
			processData: false
		});
	}else{
		request = $.ajax({
			type: "POST",
			url: generateImageUrl,
			data: serializedData
		});
	}

	request.done(function (response, textStatus, jqXHR){
		console.log("AJAX get success result: "+response);

		$resultImage = $($($currentThis.closest("div.screenshot-input-form")).prev("div.screenshot-image")).find('#result-image');
		console.log($resultImage);

		$resultImage.attr("data-original-image-name", response['oriImgFileName']);
		$resultImage.attr("src", response['imgBase64']);
	});

	request.fail(function (jqXHR, textStatus, errorThrown){
		console.error("AJAX get error: "+textStatus, errorThrown);
	});

	request.always(function () {
	});
}
