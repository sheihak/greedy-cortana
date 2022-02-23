import argparse
from lib2to3.pgen2 import driver
# import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys

import zipfile
import os, stat


def main():
    print("Ça fonctionne")
    a = 2
    b = 3
    # driver.get("http://www.python.org")
    # assert "Python" in driver.title
    # elem = driver.find_element_by_name("q")
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    # driver.close()

    return