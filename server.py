import sys, os, time, tempfile
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

@app.route("/")
def homePage():
	return render_template('index.html', screenshots=screenshotList)

@app.route('/generateImage', methods=['POST'])
def uploadAndGenImage():
	if request.method == 'POST':
		print(request.form)

		inputPrefix = request.form['inputPrefix']
		inputText = request.form['inputText']
		print(inputPrefix)
		print(inputText)

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
			generatedImageBase64 = generateImage(inputText, fileDirWithName)
			print("got base64 of generated image")
			return jsonify(imgBase64=generatedImageBase64, oriImgFileName=filename)
			#file_size = os.path.getsize(fileDirWithName)



if __name__ == "__main__":
	app.run(debug=False)
