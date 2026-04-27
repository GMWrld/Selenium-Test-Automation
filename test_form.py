import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


def test_form_automation_filling():
    browser = webdriver.Firefox()

    browser.get("https://formy-project.herokuapp.com/")
    browser.maximize_window()

    browser.find_element(By.LINK_TEXT,"Form").click()

    time.sleep(2)

    #Filling the Form

    browser.find_element(By.ID,"first-name").send_keys("Gabriel")
    browser.find_element(By.ID,"last-name").send_keys("Mashenene")
    browser.find_element(By.ID,"job-title").send_keys("Business Man")
    browser.find_element(By.ID,"radio-button-3").click()
    browser.find_element(By.ID,"checkbox-1").click()
    # browser.find_element(By.ID,"select-menu").send_keys("2-4")
    year_menu = Select(browser.find_element(By.ID,"select-menu"))
    year_menu.select_by_visible_text("2-4")


    browser.find_element(By.ID,"datepicker").send_keys("11/03/2026")

    browser.find_element(By.CSS_SELECTOR,".btn.btn-lg.btn-primary").click()

    # browser.find_element(By.LINK_TEXT,"Submit").click()
    # 

    #Checking if the Form was successfully Submitted
    time.sleep(2)
    message = browser.find_element(By.CLASS_NAME,"alert").text
    assert "successfully submitted" in message
    # print("Form Submitted Successfully")
    browser.quit()

