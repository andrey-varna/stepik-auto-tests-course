import time
from selenium import webdriver
import math

link = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    element1 = browser.find_element_by_css_selector("[id='answer'] ")
    element1.send_keys(y)
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()
