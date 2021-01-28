from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Page_Objects.Encore_common import EncoreCommon


class OrderList(EncoreCommon):

    order_sidemenu = (By.XPATH, "//ul[@id='collapse1']//li[5]")
    find_option = (By.CSS_SELECTOR, "button#OrderList_hdialog_button")
    clear_parameters_button = (By.XPATH, "//div/button[@name='clearParameters']")
    order_search = (By.XPATH, "//input[@name='orderId']")
    find_button = (By.CSS_SELECTOR, "button[id='OrderList_header_submitButton']")
    csv = (By.XPATH, "//a[contains(text(),'CSV')]")
    xls = (By.XPATH, "//a[contains(text(),'XLS')]")
    create_purchase_order = (By.ID, "CreatePurchaseOrderDialog-button")
    create_sales_order = (By.ID, "CreateSalesOrderDialog-button")
    create_purchase_title = (By.XPATH, "//h4[normalize-space()='Create Purchase Order']")
    create_sales_title = (By.XPATH, "//h4[contains(text(),'Create Sales Order')]")

    def __init__(self, driver):
        self.driver = driver

    def order_listing(self):
        return self.onclick(self.order_sidemenu)

    def order_find_option(self):
        return self.onclick(self.find_option)

    def clear_parameter(self):
        return self.onclick(self.clear_parameters_button)

    def get_order_search(self):
        return self.driver.find_element(*OrderList.order_search)

    def get_find_button(self):
        return self.onclick(self.find_button)

    def get_csv(self):
        return self.onclick(self.csv)

    def get_xls(self):
        return self.onclick(self.xls)

    def get_create_purchase_button(self):
        return self.onclick(self.create_purchase_order)

    def get_create_purchase_title(self):
        return self.get_element_text(self.create_purchase_title)

    def get_sales_order_button(self):
        return self.onclick(self.create_sales_order)

    def get_create_sale_title(self):
        return self.get_element_text(self.create_sales_title)
