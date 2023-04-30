from selenium import webdriver

import pytest
import time

driver = webdriver.Chrome()
driver.get("https://codeforces.com/profile/Ad_OK")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
driver.implicitly_wait(10)

def test_current_url():
    assert 'codeforces' in driver.current_url

@pytest.mark.fast
def test_title():
    assert 'Adok' in driver.title
