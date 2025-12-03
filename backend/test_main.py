import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the backend directory to sys.path so we can import main
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import app

class TestBackend(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok"})

    @patch('main.model')
    def test_chat_mock_mode(self, mock_model):
        # Ensure model is None to trigger mock mode
        import main
        main.model = None

        response = self.app.post('/chat', data={'message': 'Hello'})
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('response', data)
        self.assertIn('demo mode', data['response'])

    @patch('main.model')
    def test_chat_pothole_mock(self, mock_model):
        # Ensure model is None
        import main
        main.model = None

        response = self.app.post('/chat', data={'message': 'I found a pothole'})
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('response', data)
        self.assertIn('Ticket #ADM-DEMO-123', data['response'])

if __name__ == '__main__':
    unittest.main()
