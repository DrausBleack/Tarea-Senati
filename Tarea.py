#importacion de librerias 
import speech_recognition as sr
recognizer = sr.Recognizer()

mic=sr.Microphone()
with mic as source:
    print("Di algo, por favor....")
    audio = recognizer.listen(source)
    text= recognizer.recognize_google(audio, language = 'es-ES')
print(f'Has dicho: {text}') 
