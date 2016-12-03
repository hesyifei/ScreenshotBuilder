# Screenshot Builder
A Python-based tool that helps you generate screenshots for App Store &amp; Google Play Store!

Still developing... (Developed with Python 3)

Main file: `main.py`

Example usage:

```
./main.py ~/Downloads/input.png ~/Downloads/output.png 1020 1920 "example_device" -do "land" -t "Hello world!" -c "00FF00" -s 75 -f "Times New Roman.ttf" -b "FF0000" -a 50
```

---

Detail usage: (`./main.py -h`)


```
usage: main.py [options]

Generate screenshots for App Store & Google Play Store.

positional arguments:
  inputFile             input image (screenshot) path
  outputFile            path to output the generated image
  width                 output image width
  height                output image height
  deviceName            the device border on the output image

optional arguments:
  -h, --help            show this help message and exit
  -do {port,land}, --deviceOrientation {port,land}
                        the device orientation on the output image
  -t TEXT, --text TEXT  text displayed on the output image
  -c TEXTCOLOR, --textColor TEXTCOLOR
                        color of the text displayed on the output image
  -s FONTSIZE, --fontSize FONTSIZE
                        font size of the text displayed on the output image
  -f FONTFILE, --fontFile FONTFILE
                        font of the text displayed on the output image
  -b BGCOLOR, --bgColor BGCOLOR
                        the background color of the output image
  -a BGALPHA, --bgAlpha BGALPHA
                        the alpha of the output image
```
