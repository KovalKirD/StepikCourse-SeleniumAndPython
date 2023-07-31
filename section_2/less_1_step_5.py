# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://suninjuly.github.io/math.html'

def calc(x):  # Посчитать математическую функцию от x
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Считать значение для переменной x
    x = browser.find_element(By.ID, 'input_value').text
    fomula = calc(x)
    # Ввести ответ в текстовое поле
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(fomula)
    # Отметить checkbox "I'm the robot"
    checkboxes = browser.find_element(By.ID, 'robotCheckbox')
    checkboxes.click()
    # Выбрать radiobutton "Robots rule!"
    radiobuttons = browser.find_element(By.ID, 'robotsRule')
    radiobuttons.click()
    # Нажать на кнопку Submit
    submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    submit.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла