import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://www.malware-traffic-analysis.net/2023/index.html"

header_info = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}
r = requests.get(url, headers=header_info, verify=False)
soup = BeautifulSoup(r.text, 'html.parser')

# 강사님 코드에서 이 부분만 수정
# 날짜/제목 링크가 다 li 안의 a 태그라 이 정도로 충분
tags = soup.select("ul li a")

results = []

# 이 페이지는 li 하나에 a가 두 개(날짜, 제목)라서
# "제목" 링크만 쓰고 싶으면 2개 중 두 번째만 쓰면 됨
for i, tag in enumerate(tags):
    # 짝수/홀수로 걸러도 되고, 텍스트에 " - " 들어간 것만 골라도 됨
    text = tag.get_text(strip=True)
    if " - " not in text:
        continue  # 제목이 아닌 건 스킵 (예: 순수 날짜)

    link_text = text
    link_href = urljoin(url, tag.get("href"))  # 전체 URL로 변환

    results.append(f"{link_text}\n{link_href}\n")

# 파일 저장
with open('malwares.txt', 'w', encoding='utf-8') as file:
    for result in results:
        file.write(result)

print(f"총 {len(results)}개를 malwares.txt 에 저장 완료")
