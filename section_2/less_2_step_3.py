# Задание: работа с выпадающим списком
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Сумма чисел строкой
def total_sum(num1, num2):
    return str(int(num1) + int(num2))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')

    # Посчитать сумму заданных чисел
    x = browser.find_element(By.ID, 'num1').text
    y = browser.find_element(By.ID, 'num2').text
    total = total_sum(x, y)
    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(total)
    # Нажать кнопку "Submit"
    submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()

finally:
    # Коприруем код
    time.sleep(10)
    # Завершить сценарий
    browser.quit()

# Пустая строка