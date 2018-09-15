import requests
from time import sleep
import analyze_tone
import analyze_pace

filler_file="filler_words.txt"
filler_words=set()
with open(filler_file, "r+") as f:	
	for line in f:
		filler_words.add(line.strip())

def process_audio(ID=None):
	response=audio_to_text(ID)
	output, portions, colors=get_text_and_fillers(response)
	tone=analyze_tone.process_text(output)
	pause_after_sent, pause_after_comma, words_per_min=analyze_pace.prcoess_response(response)

	results_dict={"string_output": output, "tokens": portions, 
				"colors_dict": colors, "tone": tone, "pause_after_sent": pause_after_sent, 
				"pause_after_comma": pause_after_comma, "words_per_min": words_per_min}
				
	return results_dict

def audio_to_text(ID):
	'''
	This function generates a dictionary representation of text from an audio file using the REV API. 
	'''
	new_headers= {
	   	'Authorization': 'Bearer 01wXudOy88gdkI2HgWeZUrc1WEp5GtFA5XK9KFNv6O7ucF6e5Nwe47CXm3cAbMAFHML56xeOQy0Ya99FFVwF7dqrzitwc',
	   	'Accept': 'application/vnd.rev.transcript.v1.0+json',
	}

	if ID==None:
		headers = {
		    'Authorization': 'Bearer 01wXudOy88gdkI2HgWeZUrc1WEp5GtFA5XK9KFNv6O7ucF6e5Nwe47CXm3cAbMAFHML56xeOQy0Ya99FFVwF7dqrzitwc',
		    'Content-Type': 'application/json',
		}

		data = '{"media_url":"https://support.rev.com/hc/en-us/article_attachments/200043975/FTC_Sample_1_-_Single.mp3","metadata":"This is a sample submit jobs option"}'

		response = requests.post('https://api.rev.ai/revspeech/v1beta/jobs', headers=headers, data=data).json()
		ID=response["id"]

		status=response["status"]
		while status!='transcribed':
			sleep(30)
			response = requests.get('https://api.rev.ai/revspeech/v1beta/jobs/'+str(ID), headers=new_headers).json()
			status=response["status"]

	response2 = requests.get('https://api.rev.ai/revspeech/v1beta/jobs/'+str(ID)+'/transcript', headers=new_headers).json()

	return response2

def get_text_and_fillers(response2):
	colors={"blue": set()}
	text_portions=[]
	output=""
	parts=response2["monologues"][0]["elements"]

	for ind in range(len(parts)):
		elem=parts[ind]
		text_portions.append(elem["value"])
		output+=elem["value"]
		if elem["value"].lower() in filler_words:
			print("F: "+elem["value"]+"\n")
			colors["blue"].add(ind)

	return output, text_portions, colors


print("OUTPUT:", "\n", "\n", "\n", str(process_audio()))