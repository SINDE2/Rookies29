from flask import Flask, render_template, request, redirect, url_for
from ftplib import FTP   # 파이썬 표준 라이브러리: FTP 프로토콜 제어

app = Flask(__name__)

# 전역 변수(Global)로 FTP 연결 객체와 로그인 정보 보관
ftp = None  # 현재 접속 중인 FTP 객체를 저장할 변수
ftp_info = {"host": "", "user": "", "password": ""}

# 1) 로그인 페이지
#    - 사용자가 FTP 서버 IP, ID, 비밀번호를 입력하는 화면
#    - GET 요청일 때만 사용
@app.route("/")
def login_page():
    # templates 폴더 안의 login.html 파일을 렌더링해서 반환
    return render_template("login.html")

# 2) 로그인 처리
#    - 사용자가 form에서 입력한 정보로 FTP 서버에 접속
#    - 접속 성공 시 /index 페이지로 리다이렉트
#    - 실패 시 에러 메시지 출력
@app.route("/login", methods=["POST"])
def login():
    global ftp, ftp_info  # 함수 안에서 전역 변수 수정하겠다고 선언

    # HTML 폼에서 넘어온 값 읽기 (name 속성 기준)
    host = request.form.get("host")      # FTP 서버 주소 (IP 또는 도메인)
    user = request.form.get("user")      # FTP 계정 ID
    password = request.form.get("password")  # FTP 계정 비밀번호

    # 입력받은 값 전역 dict에 저장
    ftp_info["host"] = host
    ftp_info["user"] = user
    ftp_info["password"] = password

    try:
        # FTP 객체 생성 및 서버 접속
        ftp = FTP(host)  # FTP(host) 호출 시 해당 host로 TCP 연결
        # 로그인 시도 (user / passwd 인자 이름 주의)
        ftp.login(user=user, passwd=password)

        # 로그인 성공하면 파일 목록 페이지로 보내기
        return redirect(url_for("index"))

    except Exception as e:
        # 예외 발생(접속 실패, 로그인 실패 등) 시 에러 메시지 문자열 반환
        # 실제로는 다시 로그인 페이지를 보여주면서 에러를 같이 표시하는 것이 더 좋음
        return f"로그인 실패: {str(e)}"


# 3) 파일 목록 페이지
#    - 로그인 성공 후에만 접근 (ftp 객체가 존재해야 함)
#    - FTP 서버의 현재 디렉터리 파일 목록을 가져와서 출력
@app.route("/index")
def index():
    global ftp  # 전역에 있는 ftp 객체 사용

    # 만약 ftp 객체가 없으면 (로그인 안 한 상태) 로그인 페이지로 돌려보내기
    if ftp is None:
        return redirect(url_for("login_page"))

    try:
        # ftp.nlst() : 현재 디렉터리의 파일 및 디렉터리 이름 목록을 리스트로 반환
        files = ftp.nlst()

        # index.html 템플릿에 files 리스트를 넘겨서 렌더링
        return render_template("index.html", files=files)

    except Exception as e:
        # 파일 목록을 가져오는 과정에서 에러가 발생했을 경우
        return f"파일 목록 불러오기 실패: {str(e)}"

if __name__ == "__main__":
    # debug=True : 코드 변경 시 자동 리로드 / 에러 페이지 디버그 정보 제공
    app.run(debug=True)
