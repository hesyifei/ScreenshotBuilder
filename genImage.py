import base64
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from configparser import ConfigParser

def generateImage(textInfo, inputBgColor, deviceName, deviceOrientation, outputWidth, outputHeight, inputImageDir, outputImageDir):
	width, height = (outputWidth, outputHeight)
	backgroundColor = inputBgColor
	screenshot = inputImageDir

	config = ConfigParser()
	config.read("device_image/"+deviceName+"/data.ini")

	screenWidth = config.getint(deviceOrientation, 'screenWidth')
	screenHeight = config.getint(deviceOrientation, 'screenHeight')
	screenPaddingLeft = config.getint(deviceOrientation, 'screenPaddingLeft')
	screenPaddingTop = config.getint(deviceOrientation, 'screenPaddingTop')


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
	bg.paste(screenshot, (devicePaddingLeft+int(screenPaddingLeft*deviceScale), devicePaddingTop+int(screenPaddingTop*deviceScale)))
	#print(screenshot.format, screenshot.size, screenshot.mode)


	deviceFore = Image.open(deviceImagePathPrefix+"_fore.png")
	deviceFore.thumbnail((width, height), Image.ANTIALIAS)
	bg.paste(deviceFore, devicePadding, mask=deviceFore)
	#print(deviceFore.format, deviceFore.size, deviceFore.mode)


	deviceShadow = Image.open(deviceImagePathPrefix+"_shadow.png")
	deviceShadow.thumbnail((width, height), Image.ANTIALIAS)
	bg.paste(deviceShadow, devicePadding, mask=deviceShadow)
	#print(deviceShadow.format, deviceShadow.size, deviceShadow.mode)


	bg.save(outputImageDir)
	bg.show()

