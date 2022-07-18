import requests
endpoint = "https://api.assemblyai.com/v2/transcript/YOUR-TRANSCRIPT-ID-HERE"
headers = {
    "authorization": "YOUR-API-TOKEN",
}
response = requests.get(endpoint, headers=headers)
print(response.json())