from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TESTING'] = True

@app.route('/')
def hello_world():
	return "hi"

@app.route('/analyze', methods=['GET', 'POST'])
def analyze_video():
	app.logger.info(request)
	body = request.get_json()
	return {"boop":"boop"}