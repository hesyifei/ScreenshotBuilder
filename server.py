import sys, os, time, tempfile
from flask import Flask, request, render_template, send_from_directory, url_for, jsonify
from werkzeug import secure_filename
from genImage import generateImage


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'jpeg', 'png'])

def allowed_file(filename):
	return '.' in filename and \
			filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route("/")
def homePage():
	return render_template('index.html')

@app.route('/generateImage', methods=['POST'])
def upldfile():
	if request.method == 'POST':
		print(request.form['inputText'])
		inputImage = request.files['inputImage']
		print(inputImage)
		if inputImage and allowed_file(inputImage.filename):
			millis = int(round(time.time() * 1000))
			filename = "prefix_projectName_"+str(millis)+os.path.splitext(inputImage.filename)[1]
			print('FileName: ' + filename)
			updir = os.path.join(basedir, 'static/upload/')
			inputImage.save(os.path.join(updir, filename))
			file_size = os.path.getsize(os.path.join(updir, filename))
			return jsonify(name=filename, size=file_size)


if __name__ == "__main__":
	app.run()

