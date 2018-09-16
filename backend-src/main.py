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
	body = request.get_json()
    output = audio_to_text(body)
	return output