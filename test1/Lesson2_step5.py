import time
from selenium import webdriver
import os
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("abv@stepik.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "Stepik_test.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:

    time.sleep(5)
    browser.quit()

