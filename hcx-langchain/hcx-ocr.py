import requests
import uuid
import time
import base64
import json
import pprint

from dotenv import load_dotenv
from pathlib import Path

# .env 파일 경로 명시적 로드 (기본: 현재 디렉토리)
load_dotenv(dotenv_path=Path(__file__).parent / "../.env")

HCX_OCR_API_URL = os.getenv("HCX_OCR_API_URL")
HCX_OCR_SECRET_KEY = os.getenv("HCX_OCR_SECRET_KEY")


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
  'X-OCR-SECRET': HCX_OCR_SECRET_KEY,
  'Content-Type': 'application/json'
}

response = requests.request("POST", HCX_OCR_API_URL, headers=headers, data = payload)
#print(response.text)

response_json = json.loads(response.text)
print(json.dumps(response_json, indent=2, ensure_ascii=False))

#print(json.dumps(response.text, indent=2, ensure_ascii=False))