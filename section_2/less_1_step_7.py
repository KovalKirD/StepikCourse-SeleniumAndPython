# Задание: поиск сокровища с помощью get_attribute
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):  # Посчитать математическую функцию от x
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    treasure = browser.find_element(By.ID, 'treasure')
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = treasure.get_attribute('valuex')
    # Посчитать математическую функцию от x
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
    # Копируем код
    time.sleep(10)
    # Завершить сеанс
    browser.quit()

# Пустая строка