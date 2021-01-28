import time

from Page_Objects.Order_List import OrderList
from Page_Objects.Sipment_List import ShipmentList
from Utilities.BaseClass import BaseClass


class TestCase5(BaseClass):
    def test_testcase5(self):
        self.login()
        shipment_list = ShipmentList(self.driver)
        # Using order list because i don't want to initialize same pom in different testcase so i use orderlist object
        order_list = OrderList(self.driver)
        order_list.order_listing()
        order_list.order_find_option()
        order_list.clear_parameter()
        order_list.get_order_search().send_keys("106429")
        order_list.get_find_button()
        order_list.get_csv()
        shipment_list.get_order_detail()
        time.sleep(3)
        check_text = shipment_list.get_shipment_button()
        self.check_availibility_of_element("Create Shipment")