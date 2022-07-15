from selenium import webdriver
from selenium.webdriver.common.by import By
from locators.homelocators import homepagelocators


class home(object):

    def __init__(self,driver):
        self.driver = driver

    def setItemName(self,text):
        self.driver.find_element(By.XPATH, homepagelocators.enter_textbo_xpath).send_keys(text)

    def clickdropdown(self):
        self.driver.find_element(By.XPATH, homepagelocators.click_catagories_xpath).click()

    def clickselectitem(self):
        self.driver.find_element(By.XPATH, homepagelocators.click_select_item_xpath).click()

    def clicksearchbtn(self):
        self.driver.find_element(By.XPATH, homepagelocators.click_search_btn_xpath).click()
