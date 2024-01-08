import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_btn = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_btn.click()
    print(driver.current_url)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Error wrong URL"
    time.sleep(5)
    driver.find_element(By.NAME, "username").send_keys("John Doe")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID, "btn-login").click()
    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Error wrong URL"


