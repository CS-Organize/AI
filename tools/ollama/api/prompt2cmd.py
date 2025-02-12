import requests
import json
import sys
import subprocess
import aec


# 커맨드를 실행하는 함수를 추가합니다.
def execute_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"


question = input("What commands do we want to run?: ")

f = open("prompt.txt", "r")
prompt = f.read()
f.close()

url = "http://localhost:11434/api/generate"
data = {
    "model": "llama3.1",
    "prompt": 
f"""{prompt}
Question: {question}
Answer: """,
    "stream": True,
}

full_response = ""
aec.print_rainbow("printing rainbow")
print(f"Do you want to execute this command {aec.FG_WHITE}", end="")
with requests.post(url, json=data, stream=True) as response:
    for chunk in response.iter_lines():
        if chunk:
            try:
                json_data = json.loads(chunk.decode("utf-8"))
                if "response" in json_data:
                    chunk_text = json_data["response"]
                    full_response += chunk_text
                    sys.stdout.write(chunk_text)
                    sys.stdout.flush()
            except json.JSONDecodeError:
                print(
                    f"\n{aec.FG_RED}Failed to parse JSON: {chunk.decode('utf-8')}{aec.RESET}"
                )
                exit(1)

# 사용자에게 커맨드 실행 여부를 확인합니다.
user_confirmation = input(f"{aec.RESET} (y/n): ")

if user_confirmation.lower() == "y" or user_confirmation.lower() == "yes":
    result = execute_command(full_response.strip())
    print(result, end="")
else:
    print("Command execution cancelled by user.")

