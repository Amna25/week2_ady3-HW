import unittest
from src.pub import Pub


class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The parncing pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The parncing pony", self.pub.name)

    def test_pub_increase_money(self, amount):
        self.pub.increase_ += 
        

    def test_recieve_drink(self, reduce_stock):
        reduce_stock== -1
        self.assetEqual(-1, self.pub)