from selenium.webdriver.common.by import By

from Page_Objects.Encore_common import EncoreCommon


class OrderAgingPage(EncoreCommon):

    order_aging = (By.XPATH, "//ul[@id='collapse1']/li[6]")
    select_facility = (By.CSS_SELECTOR, "button[id='SelectFacility_submitButton']")
    order_listing = (By.XPATH, "//tbody/tr[2]/td[6]/a")
    check_order_listing = (By.XPATH, "//*[@id='apps-root']/div[1]/section/h1")
    # "//h1[@class='content-title']"

    def __init__(self, driver):
        self.driver = driver

    def get_order_aging(self):
        return self.onclick(self.order_aging)

    def get_select_facility(self):
        return self.onclick(self.select_facility)

    def get_order_listing(self):
        return self.onclick(self.order_listing)

    def get_check_order_listing(self):
        return self.get_element_text(self.check_order_listing)