import time
from selenium import webdriver
import math


link = "http://suninjuly.github.io/alert_accept.html"



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    element1 = browser.find_element_by_css_selector("[id='answer']")
    element1.send_keys(y)
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
