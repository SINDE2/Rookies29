import os
import time
import re

WATCH_DIR = r"C:\Users\서정우\company\my_projects\python_29"
#검색할 경로 지정
regex_patterns = {
    "주민등록번호" : r"\d{6}-\d{7}",
    "이메일" : r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
}#개인정보 패턴을 미리 등록

before = set(os.listdir(WATCH_DIR))
print("디렉토리 모니터링 시작")
while True:
    time.sleep(2)
    after = set(os.listdir(WATCH_DIR))
    added_file = after - before #after와 before 파일 수 비교
    if added_file: #새 파일 감지시 파일 이름을 획득 후, 파일 이름으로 파일을 오픈함
        for file_name in added_file:
            file_path = os.path.join(WATCH_DIR,file_name)
            print(f"\n 새 파일 추가 감지 : {file_name}")
            try:
                with open(file_path,'r',encoding='utf-8') as f:
                    lines = f.readlines()

                    #개인정보 패턴 검색하는 부분
                    for i, line in enumerate(lines, start=1):
                        is_comment = line.strip().startswith(("#","//"))#주석 확인
                        for label, pattern in regex_patterns.items():
                            matches = re.findall(pattern,line)#한줄씩 읽으며 패턴에 겹치는 부분이 있는지 확인
                            if matches:
                                if is_comment:
                                    print(f"[주석 내 {label} 탐지] ({file_name}:{i}행): {matches}")
                                print(f"[{label} 탐지] ({file_name}:{i}행): {matches}")
            except Exception as e:#에러처리로 실패시 출력될 메시지 설정
                print(f" 파일 읽기 실패 : {e}")
    before = after #계속 동작하기에 마지막에 업데이트된 파일 수로 업데이트