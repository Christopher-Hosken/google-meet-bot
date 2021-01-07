import chatbot.chatbot as chatbot
import speech_recognition as sr
import login

def run(browser):
    text = listen_to_meet()
    respond_to_speaker(browser, text)

def listen_to_meet():
    mic_index = 0
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if name == "default":
            mic_index = index
    print("LISTEN: Listening...")
    r = sr.Recognizer()
    with sr.Microphone(mic_index) as source:
        try:
            r.energy_threshold = 1500
            audio = r.listen(source, timeout=3, phrase_time_limit=5)
            text = r.recognize_google(audio, language="en-US").lower()
        except:
            print("LISTEN: Nothing detected.")
            text = None
        return text

def respond_to_speaker(browser, text):
    print(text)
    if (text is not None) and (text != ''):
        msg = chatbot.chatbot_response(text)
        print(f"{text} -> {msg}")
        login.send_meet_message(browser, msg)

while True:
    text = listen_to_meet()
    print(text)
