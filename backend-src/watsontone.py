import json
from watson_developer_cloud import ToneAnalyzerV3

# tone_analyzer = ToneAnalyzerV3(
#     version='2017-09-21',
#     iam_apikey="LpdIzZHJOOtA")

tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    username='2797f1fe-d197-49f3-ba02-db6300dc920c',
    password='LpdIzZHJOOtA',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)

text = 'Hi! I am angry'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    'application/json').get_result()
print(json.dumps(tone_analysis, indent=2))