import json
import unittest
from users import app


class UserTest(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b'Welcome to student API' in response.data)

    def test_users_post(self):
        payload = json.dumps({
            "name": "Anuj",
            "email": "Anuj@gmail.com",
            "password": "Anuj123@",
        })
        tester = app.test_client(self)
        response = tester.post("/users", headers={"Content-Type": "application/json"}, data=payload)
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, "application/json")
        self.assertTrue(b'User is added Successfully' in response.data)

    def test_users_get(self):
        tester = app.test_client(self)
        response = tester.get("/users")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        # self.assertEqual(response.content_type, "application/json")

    def test_user_get_by_userID(self):
        tester = app.test_client(self)
        response = tester.get("/users/641e610d41ffa465d94ba11c")
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        # self.assertEqual(response.content_type, "application/json")

if __name__ == '__main__':
    unittest.main()
