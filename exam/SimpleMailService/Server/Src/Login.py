from re import S
from UserMode import UserModeService
from Service import *

class LoginService(Service):
    def __init__(self):
        super(LoginService, self).__init__()
        self._isFinished = False

    def serve(self, s):
        self._isFinished = False

        s.send("\nPlease enter your username: ".encode())
        name = s.recv(1024).decode()
        
        if not ((name) in (self.db)):
            self.register(s)
        else:
            self.username = name

        self._isFinished = True
        

    def register(self, s):
        s.send("\nUsername not found, please enter new name to register:".encode())
        self.username = s.recv(1024).decode()
        if self.db.get(self.username) == None:
            self.db[self.username] = {}

    def next(self):
        self.saveDB()

        if (self.isFinished()):
            return UserModeService(self.username)
        
        return LoginService()

    def isFinished(self):
        return self._isFinished

class LogoutService(Service):
    def __init__(self):
        super().__init__()

    def serve(self, s=None, username=None):
        msg = "Do you really want to quit? (Y/N)"
        s.send(msg.encode())

        res = s.recv(1024).decode()
        if (res == "Y"):
            self._isFinished = True
            s.send("__QUIT".encode())
        else:
            self._isFinished = False        
    
    def next(self):
        return UserModeService()