from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
import keyboard
import schedule
from datetime import datetime
import requests
import sqlite3

url = "https://discordapp.com/api/webhooks/792634058017734667/6TqZaFZ--bEaXX1EuWctg0Yp-DwJxlbia7gzHTzJe-OPRbkhPvGhZ2cxrYE2e5zluuBx"


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
chromeOptions.add_experimental_option('useAutomationExtension', False)
chromeOptions.add_argument('--disable-blink-features=AutomationControlled')


chromeOptions.add_argument("--disable-infobars")
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})
service = Service("C:\\seleniumdriver\\chromedriver.exe")
browser = webdriver.Chrome(service=service, options=chromeOptions)
browser.maximize_window()
waiter = WebDriverWait(browser, 15)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def start_chrome():
    sleep(2)
    browser.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    sleep(10)
    mail = "use your mail id"
    password = "use your password"
    browser.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(mail)
    sleep(1)
    browser.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/div[2]').click()
    sleep(2)
    browser.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    sleep(2)
    browser.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/div[2]').click()


def join_class(code, duration, classname):
    browser.get('https://apps.google.com/meet/')
    browser.find_element(By.XPATH, '//*[@id="page-content"]/section[1]/div/div[1]/div[2]/div/div[2]/input').send_keys(
        code)
    sleep(3)
    browser.find_element(By.XPATH,
                         '//*[@id="page-content"]/section[1]/div/div[1]/div[2]/div/div[2]/a/button/span').click()
    sleep(5)
    keyboard.press_and_release('ctrl + d')
    sleep(5)
    keyboard.press_and_release('ctrl + e')
    sleep(5)
    browser.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div['
                                   '2]/div/div[2]/div/div[1]/div[1]/span').click()
    sleep(10)
    keyboard.press('enter')
    sleep(5)
    message = {
        'content': "joined class " + str(classname) + " at " + str(datetime.now().strftime("%H:%M:%S"))
    }
    requests.post(url, data=message)
    sleep(int(duration))
    keyboard.press('enter')
    sleep(1)
    keyboard.press('enter')
    browser.find_element(By.XPATH, '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div').click()
    sleep(4)
    message = {
        'content': "left class at " + str(datetime.now().strftime("%H:%M:%S"))
    }
    requests.post(url, data=message)
    sleep(10)


def schedule_classes():
    conn = sqlite3.connect('schedule_real.sqbpro')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM timetable")
    rows = cursor.fetchall()
    for row in rows:
        time = row[5]
        code = row[1]
        duration = row[2]
        classname = row[3]
        print(str(time) + str(code) + str(duration) + str(classname) + row[4])

        if row[4] == 'monday':
            schedule.every().monday.at(time).do(join_class, code, duration, classname)
        if row[4] == 'tuesday':
            schedule.every().tuesday.at(str(time)).do(join_class, code, duration, classname)
        if row[4] == 'wednesday':
            schedule.every().wednesday.at(str(time)).do(join_class, code, duration, classname)
        if row[4] == 'thursday':
            schedule.every().thursday.at(str(time)).do(join_class, code, duration, classname)
        if row[4] == 'friday':
            schedule.every().friday.at(str(time)).do(join_class, code, duration, classname)

    # print(schedule.run_pending())
    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == '__main__':
    start_chrome()
    sleep(2)
    schedule_classes()
