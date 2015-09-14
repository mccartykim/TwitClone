import sqlite3
import uuid

class Model:
    def __init__(self, dburl):
        self.con = sqlite3.connect(dburl)

    def setup(self):
        #cur = self.con.cursor()
        with self.con:
            self.con.execute("DROP TABLE IF EXISTS users")
            self.con.execute("DROP TABLE IF EXISTS posts")
            self.con.execute("CREATE TABLE users (uid blob PRIMARY KEY, username varchar(28) UNIQUE)")
            self.con.execute("CREATE TABLE posts (pid blob PRIMARY KEY, uid blob, message text, postedAt integer DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (uid) REFERENCES users(uid))")
        #self.con.commit()
        #self.con.close()
        return True
    
    def close(self):
        self.con.close()
        
    def addUser(self, username):
        #TODO: Validate user input
        #TODO: raise and handle exceptions in the event of invalid input or sql glitch
        userID = uuid.uuid4()
        try:
            cur = self.con.cursor()
            cur.execute("INSERT INTO users VALUES (?, ?)", (sqlite3.Binary(userID.bytes), username))
            self.con.commit()
        except sqlite3.IntegrityError:
            self.con.rollback()
            return None
        return userID

    def addPost(self, userID, message):
        #should this take a session ID?
        #post to the user's stream a new message
        if len(message) == 0 or len(message) > 140:
            return None
        postID = uuid.uuid4()
        with self.con:
            self.con.execute("INSERT INTO posts(pid, uid, message) VALUES (?, ?, ?)", (sqlite3.Binary(postID.bytes), sqlite3.Binary(userID.bytes), message))
            return postID
        return None

    def getUser(self, userID):
        cur = self.con.cursor()
        cur.execute("SELECT username FROM users WHERE uid == ?", (sqlite3.Binary(userID.bytes),))
        username = cur.fetchone()[0];
        return username

    def getPost(self, postID):
        cur = self.con.cursor()
        cur.execute("SELECT message FROM posts where pid == ?", (sqlite3.Binary(postID.bytes),))
        return cur.fetchone()[0]

    def getUserPosts(self, userID, start=0, sel_length=10):
        cur = self.con.cursor()
        cur.execute("""SELECT users.username, posts.message, posts.postedAt, posts.pid
                   FROM users
                   JOIN posts using (uid)
                   WHERE uid == ?
                   ORDER BY posts.rowid DESC LIMIT ?""", (sqlite3.Binary(userID.bytes), sel_length))
        rows = cur.fetchall()
        results = []
        for entry in rows:
            post = {"username": entry[0], "message": entry[1], "postedAt": entry[2], "postID": entry[3]}
            results.append(post)
        return results

    def deletePost(self, messageID):
        return None
    
    def deleteUser(self, userID):
        return None
