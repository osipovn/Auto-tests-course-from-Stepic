import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquite browser..")
    browser.quit()

@pytest.mark.parametrize('numb', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_input_answer(browser, numb):
    link = f"https://stepik.org/lesson/{numb}/step/1"
    browser.get(link)
    browser.implicitly_wait(15)
    input = browser.find_element_by_tag_name('textarea')
    input.send_keys(str(math.log(int(time.time()))))
    but = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    but.click()
    corr = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
    assert corr == "Correct!", corr

