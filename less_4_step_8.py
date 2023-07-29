# Задание: ждем нужный текст на странице
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # Модуль Явных Ожиданий: Ожидаемые Условия

def calc(x):  # Посчитать математическую функцию от x
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)  # Неявное ожидание

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    # Нажать на кнопку "Book"
    browser.find_element(By.ID, 'book').click()
    # Считать значение для переменной x
    x = browser.find_element(By.ID, 'input_value').text
    formula = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(formula)
    # Нажать на кнопку Submit
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# Пустая строка