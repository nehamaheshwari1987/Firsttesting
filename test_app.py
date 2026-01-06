import unittest
from app import app

class HelloCITestCase(unittest.TestCase):
    def setUp(self):
        # set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # send a GET request to the home route
        response = self.app.get('/')
        
        self.assertEqual(response.status_code, 200)
        
        # Check that the response data is "Hello, CI/CD!"
        self.assertEqual(response.data.decode('utf-8'), "Hello, CI/CD!")

if __name__ == '__main__':
    unittest.main()
