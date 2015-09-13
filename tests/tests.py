import unittest
from model import Model

mockModel = Model(":memory:")
mockUID = None

class ModelTest(unittest.TestCase):
    
    def setUp(self):
        #mockModel = Model(":memory:")
        pass

    def tearDown(self):
        #mockModel.close()
        #del mockModel()
        pass

    def test0ModelInit(self):
        mockModel = Model(":memory:")
        result = mockModel.setup()
        self.assertTrue(result, "Should return true on successful db creation")

    def test0z(self):
        mockUID = mockModel.addUser("foo bar")
        self.assertEqual("foo bar", mockModel.getUser(mockUID), "Calling a user ID should return that user")

    def test1(self):
        uidBad = mockModel.addUser("foo bar")
        self.assertIsNone(uidBad, "Adding a user twice should fail and return a uid of none")
        
    def test2(self):
        for num in range(10):
            mockModel.addPost(mockUID, str(num))
            
        posts = mockModel.getUserPosts(mockUID, 0)

        self.assertIsInstance(posts, list, "getUserPosts should return a list of posts")

        for num in range(10):
            self.assertEqual(posts[num]["message"], str(9-num), "Messages should be returned in reverse-chronological order")

    def test5(self):
        pid = mockModel.addPost(mockUID, "x" * 140)
        self.assertEqual(mockModel.getPost(pid), "x" * 140, "Should accept posts up to 140 characters")

    def test6(self):
        pid2 = mockModel.addPost(mockUID, "")
        self.assertIsNone(pid2, "Should reject 0 character messages.")

    def test7(self):
        pid2 = mockModel.addPost(mockUID, "x" * 141)
        self.assertIsNone(pid2, "Should reject messages with over 140 characters")

if __name__ == "__main__":
    unittest.main()
