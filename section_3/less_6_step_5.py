# Задание: параметризация тестов
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]

def authorization(browser):
    import config
    browser.find_element(By.ID, 'ember33').click()
    browser.find_element(By.NAME, 'login').send_keys(config.login)
    browser.find_element(By.NAME, 'password').send_keys(config.passw)
    browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader').click()

def answer_step():
    import math
    answer = math.log(int(time.time()))
    return answer

@pytest.mark.parametrize('link', links)
def test_message(browser, link):
    browser.get(link)
    authorization(browser)

    # Ответ
    time.sleep(5)
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.ember-text-area.ember-view.textarea.string-quiz__textarea'))
    )
    browser.find_element(By.CSS_SELECTOR, '.ember-text-area.ember-view.textarea.string-quiz__textarea').send_keys(answer_step())
    # Кнопка Отправить
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))
    )
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    # Опциональный фидбек
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))
    )
    feedback = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint')
    # Проверка
    assert feedback.text == 'Correct!', f'{feedback.text}'