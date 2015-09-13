import sqlite3

class Model:
    def __init__(self, dburl):
        self.con = sqlite3.connect(dburl)

    def setup(self):
        cur = self.con.cursor()
        cur.execute("CREATE TABLE users (uid blob PRIMARY KEY, username varchar(28))")
        cur.execute("CREATE TABLE posts (pid blob PRIMARY KEY, uid blob, message text, postedAt integer DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (uid) REFERENCES users(uid))")
        self.con.commit()
        return True
    
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
