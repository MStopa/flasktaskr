import os
import unittest

from project import app, db
from project._config import basedir
from project.models import User

TEST_DB = 'test.db'

class MainTests(unittest.TestCase):

    # executed priot to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{str(os.path.join(basedir, TEST_DB))}"
        self.app = app.test_client()
        db.create_all()
    
    # executed after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    # helpers
    def login(self, name, password):
        return self.app.post('/', data=dict(
            name = name,
            password=password
        ), follow_redirects=True)
    
    # tests
    def test_tests_with_debug_false(self):
        return self.assertEquals(app.debug, False)


    def test_404_error(self):
        response = self.app.get('/this-route-does-not-exist/')
        self.assertEquals(response.status_code, 404)
        self.assertIn(b"Sorry, there's nothing here.", response.data)


if __name__ == "__main__":
    unittest.main()