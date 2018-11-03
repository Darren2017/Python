from selenium import webdriver
import time
import json
import os

PASSWORD = os.getenv("WeChatPassword")
ACCOUNT = os.getenv("WeChatAccount")

def main():
    browser = webdriver.Chrome()
    browser.get('https://mp.weixin.qq.com')
    time.sleep(2)

    browser.find_element_by_name("account").clear()
    browser.find_element_by_name("account").send_keys(ACCOUNT)
    browser.find_element_by_name("password").clear()
    browser.find_element_by_name("password").send_keys(PASSWORD)
    browser.find_element_by_class_name('frm_checkbox_label').click()
    browser.find_element_by_class_name('btn_login').click()
    time.sleep(15)

    browser.get('https://mp.weixin.qq.com')
    cookies = browser.get_cookies()

    post = {}

    for cookie in cookies:
        post[cookie['name']] = cookie['value']
    cookies_json = json.dumps(post)

    with open('cookie.txt', 'w+') as f:
        f.write(cookies_json)

    browser.close()

if __name__ == '__main__':
    main()
