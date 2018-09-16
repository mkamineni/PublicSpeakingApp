from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TESTING'] = True

from transcribe import process_audio

@app.route('/')
def hello_world():
	return "hi"

@app.route('/analyze', methods=['GET','POST'])
def analyze_video():
	app.logger.info('Hello world!')
	body = request.get_json()
	print(body)
	output = ('None', 'None', 'None')
	if body and body.form and body.form.fileUrl:
		result = process_audio(body.form.fileUrl)
		if result:
			output = result
	print('OUTPUT HERE')
	return output
