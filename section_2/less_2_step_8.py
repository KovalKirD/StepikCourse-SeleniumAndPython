# Задание: загрузка файла
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    #Заполнить текстовые поля: имя, фамилия, email
    browser.find_element(By.NAME, 'firstname').send_keys('Test')
    browser.find_element(By.NAME, 'lastname').send_keys('Test')
    browser.find_element(By.NAME, 'email').send_keys('Test')
    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    element = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')          # добавляем к этому пути имя файла
    element.send_keys(file_path)
    # Нажать кнопку "Submit"
    browser.find_element(By.CSS_SELECTOR, 'button.btn[type="submit"]').click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# Пустая строка