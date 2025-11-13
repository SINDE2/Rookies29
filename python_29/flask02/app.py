import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

#한글 폰트 등록 (윈도우 기준 맑은 고딕)
pdfmetrics.registerFont(
    TTFont('MalgunGothic', r'C:\Windows\Fonts\malgun.ttf')
)


app = Flask(__name__)

# 수료증 파일 저장 폴더
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CERT_DIR = os.path.join(BASE_DIR, "certificates")
os.makedirs(CERT_DIR, exist_ok=True)


@app.route("/", methods=["GET"])
def form_page():
    # 이름, 과정, 날짜 입력 받는 페이지
    return render_template("form.html")


@app.route("/generate", methods=["POST"])
def generate_certificate():
    name = request.form.get("name")
    course = request.form.get("course")
    date = request.form.get("date")  # 2025-11-13 이런 형식

    if not (name and course and date):
        return "모든 항목을 입력하세요.", 400

    # 파일 이름(한글/공백 문제 방지를 위해 간단히 처리)
    safe_name = name.replace(" ", "_")
    safe_course = course.replace(" ", "_")
    safe_date = date.replace("-", "")
    base_filename = f"{safe_name}_{safe_course}_{safe_date}"

    docx_filename = f"{base_filename}.docx"
    pdf_filename = f"{base_filename}.pdf"

    docx_path = os.path.join(CERT_DIR, docx_filename)
    pdf_path = os.path.join(CERT_DIR, pdf_filename)

    # 1) DOCX 수료증 생성
    create_docx_certificate(docx_path, name, course, date)

    # 2) PDF 수료증 생성
    create_pdf_certificate(pdf_path, name, course, date)

    # 결과 페이지로 이동 (PDF 다운로드 링크 안내)
    return render_template(
        "result.html",
        name=name,
        course=course,
        date=date,
        pdf_filename=pdf_filename,
        docx_filename=docx_filename,
    )


@app.route("/download/pdf/<filename>")
def download_pdf(filename):
    # PDF 파일 다운로드
    return send_from_directory(
        CERT_DIR,
        filename,
        as_attachment=True,
        mimetype="application/pdf"
    )


@app.route("/download/docx/<filename>")
def download_docx(filename):
    # DOCX 파일 다운로드 (옵션)
    return send_from_directory(
        CERT_DIR,
        filename,
        as_attachment=True,
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )


def create_docx_certificate(path, name, course, date):
    """python-docx로 수료증 docx 생성"""
    document = Document()

    document.add_heading("수 료 증", level=0)

    p = document.add_paragraph()
    p.add_run(f"{name} 님은 ").bold = True
    p.add_run(f"『{course}』 과정을 성실히 이수하였음을 확인합니다.\n")

    document.add_paragraph("")
    document.add_paragraph(f"수료일자: {date}")
    document.add_paragraph("기관명: ○○교육센터")

    document.add_paragraph("")
    document.add_paragraph("위와 같이 수료증을 발급합니다.")

    document.save(path)


def create_pdf_certificate(path, name, course, date):
    """reportlab으로 수료증 pdf 생성 (한글 폰트 사용)"""
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4

    # 제목
    c.setFont("MalgunGothic", 28)
    c.drawCentredString(width / 2, height - 120, "수 료 증")

    # 본문
    c.setFont("MalgunGothic", 14)
    text_y = height - 200
    c.drawString(80, text_y, f"성    명 : {name}")
    text_y -= 30
    c.drawString(80, text_y, f"과    정 : {course}")
    text_y -= 30
    c.drawString(80, text_y, f"수료일자 : {date}")

    text_y -= 50
    c.setFont("MalgunGothic", 12)
    c.drawString(
        80,
        text_y,
        "위 사람은 위 과정을 성실히 이수하였으므로 이 수료증을 수여합니다."
    )

    text_y -= 80
    c.setFont("MalgunGothic", 14)
    c.drawRightString(width - 80, text_y, "○○교육센터장  (인)")

    c.showPage()
    c.save()



if __name__ == "__main__":
    app.run(debug=True)
