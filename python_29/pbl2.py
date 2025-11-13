import feedparser
from gtts import gTTS

# RSS 주소
feed_url = 'http://www.boannews.com/media/news_rss.xml?mkind=1'

# RSS 파싱
feed = feedparser.parse(feed_url)

# 최대 10개 뉴스만 처리
for i, entry in enumerate(feed.entries[:10], start=1):
    # 뉴스 요약 텍스트 가져오기
    text = entry.summary
    # gTTS를 이용해 음성으로 변환
    tts = gTTS(text=text, lang='ko', slow=False)
    # 파일명 지정
    output_file = f"news_summary_{i}.mp3"
    tts.save(output_file)
    print(f"{output_file} 생성 완료!")

print("모든 음성 파일이 생성되었습니다.")