#!/usr/bin/python

import sys, getopt
from genImage import generateImage

def main(argv):
	inputFile = ""
	outputFile = ""
	inputText = ""
	inputTextColor = "black"
	backgroundColor = "white"
	hint = 'usage: main.py -i <inputFile> -o <outputFile> -t "<text>"\n\n' \
	'optional input:\n'\
	'text color: -c "#ffffff"\n'\
	'background color: -b "#000000"'\

	try:
		opts, args = getopt.getopt(argv,"hi:o:t:c:b:",["ifile=","ofile=","text=","textcolor=","bgcolor="])
	except getopt.GetoptError:
		print(hint)
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print(hint)
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputFile = arg
		elif opt in ("-o", "--ofile"):
			outputFile = arg
		elif opt in ("-t", "--text"):
			inputText = arg
		elif opt in ("-c", "--textcolor"):
			inputTextColor = arg
		elif opt in ("-b", "--bgcolor"):
			backgroundColor = arg
	if inputFile == "" or outputFile == "" or inputText == "":
		print(hint)
	else:
		textInfo = {
			"text": inputText,
			"textColor": inputTextColor,
			"fontSize": 100,
			"fontFile": "Georgia Italic.ttf",
			"paddingBorderRatio": 0.04,
			"paddingDeviceRatio": 0.04,
			"paddingEachLine": 20
		}
		generateImage(textInfo, backgroundColor, inputFile, outputFile)
		print("Saved the output image to:", outputFile)

if __name__ == "__main__":
	main(sys.argv[1:])
