import time
from selenium.webdriver.common.keys import Keys

def login_google(browser, email, password):
    print("INIT: SIGNING IN")
    browser.get("https://medium.com/m/signin")

    google_sign_in = "/html/body/div[2]/div/div/div/div/div/div/div/div/div[3]/div[1]"
    signin = browser.find_element_by_xpath(google_sign_in)
    signin.click()

    time.sleep(2)
    email_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
    browser.find_element_by_xpath(email_xpath).send_keys(email)

    time.sleep(1)
    button_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button"
    browser.find_element_by_xpath(button_xpath).click()

    time.sleep(2)
    pass_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
    browser.find_element_by_xpath(pass_xpath).send_keys(password)

    time.sleep(1)
    button_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button"
    browser.find_element_by_xpath(button_xpath).click()

    time.sleep(5)
    browser.get("https://mail.google.com")

    print("INIT: SIGN IN COMPLETE")


def login_meet(browser, code):
    print("INIT: MEET SIGNING IN")
    browser.get("https://meet.google.com")

    time.sleep(3)
    join_xpath = "/html/body/div[1]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]"
    browser.find_element_by_xpath(join_xpath).click()

    time.sleep(1)
    code_xpath = "/html/body/div[1]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input"
    browser.find_element_by_xpath(code_xpath).send_keys(code)

    time.sleep(3)
    button_xpath = "/html/body/div[1]/div[3]/div/div[2]/span/div/div[4]/div[2]/div"
    browser.find_element_by_xpath(button_xpath).click()
    
    try:
        time.sleep(10)
        mic_xpath = "/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div/div"
        browser.find_element_by_xpath(mic_xpath).click()
    
        time.sleep(3)
        cam_xpath = "/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div"
        browser.find_element_by_xpath(cam_xpath).click()
    except:
        pass

    time.sleep(3)
    enter_xpath = "/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]"
    browser.find_element_by_xpath(enter_xpath).click()

    try:
        time.sleep(3)
        popup_xpath = "/html/body/div[1]/div[3]/div/div[2]/div[2]/div[3]/div"
        browser.find_element_by_xpath(popup_xpath).click()
    except:
        pass

    time.sleep(2)
    chat_xpath = "/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]"
    browser.find_element_by_xpath(chat_xpath).click()

    print("INIT: MEET SIGN IN COMPLETE")


def send_meet_message(browser, msg):
    text_xpath = "/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea"
    browser.find_element_by_xpath(text_xpath).send_keys(msg, Keys.ENTER)
