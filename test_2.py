import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def count_nexign_mentions(driver):
    page_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    return page_text.count("nexign")

def test_count(driver):
    driver.get("https://nexign.com/ru")
    mentions_count = count_nexign_mentions(driver)
    print('Количество упоминаний слова "Nexign":', mentions_count) #32 

    assert mentions_count > 0, 'Упоминаний "Nexign" не найдено'
