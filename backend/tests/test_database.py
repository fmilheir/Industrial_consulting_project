import unittest
from database import test_db_connection
from database import create_table_user_if_not_exists
from database import create_table_car_if_not_exists
from database import create_table_trip_if_not_exists
from database import create_table_public_transport_if_not_exists


class TestDatabase(unittest.TestCase):
    #General connection test
    def test_test_db_connection(self):
        self.assertEqual("Database connection successful", test_db_connection())

    #Tests for table generation
    def test_create_table_user_if_not_exists(self):
        self.assertEqual("Table 'user' created successfully.",create_table_user_if_not_exists())

    def test_create_table_car_if_not_exists(self):
        self.assertEqual("Table 'car' created successfully.",create_table_car_if_not_exists())

    def test_create_table_trip_if_not_exists(self):
        self.assertEqual("Table 'trip' created successfully.",create_table_trip_if_not_exists())

    def test_create_table_public_transport_if_not_exists(self):
        self.assertEqual("Table 'public_transport' created successfully.",create_table_public_transport_if_not_exists())





if __name__ == '__main__':
    unittest.main()
