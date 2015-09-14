import unittest
import uuid
from model import Model

#mockModel = Model("test.db")
mockUID = uuid.uuid4()

class MockModel:
    def createModel():
        mock = Model("test.db")
        return mock

    def setup():
        mock = MockModel.createModel()
        mock.setup()
        return mock

    def createUser():
        mock = MockModel.setup()
        uid = mock.addUser("foo bar")
        return (mock, uid)

class ModelTest(unittest.TestCase):
    
    def setUp(self):
        #mockModel = Model(":memory:")
        pass

    def tearDown(self):
        #mock.close()
        pass

    def test0ModelInit(self):
        #mockModel = Model(":memory:")
        result = MockModel.createModel().setup()
        self.assertIsNotNone(result, "Problem with successful db creation")

    def test0z(self):
        mock = MockModel.setup()
        mockUID = mock.addUser("foo bar")
        self.assertEqual("foo bar", mock.getUser(mockUID), "Calling a user ID should return that user")

    def test1(self):
        mock = MockModel.setup()
        for i in range(2):
            uidBad = mock.addUser("foo bar")
        self.assertIsNone(uidBad, "Adding a user twice should fail and return a uid of none")
        
    def test2(self):
        mock, uid = MockModel.createUser()
        for num in range(10):
            mock.addPost(uid, str(num))
            
        posts = mock.getUserPosts(uid, 0)

        self.assertIsInstance(posts, list, "getUserPosts should return a list of posts")

        for num in range(10):
            self.assertEqual(posts[num]["message"], str(9-num), "Messages should be returned in reverse-chronological order")

    def test5(self):
        mock, uid = MockModel.createUser()
        pid = mock.addPost(uid, "x" * 140)
        self.assertEqual(mock.getPost(pid), "x" * 140, "Should accept posts up to 140 characters")

    def test6(self):
        mock, uid = MockModel.createUser()
        pid = mock.addPost(uid, "")
        self.assertIsNone(pid, "Should reject 0 character messages.")

    def test7(self):
        mock, uid = MockModel.createUser()
        pid = mock.addPost(uid, "x" * 141)
        self.assertIsNone(pid, "Should reject messages with over 140 characters")

if __name__ == "__main__":
    unittest.main()
