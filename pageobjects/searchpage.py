from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from locators.homelocators import searchpagelocators

class search(object):

    def __init__(self,driver):
        self.driver = driver

    def getResult(self):
        result = self.driver.find_element(By.XPATH, searchpagelocators.search_results)
        print(result.text)
        print("......")

    def getNthResult(self):
        product = self.driver.find_element(By.XPATH, searchpagelocators.nth_item)
        print(product.text)
        print("......")

    def getAllProducts(self):
         list = []
         list = self.driver.find_elements(By.XPATH, searchpagelocators.all_products)

         for s in list:
             print(s.text)
             print(".....")












