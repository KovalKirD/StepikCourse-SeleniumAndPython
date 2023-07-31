# Задание: оформляем тесты в стиле unittest
import unittest

class TestClassWT(unittest.TestCase):
    def test_wt(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time

        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get('http://suninjuly.github.io/registration2.html')
        # ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        input1.send_keys('test')
        input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        input2.send_keys('test')
        input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        input3.send_keys('test')
        # отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text: str = welcome_text_elt.text
        # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, 'Не совпадает')
        # закрываем браузер после всех манипуляций
        browser.quit()
        # Пустая строка