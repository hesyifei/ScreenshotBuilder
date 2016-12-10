# Screenshot Builder
A Python-based tool that helps you generate screenshots for App Store &amp; Google Play Store!

Still developing... (Developed with Python 3)

Main file: `main.py`

Example usage:

```
./main.py ~/Downloads/input.png ~/Downloads/output.png 1020 1920 "example_device" -do "land" -t "Hello world!" -c "00FF00" -s 75 -f "Times New Roman.ttf" -b "FF0000" -a 100 -ff 0.3 -fh 0.2
```

##Demo

Input:

<img src="https://github.com/eflyjason/ScreenshotBuilder/raw/master/demo/input.png" width="200px">

Command:

```
./main.py ./demo/input.png ./demo/output.png 1020 1920 "nexus_6p" -t "Hello world" -f "Avenir Next Condensed.ttc"
```

Output:

<img src="https://github.com/eflyjason/ScreenshotBuilder/raw/master/demo/output.png" width="200px">

##Detail usage 

`./main.py -h`


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
  -ff FADEFROM, --fadeFrom FADEFROM
                        the position (from bottom/top) for the begining of the
                        fading (0 means no fading, >0 means fade from bottom,
                        <0 means fade from top) (range -1 to 1)
  -fh FADEHEIGHT, --fadeHeight FADEHEIGHT
                        the height of fading (try yourself to see what it
                        means)
```
