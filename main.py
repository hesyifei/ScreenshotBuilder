#!/usr/bin/python
import sys, argparse
from genImage import generateImage

def main(argv):
	parser = argparse.ArgumentParser(description='Generate screenshots for App Store & Google Play Store.', usage='%(prog)s [options]')
	parser.add_argument('inputFile', help='input image (screenshot) path')
	parser.add_argument('outputFile', help='path to output the generated image')
	parser.add_argument('width', type=int, help='output image width')
	parser.add_argument('height', type=int, help='output image height')
	parser.add_argument('deviceName', help='the device border on the output image')
	parser.add_argument('-do', '--deviceOrientation', choices=['port', 'land'], default='port', help='the device orientation on the output image')
	parser.add_argument('-t', '--text', default='', help='text displayed on the output image')
	parser.add_argument('-c', '--textColor', default='888888', help='color of the text displayed on the output image')
	parser.add_argument('-s', '--fontSize', type=int, default=100, help='font size of the text displayed on the output image')
	parser.add_argument('-f', '--fontFile', default='Arial.ttf', help='font of the text displayed on the output image')
	parser.add_argument('-b', '--bgColor', default='ffffff', help='the background color of the output image')
	parser.add_argument('-a', '--bgAlpha', type=int, default=100, help='the alpha of the output image')
	parser.add_argument('-ff', '--fadeFrom', type=float, default=0, help='the position (from bottom/top) for the begining of the fading (0 means no fading, >0 means fade from bottom, <0 means fade from top) (range -1 to 1)')
	parser.add_argument('-fh', '--fadeHeight', type=float, default=0.5, help='the height of fading (try yourself to see what it means)')

	args = parser.parse_args()

	inputFile = args.inputFile
	outputFile = args.outputFile

	width = args.width
	height = args.height

	deviceName = args.deviceName
	deviceOrientation = args.deviceOrientation

	text = args.text
	textColor = args.textColor
	fontSize = args.fontSize
	fontFile = args.fontFile

	backgroundColor = args.bgColor
	backgroundAlpha = args.bgAlpha

	outputFadeFrom = args.fadeFrom
	outputFadeHeight = args.fadeHeight


	textColor = "#"+textColor
	textInfo = {
		"text": text,
		"textColor": textColor,
		"fontSize": fontSize,
		"fontFile": fontFile,
		"paddingBorderRatio": 0.04,
		"paddingDeviceRatio": 0.04,
		"paddingEachLine": 20
	}
	backgroundAlpha = int(255*(backgroundAlpha/100))
	generateImage(textInfo, backgroundColor, backgroundAlpha, deviceName, deviceOrientation, width, height, outputFadeFrom, outputFadeHeight, inputFile, outputFile)
	print("Saved the output image to:", outputFile)

if __name__ == "__main__":
	main(sys.argv[1:])
