from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Ждем когда цена в окне станет равна 100 и нажимаем кнопку "book"
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100")
                                              ), browser.find_element_by_id("book").click()
    # находим переменный элемент "х" и считаем по формуле def
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    option = browser.find_element_by_css_selector("[id='answer']")
    option.send_keys(y)
    # скролим вниз до появления кнопки "submit" и нажимаем ее
    button1 = browser.find_element_by_xpath("//button[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()

finally:
    time.sleep(5)
    browser.quit()
