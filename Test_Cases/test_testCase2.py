import time

from Page_Objects.Order_Detail import OrderDetailPage
from Utilities.BaseClass import BaseClass


class TestCase2(BaseClass):
    def test_testcase2(self):
        self.login()
        order_detail = OrderDetailPage(self.driver)
        order_detail.get_order_sidemenu()
        order_detail.get_order_click()
        time.sleep(3)
        line_item = order_detail.get_line_item()
        self.check_availibility_of_element(line_item)
        customer_address = order_detail.get_address()
        self.check_availibility_of_element(customer_address)
        buttons_visible = order_detail.get_buttons()
        self.check_availibility_of_element(buttons_visible)

