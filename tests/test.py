import unittest
from ..core.app import subdir_paths

"""
test --> all workorder/sampletype subdir's have sample files
unittest

List of bugs:
    input contraints for:
        add_workorder - workorder # length, non-integer type

"""


class TestParcelReplicator(unittest.TestCase):

    def test_workorder_constraints(self):
        """
        input length is 
        """
        return

    def test_final(self):
        """
        Test that parcel of data was replicated to correct subdirectories
        """
        print("おはよ")
        # self.assertIn()


if __name__ == "__main__":
    unittest.main()
