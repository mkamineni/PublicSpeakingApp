from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TESTING'] = True

from transcribe import audio_to_text

@app.route('/')
def hello_world():
	return "hi"

@app.route('/analyze', methods=['POST'])
def analyze_video():
	print('Hello world!', file=sys.stderr)
	body = request.get_json()
	print(body, file=sys.stderr)
	output = audio_to_text(body)
	print('OUTPUT HERE', file=sys.stderr)
	return output
