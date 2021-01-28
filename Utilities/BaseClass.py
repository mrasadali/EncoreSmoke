import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures( "setup" )
class BaseClass:
    name = "Asad"
    password = "asad@123"
    pack_issue_item = "Pack/Issue Item"
    reserve = "Reserve"

    def login(self):
        # loginpage = LoginPage(self.driver)
        # loginpage.user_name().send_keys("Asad")
        # loginpage.login_password().send_keys("asad@123")
        # loginpage.login().click()
        self.driver.find_element(By.ID, "login_form_username").send_keys("Asad")
        self.driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("asad@123")
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Sign in')]").click()

    def check_availibility_of_element(self, variable):
        if len(variable) == 0:
            print("Test case failed")
        else:
            print("Test Case Passed")

    # Two ways to assert the text
    def asserting_the_text(self, text, variable):
        if text in variable:
            print("Successfully Asserted")
        else:
            print("String is not present")

    def check_the_assertion(self, text, variable):
        assert text in variable
