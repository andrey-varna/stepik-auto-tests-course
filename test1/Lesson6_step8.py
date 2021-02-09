from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля в блоке, для обязательного заполнения
    # elements = browser.find_elements_by_css_selector(".first_block input") или вариант browser.find_element_by_css_selector("input[required]")
    # for element in elements:
    #     element.send_keys("ответ")


    # Код, под необходимые 3 поля
    element1 = browser.find_element_by_css_selector(".first_block .first")
    element1.send_keys("ответ")
    element2 = browser.find_element_by_css_selector(".first_block .second")
    element2.send_keys("ответ")
    element3 = browser.find_element_by_css_selector(".first_block .third")
    element3.send_keys("ответ")
    ...

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()