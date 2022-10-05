# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestCheckbox():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_checkbox(self):
        self.driver.get("https://www.swtest.cz/")
        self.driver.set_window_size(1920, 1032)
        elements = self.driver.find_elements(By.XPATH, "//label[1]/input[@type=\"checkbox\"]")
        assert len(elements) > 0
        self.vars["noCheckbox"] = len(self.driver.find_elements(By.XPATH, "//input[@type=\"checkbox\"]"))
        print("{}".format(self.vars["noCheckbox"]))
        self.vars["prvniCheckbox"] = len(self.driver.find_elements(By.XPATH, "//input[@id=\'brand-input-1\']"))
        print("{}".format(self.vars["prvniCheckbox"]))
        if self.driver.execute_script("return (arguments[0] > 0)", self.vars["prvniCheckbox"]):
            assert self.driver.find_element(By.XPATH, "//input[@id=\'brand-input-1\']").is_selected() is False
            element = self.driver.find_element(By.ID, "brand-input-1")
            assert element.is_enabled() is True
