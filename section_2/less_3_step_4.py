# Задание: принимаем alert
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):  # Посчитать математическую функцию от x
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    # Нажать на кнопку
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    # Принять confirm
    browser.switch_to.alert.accept()
    # Считать значение для переменной x
    x = browser.find_element(By.ID, 'input_value').text
    fomula = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(fomula)
    # Нажать на кнопку Submit
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла