import time

from Page_Objects.Order_Discrepancy import OrderDiscrepancy
from Utilities.BaseClass import BaseClass
# Retrieve button case remaining


class TestCase4(BaseClass):
    def test_testcase4(self):

        self.login()
        order_discrepancy = OrderDiscrepancy(self.driver)
        order_discrepancy.get_order_reports()
        order_discrepancy.get_choose_store()
        order_discrepancy.drop_down("KK_SHOPIFY")
        #order_discrepancy.get_calendar()
        order_discrepancy.get_go_button()
        order_discrepancy.get_csv()
        order_discrepancy.get_xls()

        time.sleep(2)
