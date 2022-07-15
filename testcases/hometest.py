import time
import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
from pageobjects.searchpage import search
sys.path.append("/Users/abiharaza/Documents/POM")
from pageobjects.homepage import home


class Test(unittest.TestCase):
    baseURL = "https://www.ebay.com/"
    driver = webdriver.Chrome()
    driver.get(baseURL)

    def test_search_product(self):
    #homepage
        hp = home(self.driver)
        hp.setItemName("iphone")
        hp.clickdropdown()
        hp.clickselectitem()
        hp.clicksearchbtn()

    #searchpage
        sp = search(self.driver)
        sp.getResult()
        sp.getNthResult()
        sp.getAllProducts()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\reports'))




