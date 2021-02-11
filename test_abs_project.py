import unittest
from selenium import webdriver
import time

class MyTest(unittest.TestCase):
    def test_reg1(self):

        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)

        fir = browser.find_element_by_xpath('//input[@placeholder= "Input your first name"]')
        fir.send_keys('Владимир Владимирович')
        las = browser.find_element_by_xpath('//input[@placeholder= "Input your last name"]')
        las.send_keys('Путин')
        email = browser.find_element_by_xpath('//input[@placeholder= "Input your email"]')
        email.send_keys('lider@kremlin.ru')

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

            # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
            # закрываем браузер после всех манипуляций
        browser.quit()
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "good")

    def test_reg2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)

        fir = browser.find_element_by_xpath('//input[@placeholder= "Input your first name"]')
        fir.send_keys('Владимир Владимирович')
        las = browser.find_element_by_xpath('//input[@placeholder= "Input your last name"]')
        las.send_keys('Путин')
        email = browser.find_element_by_xpath('//input[@placeholder= "Input your email"]')
        email.send_keys('lider@kremlin.ru')

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

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "good")

if __name__ == "__main__":
    unittest.main()