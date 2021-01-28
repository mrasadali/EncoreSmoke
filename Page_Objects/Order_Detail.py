from selenium.webdriver.common.by import By

from Page_Objects.Encore_common import EncoreCommon


class OrderDetailPage(EncoreCommon):
    order_sidemenu = (By.XPATH, "//ul[@id='collapse1']//li[5]")
    order_click = (By.CSS_SELECTOR, "a[id='OrderList_orderId_1_orderDetail']")
    item = (By.CSS_SELECTOR, "a[id='OrderItems_productLink_0_0_editProduct']")
    address = (By.CSS_SELECTOR, "div[class='row'] address")
    buttons = (By.CSS_SELECTOR, "button[onclick][class='btn btn-primary btn-sm']")

    def __init__(self, driver):
        self.driver = driver

    def get_order_sidemenu(self):
        return self.onclick(self.order_sidemenu)

    def get_order_click(self):
        return self.onclick(self.order_click)

    def get_line_item(self):
        return self.get_element_text(self.item)

    def get_address(self):
        return self.get_element_text(self.address)

    def get_buttons(self):
        return self.get_element_text(self.buttons)