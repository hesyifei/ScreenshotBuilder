var generateImageUrl = "/generateImage";

$(document).ready(function() {
	console.log("document ready");

	if (!("FormData" in window)) {
		// FormData is not supported; degrade gracefully/ alert the user as appropiate
		alert("FormData is not supported on your browser! Please try a modern browser!")
	}

	$('.input-color-picker').colorpicker({
		format: "hex"
	});

	$(".screenshot-input-image input:file").change(function (){
		var file = this.files[0];
		var reader = new FileReader();
		reader.readAsDataURL(file);

		console.log('inputImage changed');

		var $thisForm = $(this).closest('form');
		uploadScreenshotInfo($thisForm, true);
	});


	var inputTextTypeWatchOptions = {
		callback: function (value) {
			console.log('typeWatch callback: (' + (this.type || this.nodeName) + ') ' + value);
			uploadScreenshotInfo($(this), false);
		},
		wait: 750,
		highlight: true,
		allowSubmit: false,
		captureLength: 0
	}
	$(".input-text").typeWatch(inputTextTypeWatchOptions);

	$('.input-color-picker').focusout(function() {
		console.log('input-color-picker changed');
		uploadScreenshotInfo($(this), false);
	});

});


function uploadScreenshotInfo($currentThis, containScreenshot) {
	console.log($currentThis);

	inputScreenshotId = $currentThis.closest("li.screenshot-item").attr('id').replace(/screenshotItem/, "");
	inputPrefix = $("#inputPrefix").val() + "_" + inputScreenshotId;
	if(inputPrefix.length == 0){
		return;
	}
	console.log(inputPrefix);

	$inputForm = $($currentThis[0].closest("div.screenshot-input-form"));
	inputTextVal = $.trim($($inputForm.find(".input-text")).val());
	inputBgColor = $($($inputForm).find(".input-bg-color")).val();
	console.log(inputTextVal);
	console.log(inputBgColor);

	var serializedData;
	if(containScreenshot){
		serializedData = new FormData($currentThis[0]);
	}else{
		serializedData = new FormData();
	}
	serializedData.append('inputText', inputTextVal);
	serializedData.append('inputBgColor', inputBgColor);
	serializedData.append('inputPrefix', inputPrefix);
	console.log(serializedData);


	request = $.ajax({
		type: "POST",
		url: generateImageUrl,
		data: serializedData,
		contentType: false,
		processData: false
	});

	request.done(function (response, textStatus, jqXHR){
		console.log("AJAX get success result: "+response);

		$resultImage = $($($currentThis.closest("div.screenshot-input-form")).prev("div.screenshot-image")).find('.result-image');
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
