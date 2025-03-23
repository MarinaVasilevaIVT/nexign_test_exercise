import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://nexign.com/ru"

def test_nord(driver):
    driver.get(link)
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//li/span[text()='Продукты и решения']").click()
    driver.find_element(By.XPATH, "//li/span[text()='Инструменты для ИТ-команд']").click()
    driver.find_element(By.XPATH, "//li/a[text()='Nexign Nord']").click()
    title = driver.find_element(By.XPATH, "//h1")
    assert title.text == 'Nexign Nord', title.text