import sqlite3

class Model:
    def __init__(self, dburl):
        self.con = sqlite3.connect("database.db")

    def setup(self):
        return None
    
    def close(self):
        self.con.close()
        
    def addUser(self, username):
        #TODO: Validate user input
        #TODO: raise and handle exceptions in the event of invalid input or sql glitch
        userID = 0
        return userID

    def addPost(self, userID, message):
        #should this take a session ID?
        #post to the user's stream a new message
        postID = ""
        return postID

    def getUser(self, userID):
        return ""

    def getPost(self, postID):
        return None

    def getUserPosts(self, userID, start=0):
        return []

    def deletePost(self, messageID):
        return None
    
    def deleteUser(self, userID):
        return None
