import time

from Page_Objects.Order_Aging import OrderAgingPage
from Utilities.BaseClass import BaseClass


class TestCase3(BaseClass):
    def test_testcase3(self):
        self.login()
        order_age = OrderAgingPage(self.driver)
        order_age.get_order_aging()
        order_age.get_select_facility()
        order_age.get_order_listing()
        checking = order_age.get_check_order_listing()
        print(checking)
        self.asserting_the_text("Orders | Find Order", checking)
