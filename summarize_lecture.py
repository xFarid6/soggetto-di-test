'''
Step 1 — Libraries
Step 2 — Lecture Audio Data
Step 3 — Speech to Text with Auto Summary
Final Step — Checking the Results
'''

import sys
import time
import requests


# import the audio data
audio_data = r"C:\Users\gioma\Downloads\Materiali moodle imprenditorialità\2 - fare impresa oggi.mp4"

# write a function to read this audio recording
def read_audio(audio_data, chunk_size=5242880):
    with open(audio_data, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data


# post request our audio data into the cloud using our API key
headers = {
    "authorization": "e15ee70dddea42458b580542e7230dac"
 }
response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers, data=read_audio(audio_data))
print(response.json()) # {'upload_url': 'https://api.assemblyai.com/v2/upload/...'}


# The first variable defines the API model we are planning to use.
speech_to_text_api = "https://api.assemblyai.com/v2/transcript"

#The second variable is a dictionary. 
# It contains two keys-values: the audio_url and the auto_chapters. 
# To turn on the auto-summary feature when getting the speech-to-text results, 
# we must add the auto_chaptersboolean key with the value of TRUE.
data = {
    "audio_url": response.json()['upload_url'],
    "auto_chapters": "TRUE",
    "language": "it"
}

# The third variable is also a dictionary. 
# It contains our API key and the content type.
headers = {
    "authorization": "e15ee70dddea42458b580542e7230dac",
    "content-type": "application/json"
}

# And lastly, we have a post request to combine all the variables into it and send it 
# to the API. The response will be reserved in the response variable.
response = requests.post(speech_to_text_api, json=data, headers=headers)

print(response.json())

# let’s copy the ID value from this response. 
# This ID value is the request-id of the request we just submitted. 
# We will need to check the request’s status and pull the results.
request_id = response.json()['id']


# final step, we are going to call back our request and then analyze the result.
# First, we are defining the request URL variable. It’s the API URL followed by the request-id.
request_url = "https://api.assemblyai.com/v2/transcript/" + request_id
# Secondly, we are just defining the API key.
headers = {
    "authorization": "e15ee70dddea42458b580542e7230dac"
}

# Thirdly, we call a get function to receive the results into our local machine.
response = requests.get(request_url, headers=headers)

# The response variable contains many attributes; 
# that’s why we are filtering out the chapters section.
auto_summary_report = response.json()['chapters']

# And lastly, we are calling the variable to see the auto-summary report.
print(auto_summary_report)