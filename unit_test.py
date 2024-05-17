
from unittest import TestCase
from flask_testing import TestCase
from app import app, db
from app import create_app 
from app.config import DeploymentConfig
from flask import url_for
from test_data import users, form_data, api_responses, config_settings

class BasicUnitTests(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF forms protection in testing
        return app

    def setUp(self):
        super(BasicUnitTests, self).setUp()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
        super(BasicUnitTests, self).tearDown()

    def test_register(self):
        response = self.client.post(url_for('register'), data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password123',
            'confirm': 'password123'
        })
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post(url_for('login'), data={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
    

    def test_form_submission(self):
        response = self.client.post(url_for('contact'), data={
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message.'
        })
        self.assertIn("Thank you for your message", response.data.decode())

    def test_post_message(self):
        self.client.post(url_for('login'), data={'username': 'user', 'password': 'password'})
        response = self.client.post(url_for('post_message'), data={'message': 'Hello World'})
        self.assertEqual(response.status_code, 200)

    def test_view_recipes_by_type(self):
        response = self.client.get(url_for('recipes', recipe_type='Breakfast'))
        self.assertIn('Breakfast', response.data.decode())
        

    def test_new_pages(self):
        response = self.client.get(url_for('new_restaurants'))
        self.assertEqual(response.status_code, 200)
        

    

if __name__ == '__main__':
    import unittest
    unittest.main()
    