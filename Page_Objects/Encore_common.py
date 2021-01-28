from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EncoreCommon:

    check_purchase_title = "Create Purchase Order"
    check_sales_title = "Create Sales Order"

    def onclick(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).click()

    def sendkey(self, locator, value):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_title(self, title):
        WebDriverWait(self.driver, 30).until(EC.title_is(title))
        return self.driver.title

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return element.text

    def get_elements_text(self, locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(locator))
        return element.text



   # def visibility(self, locator):
    #    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located(locator))
     #   return bool(element)