import requests
import json
import sys
import sqlite3
from datetime import datetime

# SQLite에 datetime 객체를 저장할 때 사용할 함수를 정의합니다.
def adapt_datetime(ts):
    # datetime 객체를 ISO 형식의 문자열로 변환합니다.
    return ts.isoformat()

# SQLite에 datetime 객체를 저장할 때 위에서 정의한 함수를 사용하도록 등록합니다.
sqlite3.register_adapter(datetime, adapt_datetime)

# 'chat_history.db'라는 이름의 SQLite 데이터베이스에 연결합니다.
conn = sqlite3.connect('chat_history.db')
# 데이터베이스 작업을 수행할 커서를 생성합니다.
cursor = conn.cursor()

# conversations 테이블이 없으면 새로 생성합니다.
# id INTEGER PRIMARY KEY AUTOINCREMENT : 자동으로 증가하는 고유 ID
# role TEXT : 메시지 작성자의 역할 (human 또는 ai)  
# content TEXT : 메시지 내용
# timestamp TEXT :  메시지가 작성된 시간
cursor.execute('''
CREATE TABLE IF NOT EXISTS conversations
(id INTEGER PRIMARY KEY AUTOINCREMENT,
 role TEXT,
 content TEXT,
 timestamp TEXT)
''')
# 변경사항을 데이터베이스에 저장합니다.
conn.commit()

# 새로운 메시지를 데이터베이스에 저장하는 함수
def save_message(role, content):
    # SQL 쿼리를 실행하여 메시지를 저장합니다.
    cursor.execute('INSERT INTO conversations (role, content, timestamp) VALUES (?, ?, ?)', (role, content, datetime.now().isoformat()))
    # 변경사항을 데이터베이스에 저장합니다.
    conn.commit()

# 최근 대화 내용을 가져오는 함수
def get_chat_history():
    # 최근 10개의 대화를 시간 역순으로 가져옵니다.
    cursor.execute('SELECT role, content FROM conversations ORDER BY timestamp DESC LIMIT 10')
    # 결과를 리스트로 가져와 역순으로 반환합니다 (시간 순서대로).
    return cursor.fetchall()[::-1]

# 대화 내용을 문자열 형식으로 포맷하는 함수
def format_history(history):
    # 각 대화를 "역할: 내용" 형식으로 변환하고 줄바꿈으로 연결합니다.
    return "\n".join([f"{role}: {content}" for role, content in history])

# 무한 루프를 시작하여 계속해서 사용자 입력을 받습니다.
while True:
    # 사용자에게 질문을 입력받습니다.
    prompt = input("What is your question? (Type 'exit' to quit): ")
    # 'exit'를 입력하면 프로그램을 종료합니다.
    if prompt.lower() == 'exit':
        break

    # 사용자의 질문을 데이터베이스에 저장합니다.
    save_message('human', prompt)
    
    # 최근 대화 내용을 가져옵니다.
    history = get_chat_history()
    # 대화 내용을 문자열로 포맷합니다.
    context = format_history(history)

    # Ollama API의 URL을 지정합니다.
    url = "http://localhost:11434/api/generate"
    # API 요청에 필요한 데이터를 준비합니다.
    data = {
        "model": "llama3.1",  # 사용할 AI 모델
        "prompt": f"{context}\nHuman: {prompt}\nAI:",  # 컨텍스트와 현재 질문을 포함한 프롬프트
        "stream": True  # 스트리밍 모드 활성화
    }

    # AI의 응답을 저장할 변수를 초기화합니다.
    full_response = ""
    # API에 POST 요청을 보냅니다.
    with requests.post(url, json=data, stream=True) as response:
        # 응답을 줄 단위로 반복합니다.
        for chunk in response.iter_lines():
            if chunk:
                try:
                    # 바이트 문자열을 JSON으로 파싱합니다.
                    json_data = json.loads(chunk.decode('utf-8'))
                    if 'response' in json_data:
                        # AI의 응답을 가져와 출력하고 저장합니다.
                        chunk_text = json_data['response']
                        full_response += chunk_text
                        sys.stdout.write(chunk_text)
                        sys.stdout.flush()
                    if json_data.get('done', False):
                        # 응답이 완료되면 줄바꿈을 출력합니다.
                        print()
                except json.JSONDecodeError:
                    # JSON 파싱에 실패하면 에러 메시지를 출력합니다.
                    print(f"\nFailed to parse JSON: {chunk.decode('utf-8')}")

    # AI의 전체 응답을 데이터베이스에 저장합니다.
    save_message('ai', full_response)
    # 대화 구분을 위해 빈 줄을 출력합니다.
    print("\n")

# 데이터베이스 연결을 닫습니다.
conn.close()
