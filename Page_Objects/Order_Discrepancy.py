from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Page_Objects.Encore_common import EncoreCommon
# Retrieve button case remaining

class OrderDiscrepancy(EncoreCommon):
    order_report = (By.XPATH, "//ul[@id='collapse1']/li[14]")
    choose_store = (By.CSS_SELECTOR, "button[id='ChooseStoreDialog-button']")
    store_name = (By.ID, "ChooseStoreForm_integrationId")
    calendar = (By.XPATH, "//div[@id='ChooseStoreForm_fromDate']/span")
    go_button = (By.ID, "ChooseStoreForm_submitButton")
    csv = (By.LINK_TEXT, "CSV")
    xls = (By.LINK_TEXT, "XLS")

    def __init__(self, driver):
        self.driver = driver

    def get_order_reports(self):
        return self.onclick(self.order_report)

    def get_choose_store(self):
        return self.onclick(self.choose_store)

    def drop_down(self, text):
        select = Select( self.driver.find_element(*self.store_name))
        selection = select.select_by_visible_text(text)
        return selection

    def get_calendar(self):
        return self.onclick(self.calendar)

    def get_go_button(self):
        return self.onclick(self.go_button)

    def get_csv(self):
        return self.onclick(self.csv)

    def get_xls(self):
        return self.onclick(self.xls)
