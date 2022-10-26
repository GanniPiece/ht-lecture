from Login import *
from Service import Service

class InteractiveService(Service):
    def __init__(self):
        super().__init__()

        self.service = LoginService()
        self.socket = None
    
    def serve(self, socket):
        self.service = LoginService()
        self.socket = socket

        while (not self.isFinished()):
            self.service.serve(socket)

        self.socket.close()
        
    def isFinished(self):
        if (self.service.isFinished() and type(self.service) != LogoutService) or \
           (not self.service.isFinished() and type(self.service) == LogoutService):
            self.service = self.service.next()            

        if self.service.isFinished() and type(self.service) == LogoutService:
            return True

        return False