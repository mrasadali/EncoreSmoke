import time

from Page_Objects.Order_List import OrderList
from Utilities.BaseClass import BaseClass


class TestCases(BaseClass):

    def test_case1(self):

        order = OrderList(self.driver)
        self.login()
        order.order_listing()
        order.order_find_option()
        order.clear_parameter()
        order.get_order_search().send_keys("106536:01")
        #order.get_find_button()
        self.driver.get("https://staging-encore.brandedonline.com/vapps/oms/Order/FindOrder")
        order.get_csv()
        order.get_xls()
        order.get_create_purchase_button()
        time.sleep(3)
        title_text = order.get_create_purchase_title()
        print(title_text)
        assert title_text == order.check_purchase_title
        self.driver.get("https://staging-encore.brandedonline.com/vapps/oms/Order/FindOrder")
        order.get_sales_order_button()
        sales_tittle = order.get_create_sale_title()
        print(sales_tittle)
        time.sleep(3)
        assert sales_tittle in order.check_sales_title