import base64
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO


def generateImage():
	width, height = (1080, 1920)
	backgroundColor = "blue"
	deviceName = "nexus_6p"
	deviceOrientation = "port"
	screenWidth, screenHeight = (1440, 2560)
	screenPaddingLeft, screenPaddingTop = (195, 329)
	screenshot = "screenshot.png"
	textInfo = {
		"text": "Hello\nWorld!",
		"textColor": "white",
		"fontSize": 100,
		"fontFile": "Georgia Italic.ttf",
		"paddingBorderRatio": 0.04,
		"paddingDeviceRatio": 0.04,
		"paddingEachLine": 20
	}




	bg = Image.new("RGB", (width, height), backgroundColor)


	lines = textInfo['text'].split("\n")

	draw = ImageDraw.Draw(bg)
	font = ImageFont.truetype(textInfo['fontFile'], textInfo['fontSize'])
	totalTextHeight = height*textInfo['paddingBorderRatio']
	paddingEachLine = textInfo['paddingEachLine']
	for line in lines:
		textWidth, textHeight = draw.textsize(line, font=font)
		draw.text(((width - textWidth) / 2, totalTextHeight), line, fill=textInfo['textColor'], font=font)
		totalTextHeight += textHeight + paddingEachLine
	# remove last extra padding & padding to border in order to get exact text height
	totalTextHeight = totalTextHeight - height*textInfo['paddingBorderRatio'] - paddingEachLine



	deviceImagePathPrefix = "device_image/"+deviceName+"/"+deviceOrientation

	deviceBg = Image.open(deviceImagePathPrefix+"_back.png")
	oriDeviceSize = deviceBg.size
	deviceBg.thumbnail((width, height), Image.ANTIALIAS)

	'''
	print(height*textInfo['paddingBorderRatio'])
	print(totalTextHeight)
	print(height*textInfo['paddingDeviceRatio'])
	'''

	devicePaddingLeft = int((width - deviceBg.size[0])/2)
	devicePaddingTop = int(round(height*textInfo['paddingBorderRatio'] + totalTextHeight + height*textInfo['paddingDeviceRatio']))
	devicePadding = (devicePaddingLeft, devicePaddingTop)

	bg.paste(deviceBg, devicePadding, mask=deviceBg)
	#print(deviceBg.format, deviceBg.size, deviceBg.mode)

	deviceScale = deviceBg.size[0]/oriDeviceSize[0]


	screenshot = Image.open(screenshot)
	screenshot.thumbnail((deviceBg.size[0]*(screenWidth/oriDeviceSize[0]), deviceBg.size[1]*(screenHeight/oriDeviceSize[1])), Image.ANTIALIAS)
	bg.paste(screenshot, (devicePaddingLeft+int(screenPaddingLeft*deviceScale), devicePaddingTop+int(screenPaddingTop*deviceScale)), mask=screenshot)
	#print(screenshot.format, screenshot.size, screenshot.mode)


	deviceFore = Image.open(deviceImagePathPrefix+"_fore.png")
	deviceFore.thumbnail((width, height), Image.ANTIALIAS)
	bg.paste(deviceFore, devicePadding, mask=deviceFore)
	#print(deviceFore.format, deviceFore.size, deviceFore.mode)


	deviceShadow = Image.open(deviceImagePathPrefix+"_shadow.png")
	deviceShadow.thumbnail((width, height), Image.ANTIALIAS)
	bg.paste(deviceShadow, devicePadding, mask=deviceShadow)
	#print(deviceShadow.format, deviceShadow.size, deviceShadow.mode)


	#bg.show()

	# http://stackoverflow.com/q/16065694/2603230
	outputBuffer = BytesIO()
	bg.save(outputBuffer, format='JPEG')
	bgBase64Data = outputBuffer.getvalue()

	# http://stackoverflow.com/q/16748083/2603230
	return 'data:image/jpeg;base64,' + base64.b64encode(bgBase64Data).decode()
