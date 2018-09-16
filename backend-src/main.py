from flask import Flask, request
from flask_restful import Api
from transcribe import process_audio
app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/send', methods=['POST'])
def send_video():
	body = request.get_json()
	#may need to process body['form']
	#get audio here!!
	results_dict=process_audio(audio)
	#call function

	tokens=results_dict["tokens"]
	colors=results_dict["colors_dict"]

	pause_after_sent=results_dict["pause_after_sent"]
	pause_after_comma=results_dict["pause_after_comma"]
	words_per_min=results_dict["words_per_min"]
	tone_of_text=results_dict["tone"]

	api.get_annotated_text(tokens, colors)
	users_stats=[pause_after_sent, pause_after_comma, words_per_min, percentage_filler, filler_freqs, tone_of_text]
	ideal_stats=[2, 1, 150, 0, None, None]
	api.get_results(users_stats, ideal_stats)

	api.get_graph_data()
    return "setup is hard"

