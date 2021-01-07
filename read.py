import chatbot.chatbot as chatbot
import login

def run(browser):
    user, text = read_meet(browser)
    respond_to_chat(browser, user, text)

def read_meet(browser):
    chatbox_xpath = "/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]/div[last()]"
    user_xpath = f"{chatbox_xpath}/div[1]/div[1]"
    message_xpath = f"{chatbox_xpath}/div[last()]/div[last()]"
    online_xpath = "/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[1]/div[1]/span/div/span[2]"

    try:
        chat_user = browser.find_element_by_xpath(user_xpath).text.lower()
    except:
        chat_user = None
    try:
        chat_text = browser.find_element_by_xpath(message_xpath).text.lower()
    except:
        chat_text = None
    try:
        online_users = browser.find_element_by_xpath(online_xpath).text.lower()
    except:
        online_users = None


    return chat_user, chat_text, online_users

def respond_to_chat(browser, chat_user, chat_text, online_users):
    if (chat_text is not None) and (chat_text != ''):
        if (chat_user is not None) and (chat_user != 'you'):
            print(f"User: {chat_user}")
            msg = chatbot.chatbot_response(chat_text)
            print(f"{chat_text} -> {msg}")
            login.send_meet_message(browser, msg)