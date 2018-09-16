from flask import Flask, request
app = Flask(__name__)

from transcribe import process_audio

@app.route('/')
def hello_world():
	return "hi"

@app.route('/analyze', methods=['GET','POST'])
def analyze_video():
	app.logger.info('Hello world!')
	body = request.get_json()
	#app.logger.info('BODY',body)
	output = ""
	if body and body.form and body.form.fileUrl:
		result = process_audio(body.form.fileUrl)
		if result:
			output = result
	app.logger.info('Bye world!')
	return output
