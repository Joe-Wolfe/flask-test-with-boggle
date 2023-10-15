from unittest import TestCase
from app import app
from flask import session


class FlaskTests(TestCase):
    def setUp(self):
        """Pre test Set Up"""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Testing html is displayed"""

        with self.client:
            response = self.client.get('/')
            self.assertIn('Score:'.encode(), response.data)

    def test_invalid_word(self):
        """Testing if a word is not on the board *highly unlikely to pass but might?"""

        self.client.get('/')
        response = self.client.get('/check?word=zymophosphate')
        self.assertEqual(response.json['result'], 'not-on-board')

    def non_english_word(self):
        """Test if word is on the board"""

        self.client.get('/')
        response = self.client.get(
            '/check?word=mom')
        self.assertEqual(response.json['result'], 'not-word')
