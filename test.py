import speech_recognition as sr
import webbrowser as wb

r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()

with sr.Microphone() as source:
    print("search for a video")
    print("speak now")
    audio=r3.listen(source)

if "video" in r2.recognize_google(audio):
    r2=sr.Recognizer()
    url="https://www.youtube.com/"
    with sr.Microphone() as source:
        print("search your query")
        audio=r2.listen(source)

        try:
            get=r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+"results?search_query="+get)

        except sr.UnknownValueError:
            print("could not understand")

        except sr.RequestError as e:
            print("failed to get result".format(e))

if "google" in r1.recognize_google(audio):
    r1 = sr.Recognizer()
    url = "https://www.google.co.in/"
    with sr.Microphone() as source:
        print("search your query")
        audio = r1.listen(source)

        try:
            get = r1.recognize_google(audio)
            print(get)
            wb.get().open_new(url + "results?search_query=" + get)

        except sr.UnknownValueError:
            print("could not understand")

        except sr.RequestError as e:
            print("failed to get result".format(e))

