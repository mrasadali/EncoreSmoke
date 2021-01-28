import time

from Page_Objects.Packing import Packing
from Utilities.BaseClass import BaseClass


class TestCase7(BaseClass):

    def test_testcase7(self):
        self.login()
        packing = Packing(self.driver)
        packing.get_shipping()
        packing.get_picklist()
        packing.get_new_picklist()
        packing.drop_down("KK_FACILITY: Karen Kane Warehouse")
        time.sleep(2)