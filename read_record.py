import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('recording1.wav') as source:
    audio_text = r.listen(source)

    try:
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)

    except:
         print('Sorry.. run again...')