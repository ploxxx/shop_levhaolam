import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options

class MainPage():
   
    def test_sign_in(self):
        link = "https://shop.levhaolam.com/"
        login_email = self.browser.find_element(By.ID , "username")
        login_email.send_keys("vladz@levhaolam.com")
        login_password = self.browser.find_element(By.ID , "password")
        login_password.send_keys("Vld5444789")
        self.browser.find_element(By.XPATH,"//button[@name='login']").click()
        