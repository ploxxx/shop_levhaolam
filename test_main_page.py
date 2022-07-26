import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage

def test_sign_in_the_site(browser):
    link = "https://shop.levhaolam.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_sign_in()
