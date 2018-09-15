import json
from watson_developer_cloud import ToneAnalyzerV3

def process_text(text):
	tone_analyzer = ToneAnalyzerV3(
	    version='2017-09-21',
	    username='2797f1fe-d197-49f3-ba02-db6300dc920c',
	    password='LpdIzZHJOOtA',
	    url='https://gateway.watsonplatform.net/tone-analyzer/api'
	)

	tone_analysis = tone_analyzer.tone(
		{'text': text},'application/json').get_result()
	document_tones=json.dumps(tone_analysis, indent=2)["document_tone"]["tones"]
	processed_tones=[]
	for elem in document_tones:
		tone_val=elem["tone_id"]
		score=elem["score"]
		processed_tones.append((tone_val, score))

	return processed_tones
