import requests
import uuid
import time
import base64
import json
import pprint

api_url = 'https://q93lwb0cm8.apigw.ntruss.com/custom/v1/44031/2e56f044f18c5334e14a68e185c39d326e309a555a5c4c62a52bbc9619e21e70/general'
secret_key = 'WUt2eGhhYXllUVptYnVMbkJ0Z2tDRmJ3WmxvZkRBSlA='

image_file = './sample.pdf'

with open(image_file,'rb') as f:
    file_data = f.read()

request_json = {
    'images': [
        {
            'format': 'pdf',
            'name': 'sample',
            'data': base64.b64encode(file_data).decode()
        }
    ],
    'requestId': str(uuid.uuid4()),
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000)),
    'lang': 'ko'
}

payload = json.dumps(request_json).encode('UTF-8')
headers = {
  'X-OCR-SECRET': secret_key,
  'Content-Type': 'application/json'
}

response = requests.request("POST", api_url, headers=headers, data = payload)
#print(response.text)

response_json = json.loads(response.text)
print(json.dumps(response_json, indent=2, ensure_ascii=False))

#print(json.dumps(response.text, indent=2, ensure_ascii=False))