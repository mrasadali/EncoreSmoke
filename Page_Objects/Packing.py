from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Page_Objects.Encore_common import EncoreCommon


class Packing(EncoreCommon):
    shipping_sidemenu = (By.XPATH, "//ul[@id='collapse1']/li[7]")
    picklists_button = (By.LINK_TEXT, "Picklists")
    new_picklist = (By.ID, "NewPicklistContainer-button")
    facility = (By.CLASS_NAME, "facilityId")

    def __init__(self, driver):
        self.driver = driver

    def get_shipping(self):
        return self.onclick(self.shipping_sidemenu)

    def get_picklist(self):
        return self.onclick(self.picklists_button)

    def get_new_picklist(self):
        return self.onclick(self.new_picklist)

    #def get_facility(self):
    #    return self.onclick(self.facility)
    def drop_down(self, text):
        select = Select(self.driver.find_element(*self.facility))
        selection = select.select_by_visible_text(text)
        return selection