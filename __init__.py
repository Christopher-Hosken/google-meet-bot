from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import login, read, listen

opt = Options()
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications" : 1,
})

browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opt)


def main():
    login.login_google(browser)
    login.login_meet(browser, "COMSCI")
    while True:
       #listen.run(browser)
       read.run(browser)

if __name__ == '__main__':
    main()