import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pyaspeller import YandexSpeller

def get_text(driver):
    page_text = driver.find_element(By.TAG_NAME, "main").text
    return page_text

def filter_long_text(text, max_length=100):
    sentences = text.split('. ')
    return '. '.join([s for s in sentences if len(s) <= max_length])

def check_words(text, speller, ignore_words=None):
    if ignore_words is None:
        ignore_words = set()
    errors = speller.spell(text)
    if errors:
        return [error['word'] for error in errors if error['word'] not in ignore_words]
    return []

def test_pages(driver):
    speller = YandexSpeller()
    ignore_words = {'Nexign', 'IoT', 'RCAF', 'SCEF', 'Nexign IoT', 'MEA', 'ИТ', 'кроссфункциональных', 'nexign', 'Нэксайн', 'Минцифры', 'PostgeSQL', 'B2X', 'ФЗЗ', 'Организацию'}
    driver.get("https://nexign.com/ru")
    driver.implicitly_wait(10)

    page_text = get_text(driver)
    filtered_text = filter_long_text(page_text)
    misspelled = check_words(filtered_text, speller, ignore_words)

    assert not misspelled, f"Ошибки в следующих словах: {misspelled}"

    all_links = driver.find_elements(By.TAG_NAME, 'a')

    urls = set()

    for link in all_links:
        href = link.get_attribute("href")
        if href and "nexign.com/ru" in href:
            if href != "https://nexign.com/ru/image-captcha-refresh/webform_submission_form_contacts_node_1_add_form":
                urls.add(href)

    urls = list(urls)

    for url in urls:
        driver.get(url)
        page_text = get_text(driver)
        filtered_text = filter_long_text(page_text)
        misspelled = check_words(filtered_text, speller, ignore_words)
        if misspelled:
            print(f"Ошибки на странице {url}: {misspelled}")
        time.sleep(3)

if __name__ == "__main__":
    pytest.main(["-s", "test_3.py"])