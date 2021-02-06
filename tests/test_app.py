import unittest
from flask_testing import TestCase
from flask import url_for
from app import app, db, Task

class TestBase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/testdb'
        return app
    
    def setUp(self):
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)


class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(url_for('home'), data = dict(task_name="buy milk"))
        self.assertIn(b'buy milk', response.data)


class TestUpdate(TestBase):
    def test_update_post(self):
        response = self.client.post(url_for('update'), data = dict(new_task="buy apple Fanta", old_task="buy orange Fanta"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

class TestDelete(TestBase):
    def test_delete_post(self):
        response = self.client.post(url_for('delete'), data = dict(task_name="buy orange Fanta"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)