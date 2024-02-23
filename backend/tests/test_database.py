import unittest
from database import *


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


#input and select statement tests
    def test_create_new_user(self):
        self.assertEqual("New user created successfully.",create_new_user("Joe","Momma","joe@momma.com","07464769378",1))

    def test_create_public_transport(self):
        self.assertEqual("New transport created successfully.",create_new_public_transport("truck", 1))

if __name__ == '__main__':
    unittest.main()
