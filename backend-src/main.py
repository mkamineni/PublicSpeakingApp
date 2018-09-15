from flask import Flask, request
from transcribe import process_audio
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/send', methods=['POST'])
def send_video():
	body = request.get_json()
	#may need to process body['form']
	#call function
    return "setup is hard"