import sys, os, tempfile
from flask import Flask, request, render_template, send_from_directory, url_for, jsonify
from werkzeug import secure_filename
from genImage import generateImage

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
		files = request.files['inputImage']
		print(files)
		if files and allowed_file(files.filename):
			with tempfile.TemporaryDirectory() as temp_dir:
				filename = secure_filename(files.filename)
				print(filename)
				print(temp_dir)
				files.save(os.path.join(temp_dir, filename))
				file_size = os.path.getsize(os.path.join(temp_dir, filename))
				print(file_size)
				generateImage()
				return jsonify(name=filename, size=file_size)


if __name__ == "__main__":
	app.run()

