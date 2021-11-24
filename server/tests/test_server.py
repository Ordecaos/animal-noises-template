import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_view_animals(self):
        with requests_mock.Mocker() as m:
            m.get('http://animal_api:5000/animal/name', text='Pig')
            m.post('http://animal_api:5000/animal/noise', text='Oink')
            response = self.client.get(url_for('animals'))
     self.assertEqual(response.status_code, 200)

    def test_pig_noise(self):
        with requests_mock.Mocker() as m:
            m.get('http://animal_api:5000/animal/name', text='Pig')
            m.post('http://animal_api:5000/animal/noise', text='Oink')
            
            response = self.client.get(url_for('animals'))
            self.assertIn(b'The Pig Goes Oink')

    def test_cow_noise(self):
        with requests_mock.Mocker() as m:
            m.get('http://animal_api:5000/animal/name', text='Cow')
            m.get('http://animal_api:5000/animal/noise', text='Moo')

            response = self.client.get(url_for('animals'))
            self.assertIn(b'The Cow Goes Moo')

    def test_dog_noise(self):
        with requests_mock.Mocker() as m:
            m.get('http://animal_api:5000/animal/name', text='Dog')
            m.get('http://animal_api:5000/animal/noise', text='Woof')

            response = self.client.get(url_for('animals'))
            self.assertIn(b'The Dog Goes Woof')