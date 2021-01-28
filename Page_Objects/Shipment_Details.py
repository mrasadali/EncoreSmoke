from selenium.webdriver.common.by import By

from Page_Objects.Encore_common import EncoreCommon


class ShipmentDetails(EncoreCommon):
    shipment_sidemenu = (By.XPATH, "//ul[@id='collapse1']/li[8]")
    shipment_find_option = (By.ID, "ShipmentList_hdialog_button")
    clear_parameters_button = (By.XPATH, "//div/button[@name='clearParameters']")
    pack_issue_item_button = (By.ID, "PackItemContainer_0-button")
    shipment_search = (By.ID, "ShipmentList_header_shipmentId")
    shipment_find_button = (By.XPATH, "//div/button[@name='findButton']")
    order = (By.LINK_TEXT, "103316")
    reset_reservation_reserve = (By.ID, "ItemReserveDialog_0_0-button")
    reserve_text = (By.XPATH, "//h4[contains(text(),'Reserve')]")
    reserve_close = (By.CSS_SELECTOR, "div[id='ItemReserveDialog_0_0'] button[type='button']")
    pack_pdf = (By.LINK_TEXT, "Pack")
    insert_pdf = (By.LINK_TEXT, "Insert")

    def __init__(self, driver):
        self.driver = driver

    #def get_script_element(self):
    #    WebElement scriptElement = self.driver.findElement(By.tagName("script"))
    #    scriptText = ((JavascriptExecutor)driver).executeScript("return arguments[0].innerHTML", scriptElement)

    def get_shipment_sidemenu(self):
        return self.onclick(self.shipment_sidemenu)

    def get_shipment_find_option(self):
        return self.onclick( self.shipment_find_option )

    def get_shipment_clear_parameter(self):
        return self.onclick( self.clear_parameters_button )

    def get_shipment_find_button(self):
        return self.onclick( self.shipment_find_button )

    def get_shipment(self):
        return self.driver.find_element( *self.shipment_search )

    def get_order(self):
        return self.onclick( self.order )

    def get_pack_issue_button(self):
        return self.get_element_text(self.pack_issue_item_button)

    def get_reset_reservation(self):
        return self.onclick(self.reset_reservation_reserve)

    def get_reserve_text(self):
        return self.get_element_text(self.reserve_text)

    def get_reserve_close(self):
        return self.onclick(self.reserve_close)

    def get_pack(self):
        return self.onclick(self.pack_pdf)

    def get_insert(self):
        return self.onclick(self.insert_pdf)

