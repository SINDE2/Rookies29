from deep_translator import GoogleTranslator

input_text = input("번역할 한글을 입력하세요. :")
translated = GoogleTranslator(source = 'ko', target ='en').translate(input_text)
print("번역된 내용: ",translated)
