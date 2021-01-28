import time

# from Page_Objects.Order_List import OrderList
from Page_Objects.Shipment_Details import ShipmentDetails
from Utilities.BaseClass import BaseClass


class TestCase6(BaseClass):

    def test_testcase6(self):
        self.login()
        shipment_details = ShipmentDetails(self.driver)
        shipment_details.get_shipment_sidemenu()
        shipment_details.get_shipment_find_option()
        shipment_details.get_shipment_clear_parameter()
        shipment_details.get_shipment().send_keys("103316")
        shipment_details.get_shipment_find_button()
        time.sleep(3)
        shipment_details.get_order()
        issue_button = shipment_details.get_pack_issue_button()
        assert issue_button in self.pack_issue_item
        shipment_details.get_reset_reservation()
        reserve_popup = shipment_details.get_reserve_text()
        assert reserve_popup in self.reserve
        shipment_details.get_reserve_close()
        shipment_details.get_pack()
        shipment_details.get_insert()
        time.sleep(3)