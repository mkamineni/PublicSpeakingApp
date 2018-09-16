from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "hi"

@app.route('/analyze', methods=['GET', 'POST'])
def analyze_video():
	body = request.get_json()
	return body