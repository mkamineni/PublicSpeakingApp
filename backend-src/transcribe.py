import requests
from time import sleep
import urllib.request

import analyze_tone
import analyze_pace
from track_eyes import evaluate_focus
from image_analysis import process_video


filler_file="filler_words.txt"
filler_words=set()
with open(filler_file, "r+") as f:	
    for line in f:
        filler_words.add(line.strip())

def process_audio(url, ID=None):
    response=audio_to_text(ID, url)
    output, tokens, colors, filler_freqs=get_text_and_fillers(response)
    tone_of_text=analyze_tone.process_text(output)
    pause_after_sent, pause_after_comma, words_per_min, time_length=analyze_pace.process_response(response)

    rsp = urllib.request.urlopen(url)
    with open("video.mov",'wb') as f:
        f.write(rsp.read())
    off_center_counter=evaluate_focus("video.mov")
    average_focus=None
    if off_center_counter != 0:
        average_focus=time_length/off_center_counter

    percentage_filler=sum(filler_freqs[freq] for freq in filler_freqs)/len(tokens)
    users_stats=[pause_after_sent, pause_after_comma, words_per_min, percentage_filler, filler_freqs, average_focus, tone_of_text]
    ideal_stats=[2, 1, 150, 0, None, None, None]

    smile, datasets=process_video(url)

    data={}
    for tone in datasets:
        new_set=[]
        for point in datasets[tone]:
            new_set.append({"x":point[0], "y": point[1]})
        data[tone]=new_set

    return ((tokens, colors), (users_stats, ideal_stats), (data, smile))

def audio_to_text(ID, media_url):
    '''
    This function generates a dictionary representation of text from an audio file using the REV API. 
    '''
    new_headers= {
           'Authorization': 'Bearer 01ZJp2tTdA-vwurB-UELOdE8BVF5VuDgOyzjbQD0AjNFNZdHCd8EWPPN5bSt-wKUAGEaZcvgzI4fZke9hyX-6ZBPN4aQg',
           'Accept': 'application/vnd.rev.transcript.v1.0+json',
    }

    if ID==None:
        headers = {
            'Authorization': 'Bearer 01ZJp2tTdA-vwurB-UELOdE8BVF5VuDgOyzjbQD0AjNFNZdHCd8EWPPN5bSt-wKUAGEaZcvgzI4fZke9hyX-6ZBPN4aQg'
        }

        url = "https://api.rev.ai/revspeech/v1beta/jobs"
        payload = {'media_url': media_url,
            'metadata': "Test"}
        response = requests.post(url, headers=headers, json=payload)

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
            if word not in filler_freqs:
                filler_freqs[word]=0
            filler_freqs[word]+=1
            colors["blue"].add(ind)

    return output, text_portions, colors, filler_freqs


url = "https://support.rev.com/hc/en-us/article_attachments/200043975/FTC_Sample_1_-_Single.mp3"
print("OUTPUT:", "\n", "\n", "\n", str(process_audio(url)))