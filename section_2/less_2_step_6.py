# Задание на execute_script
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):  # Посчитать математическую функцию от x
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')
    # Считать значение для переменной x
    x = browser.find_element(By.ID, 'input_value').text
    formula = calc(x)
    # Проскроллить страницу вниз.
    browser.execute_script("window.scrollBy(0, 100);")
    # Ввести ответ в текстовое поле
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(formula)
    # Отметить checkbox "I'm the robot"
    checkboxes = browser.find_element(By.ID, 'robotCheckbox')
    checkboxes.click()
    # Выбрать radiobutton "Robots rule!"
    radiobuttons = browser.find_element(By.ID, 'robotsRule')
    radiobuttons.click()
    # Нажать на кнопку Submit
    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn[type="submit"]')
    submit.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# Пустая строка