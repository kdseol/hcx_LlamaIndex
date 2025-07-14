import sys
import json
import os
from langchain_naver.chat_models import ChatClovaX
import io

from dotenv import load_dotenv
from pathlib import Path

# .env 파일 경로 명시적 로드 (기본: 현재 디렉토리)
load_dotenv(dotenv_path=Path(__file__).parent / "../.env")

# 🔐 API Key 설정 (환경변수에서 가져오기)
HCX_API_KEY = os.getenv("HCX_API_KEY")


print(f"HCX API KEY: {HCX_API_KEY}")

MODEL_NAME = "HCX-005"  # 모델 이름 (기본 모델)

if not HCX_API_KEY:
    print("에러: HCX_API_KEY 환경변수가 설정되지 않았습니다.")
    sys.exit(1)

# ChatClovaX 클래스 초기화
chat = ChatClovaX(
    model=MODEL_NAME,
    api_key='Bearer '+HCX_API_KEY,
    base_url="https://clovastudio.stream.ntruss.com/v1/openai"
)

# ✅ Python 출력 인코딩을 UTF-8로 설정 (출력 깨짐 방지)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def infer(question):
    try:
        prompt = (
            question
        )

        # 요청 메시지 구성
        messages = [
            ("system", "You are an AI model that evaluates multiple-choice questions. "),
            ("human", prompt)
        ]

        # 모델 호출 (invoke 사용)
        ai_msg = chat.invoke(messages)
        
        # 응답이 없는 경우 오류 처리
        if not ai_msg or not ai_msg.content:
            return "응답 오류: 모델에서 결과를 받지 못했습니다."
        
        result = ai_msg.content.strip()
        return result
        
    except Exception as e:
        return f"에러 발생: {e}"

if __name__ == "__main__":
    try:
        question = "CLOVA Studio가 무엇인가요?"
        # HyperCLOVA X 모델 호출
        result = infer(question)
        
        # 결과 출력
        print(result)
        
    except Exception as e:
        print(f"에러 발생: {e}")
