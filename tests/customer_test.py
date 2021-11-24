import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer= Customer("Jim",500)

    def test_customer_has_name(self):
        self.assertEqual("Jim", self.customer.name)