import chatbot.chatbot as chatbot
import speech_recognition as sr
from login import send_meet_message

def run(browser, threshold, mic):
    text = listen_to_meet(mic)
    msg, cat, conf = respond_to_speaker(browser, text, threshold)
    return text, msg, cat, conf

def listen_to_meet(source):
    r = sr.Recognizer()
    print("LISTEN: Listening...")
    try:
        audio = r.listen(source, timeout=3, phrase_time_limit=5)
        text = r.recognize_google(audio, language="en-US").lower()
    except:
        print("LISTEN: Nothing detected.")
        text = None
    return text

def respond_to_speaker(browser, text, threshold):
    msg = None
    category = None
    confidence = None
    print(text)
    if (text is not None) and (text != '') and (check_mic_muted(browser) == 'true'):
        msg, category, confidence = chatbot.chatbot_response(text)
        if msg != " ":
            if confidence > threshold:
                print(f"{text} -> {msg}")
                send_meet_message(browser, msg)
                f = open("chatbot/data/transcript.txt", "a")
                f.write(f"Audio: {text} -> {msg}\n\n\n")
                f.close()
            else:
                f = open("chatbot/data/unkown.txt", "a")
                write = True
                for line in open("chatbot/data/unkown.txt").readlines():
                    if (f"{text} -> {msg}") in line:
                            write = False
                if write:
                    f.write(f"{text} -> {msg}\n\n\n")
                f.close()

        else:
            f = open("chatbot/data/unkown.txt", "a")
            write = True
            for line in open("chatbot/data/unkown.txt").readlines():
                if (f"{text} -> {msg}") in line:
                    write = False
            if write:
                f.write(f"{text} -> {msg}\n\n\n")
            f.close()

    return msg, category, confidence

def check_mic_muted(browser):
    mic_xpath = "/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[1]/div/div/div"
    active = browser.find_element_by_xpath(mic_xpath).get_attribute("data-is-muted")
    return active