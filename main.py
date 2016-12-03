#!/usr/bin/python
import sys, getopt
from genImage import generateImage

def showHintExit():
	hint = 'usage: main.py -i <inputFile> -o <outputFile> -n "<device_name>" -d "<port/land>"\n\n' \
	'optional input:\n'\
	'text: -t "<text>"\n'\
	'text color: -c "ffffff"\n'\
	'font size: -s 100\n'\
	'font file: -f "Arial.ttf"\n'\
	'background color: -b "000000"'
	print(hint)
	sys.exit(2)

def main(argv):
	inputFile = ""
	outputFile = ""

	deviceName = ""
	deviceOrientation = ""

	text = ""
	textColor = "000000"
	fontSize = 100
	fontFile = "Arial.ttf"
	backgroundColor = "ffffff"

	try:
		opts, args = getopt.getopt(argv, "i:o:n:d:t:c:s:f:b:", ["ifile=","ofile=","device=","deviceori=","text=","textcolor=","fontsize=","fontfile=","bgcolor="])
	except getopt.GetoptError:
		showHintExit()
	for opt, arg in opts:
		if opt in ("-i", "--ifile"):
			inputFile = arg
		elif opt in ("-o", "--ofile"):
			outputFile = arg
		elif opt in ("-n", "--device"):
			deviceName = arg
		elif opt in ("-d", "--deviceori"):
			deviceOrientation = arg
		elif opt in ("-t", "--text"):
			text = arg
		elif opt in ("-c", "--textcolor"):
			textColor = arg
		elif opt in ("-s", "--fontsize"):
			try:
				fontSize = int(arg)
			except ValueError:
				showHintExit()
		elif opt in ("-f", "--fontfile"):
			fontFile = arg
		elif opt in ("-b", "--bgcolor"):
			backgroundColor = arg
	if inputFile == "" or outputFile == "" or deviceName == "" or deviceOrientation == "":
		showHintExit()
	else:
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
		generateImage(textInfo, backgroundColor, deviceName, deviceOrientation, 1080, 1920, inputFile, outputFile)
		print("Saved the output image to:", outputFile)

if __name__ == "__main__":
	main(sys.argv[1:])
