import time

from selenium import webdriver
import logging


def test_open_web():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    chrome_option = webdriver.ChromeOptions
    driver.maximize_window()
    driver_tittle = driver.title
    time.sleep(10)
