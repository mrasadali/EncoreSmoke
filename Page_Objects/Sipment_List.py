from selenium.webdriver.common.by import By

from Page_Objects.Encore_common import EncoreCommon
from Page_Objects.Order_List import OrderList


class ShipmentList(OrderList):

    order_detail = (By.CSS_SELECTOR, "a[id='OrderList_orderId_0_orderDetail']")
    shipment_button = (By.XPATH, "//button[@class='btn btn-success btn-sm']")
    #order_sidemenu = (By.XPATH, "//ul[@id='collapse1']//li[5]")
    #find_option = (By.CSS_SELECTOR, "button#OrderList_hdialog_button")

    def __init__(self, driver):
        self.driver = driver

   # def get_order_sidemenu(self):
   #     return self.onclick(self.order_sidemenu)

   # def get_find_option(self):
   #     return self.onclick(self.find_option)

    def get_order_detail(self):
        return self.onclick(self.order_detail)

    def get_shipment_button(self):
        return self.get_element_text(self.shipment_button)