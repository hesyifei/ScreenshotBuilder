import sys, os, re, time, tempfile
from flask import Flask, request, render_template, send_from_directory, url_for, jsonify
from werkzeug import secure_filename
from genImage import generateImage


basedir = os.path.abspath(os.path.dirname(__file__))

screenshotList = ["tst", "haa"]

app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'jpeg', 'png'])

def allowed_file(filename):
	return '.' in filename and \
			filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']



# ERROR HANDLING
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response



@app.route("/")
def homePage():
	return render_template('index.html', screenshots=screenshotList)

@app.route('/generateImage', methods=['POST'])
def uploadAndGenImage():
	if request.method == 'POST':
		print(request.form)

		inputPrefix = request.form['inputPrefix']
		inputText = request.form['inputText']
		inputBgColor = request.form['inputBgColor']
		print(inputPrefix)
		print(inputText)
		print(inputBgColor)

		if not re.match("^[a-zA-Z0-9_]{6,20}$", inputPrefix):
			raise InvalidUsage('inputPrefix is not not acceptable.', status_code=406)
		if not re.match("^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", inputBgColor):
			raise InvalidUsage('inputBgColor is not not acceptable.', status_code=406)


		filename = "image_"+inputPrefix+".png"
		print('FileName: ' + filename)
		fileDir = os.path.join(basedir, 'static/upload/')
		fileDirWithName = os.path.join(fileDir, filename)
		print('FileName: ' + fileDirWithName)


		# use request.files.get() as it is optional
		inputImage = request.files.get('inputImage')
		print(inputImage)
		if inputImage and allowed_file(inputImage.filename):
			print("Have new screenshot")
			inputImage.save(fileDirWithName)


		if os.path.isfile(fileDirWithName):
			generatedImageBase64 = generateImage(inputText, inputBgColor, fileDirWithName)
			print("got base64 of generated image")
			return jsonify(imgBase64=generatedImageBase64, oriImgFileName=filename)
			#file_size = os.path.getsize(fileDirWithName)
		else:
			raise InvalidUsage('Screenshot image cannot be found.', status_code=406)



if __name__ == "__main__":
	app.run(debug=False)
