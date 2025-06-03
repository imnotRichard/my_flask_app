import unittest
from src.app import app

class IntegrationTest(unittest.TestCase):
    def setUp(self):
        """
        Set up a test client before each test.
        """
        self.app = app.test_client()
        self.app.testing = True

    def test_submit(self):
        """
        Test the /submit route with sample form data.
        Checks if the response contains the correct echoed data.
        """
        response = self.app.post('/submit', data={
            'sleep': '8',
            'water': '1500',
            'mood': 'happy'
        })
        self.assertEqual(response.status_code, 200)
        response_text = response.get_data(as_text=True)
        self.assertIn('You slept: 8 hours', response_text)
        self.assertIn('drank: 1500 ml water', response_text)
        self.assertIn('mood: happy', response_text)

if __name__ == '__main__':
    unittest.main()
