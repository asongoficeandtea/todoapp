import unittest
from flask_testing import TestCase
from flask import url_for
from app import app, db, Task

class TestBase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://alimatea7:mariam@localhost/testdb'
        return app
    
    def setUp(self):
        db.create_all()

      # sample data 
        test_task = Task(task_name="buy milk")
        
        db.session.add(test_task)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)


# Testing adding data.
class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(url_for('home'), data = dict(task_name="buy apple Fanta"))
        self.assertIn(b'buy apple Fanta', response.data)

# Testing updating data.
class TestUpdate(TestBase):
    def test_update_post(self):
        response = self.client.post(url_for('update'), data = dict(new_task="buy Doritos", old_task="buy milk"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

# Testing deleting data.
class TestDelete(TestBase):
    def test_delete_post(self):
        response = self.client.post(url_for('delete'), data = dict(task_name="buy milk"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
