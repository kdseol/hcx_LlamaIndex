import os
import requests
import json
from dotenv import load_dotenv
from pathlib import Path

# .env 파일 경로 명시적 로드 (기본: 현재 디렉토리)
load_dotenv(dotenv_path=Path(__file__).parent / "../.env")

# API Key 및 Request ID 설정
HCX_API_KEY = os.getenv("HCX_API_KEY")
# 분할할 원문 텍스트
text_to_chunk = """
NAVER는 AI 기술을 활용하여 다양한 서비스 혁신을 이루고 있습니다.
예를 들어, HyperCLOVA X를 기반으로 한 CLOVA Studio는 비즈니스에 특화된 생성형 AI 서비스를 쉽게 만들 수 있도록 지원합니다.
또한, 자연어 처리, 이미지 분석, 음성 인식 등 다양한 분야의 API도 함께 제공합니다.
"""

# 요청 페이로드 구성
payload = {
    "text": text_to_chunk,
          "alpha": -100,
          "segCnt": -1,
          "postProcess": False,
          "postProcessMaxSize": 2000,
          "postProcessMinSize": 500
}

# API 요청
response = requests.post(
    "https://clovastudio.stream.ntruss.com/testapp/v1/api-tools/segmentation",  # 문단 나누기 API 엔드포인트
    headers={
        "Authorization": f"Bearer {HCX_API_KEY}",
        "Content-Type": "application/json"
    },
    json=payload
)

# 결과 출력
if response.status_code == 200:
    result = response.json()
    print("📄 분할 결과:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
else:
    print("❌ 요청 실패:", response.status_code, response.text)
