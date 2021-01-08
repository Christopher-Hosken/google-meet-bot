import chatbot.chatbot as chatbot
import speech_recognition as sr
from login import send_meet_message

def run(browser):
    text = listen_to_meet()
    msg = respond_to_speaker(browser, text)
    return text, msg

def listen_to_meet():
    print("LISTEN: Listening...")
    r = sr.Recognizer()
    with sr.Microphone(0) as source:
        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=5)
            text = r.recognize_google(audio, language="en-US").lower()
        except:
            print("LISTEN: Nothing detected.")
            text = None
        return text

def respond_to_speaker(browser, text):
    msg = None
    print(text)
    if (text is not None) and (text != '') and (check_mic_muted(browser) == 'true'):
        msg = chatbot.chatbot_response(text)
        print(f"{text} -> {msg}")
        send_meet_message(browser, msg)
    return msg
    

def check_mic_muted(browser):
    mic_xpath = "/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[10]/div[2]/div[1]/div[1]/div/div"
    active = browser.find_element_by_xpath(mic_xpath).get_attribute("data-is-muted")
    return active