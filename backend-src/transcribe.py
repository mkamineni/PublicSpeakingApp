import requests
from time import sleep
import analyze_tone
import analyze_pace

filler_file="filler_words.txt"
filler_words=set()
with open(filler_file, "r+") as f:	
	for line in f:
		filler_words.add(line.strip())

def process_audio(file, ID=None):
	response=audio_to_text(ID, file)
	output, portions, colors, filler_freqs=get_text_and_fillers(response)
	tone=analyze_tone.process_text(output)
	pause_after_sent, pause_after_comma, words_per_min=analyze_pace.process_response(response)

	results_dict={"string_output": output, "tokens": portions, 
				"colors_dict": colors, "filler_freqs": filler_freqs, "tone": tone, 
				"pause_after_sent": pause_after_sent, "pause_after_comma": pause_after_comma, "words_per_min": words_per_min}

	return results_dict

def audio_to_text(ID, file):
	'''
	This function generates a dictionary representation of text from an audio file using the REV API. 
	'''
	new_headers= {
	   	'Authorization': 'Bearer 01wXudOy88gdkI2HgWeZUrc1WEp5GtFA5XK9KFNv6O7ucF6e5Nwe47CXm3cAbMAFHML56xeOQy0Ya99FFVwF7dqrzitwc',
	   	'Accept': 'application/vnd.rev.transcript.v1.0+json',
	}

	if ID==None:
		headers = {
		    'Authorization': 'Bearer 01wXudOy88gdkI2HgWeZUrc1WEp5GtFA5XK9KFNv6O7ucF6e5Nwe47CXm3cAbMAFHML56xeOQy0Ya99FFVwF7dqrzitwc'
		}

		url = "https://api.rev.ai/revspeech/v1beta/jobs"
		files = { 'media': (file, open(file, 'rb'), 'audio/mp3') }
		response = requests.post(url, headers=headers, files=files)
		if response.status_code != 200:
		    raise Exception

		#data = '{"media_url":"https://support.rev.com/hc/en-us/article_attachments/200043975/FTC_Sample_1_-_Single.mp3","metadata":"This is a sample submit jobs option"}'
		#response = requests.post('https://api.rev.ai/revspeech/v1beta/jobs', headers=headers, data=data).json()

		#response = requests.post('https://api.rev.ai/revspeech/v1beta/jobs', headers=headers, files=files).json()
		response=response.json()
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
	filler_freqs={}
	text_portions=[]
	output=""
	parts=response2["monologues"][0]["elements"]

	for ind in range(len(parts)):
		elem=parts[ind]
		text_portions.append(elem["value"])
		output+=elem["value"]

		word=elem["value"].lower()
		if word in filler_words:
			print("F: "+elem["value"]+"\n")
			if word not in filler_freqs:
				filler_freqs[word]=0
			filler_freqs[word]+=1
			colors["blue"].add(ind)

	print("OUT:", output, "\n")

	return output, text_portions, colors, filler_freqs


file="another_one.mp3"
print("OUTPUT:", "\n", "\n", "\n", str(process_audio(file)))