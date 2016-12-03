#!/usr/bin/python
import sys, getopt
from genImage import generateImage

def showHintExit():
	hint = 'usage: main.py -i <inputFile> -o <outputFile> -t "<text>"\n\n' \
	'optional input:\n'\
	'text color: -c "#ffffff"\n'\
	'font size: -s 100\n'\
	'background color: -b "#000000"'
	print(hint)
	sys.exit(2)

def main(argv):
	inputFile = ""
	outputFile = ""

	text = ""
	textColor = "black"
	fontSize = 100
	backgroundColor = "white"

	try:
		opts, args = getopt.getopt(argv,"hi:o:t:c:s:b:",["ifile=","ofile=","text=","textcolor=","fontsize=","bgcolor="])
	except getopt.GetoptError:
		showHintExit()
	for opt, arg in opts:
		if opt == '-h':
			showHintExit()
		elif opt in ("-i", "--ifile"):
			inputFile = arg
		elif opt in ("-o", "--ofile"):
			outputFile = arg
		elif opt in ("-t", "--text"):
			text = arg
		elif opt in ("-c", "--textcolor"):
			textColor = arg
		elif opt in ("-b", "--bgcolor"):
			backgroundColor = arg
		elif opt in ("-s", "--fontsize"):
			try:
				fontSize = int(arg)
			except ValueError:
				showHintExit()
	if inputFile == "" or outputFile == "" or text == "":
		showHintExit()
	else:
		textInfo = {
			"text": text,
			"textColor": textColor,
			"fontSize": fontSize,
			"fontFile": "Georgia Italic.ttf",
			"paddingBorderRatio": 0.04,
			"paddingDeviceRatio": 0.04,
			"paddingEachLine": 20
		}
		generateImage(textInfo, backgroundColor, inputFile, outputFile)
		print("Saved the output image to:", outputFile)

if __name__ == "__main__":
	main(sys.argv[1:])
