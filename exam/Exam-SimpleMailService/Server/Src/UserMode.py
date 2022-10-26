import Login
from Service import Service

class UserModeService(Service):
    def __init__(self, username=None):
        super().__init__()
        self.username = username
        self.factory = UserModeFactory()
    
    def serve(self, socket):
        self._isFinished = False
        # 1. send mail
        # 2. list inbox
        # 3. check new inbox
        # 4. logout
        socket.send( self.displayOptions().encode() )

        product = SendService()
        while True:
            cmd = socket.recv(1024).decode()
            product = self.factory.manufacture(cmd)
            
            if product == None:
                socket.send(self.displayOptions(True).encode())
                continue
            elif type(product) == Login.LogoutService:
                break

            product.serve(socket, self.username)

        self._isFinished = True
    
    def displayOptions(self, warning=False):
        msg = "="*10 + "\n"
        if warning:
            msg += "\nCommand not found please re-enter (1-3)\n" 
        msg += "Function list:\n1. send mail\n2. list inbox\n3. Logout\n\nPlease enter mode: "
        
        return msg

    def next(self):
        return Login.LogoutService()



class SendService(UserModeService):
    def __init__(self):
        super().__init__()
    
    def serve(self, socket, username):
        socket.send("\nEnter recipient name: ".encode())
        recipient = socket.recv(1024).decode()
    
        socket.send("\nEnter mail title: ".encode())
        title = socket.recv(1024).decode()

        socket.send("\nEnter content: ".encode())
        content = socket.recv(1024).decode()

        if recipient not in self.db:
            msg = "\nInvalid recipient name\n"
            msg += self.displayOptions()
            socket.send(msg.encode())
            return

        # timestamp, from, to, title, content
        import time
        t = time.time()

        content = {
            'from': username,
            'to': recipient,
            'timestamp': str(t),
            'title': title,
            'content': content
        }

        self.addToDB(content)
        socket.send(self.displayOptions().encode())


    def addToDB(self, content):
        if self.db[content['from']].get('send') == None:
            self.db[content['from']]['send'] = []
        if self.db[content['to']].get('recv') == None:
            self.db[content['to']]['recv'] = [] 
        
        self.db[content['from']]['send'].append(content)
        self.db[content['to']]['recv'].append(content)
        
        self.refreshDB()

class ListMailService(UserModeService):
    def __init__(self):
        super().__init__()

    def serve(self, socket, username):
        self.loadDB()

        if self.db[username].get('recv') == None:
            msg = "\nThere isn't any received mail.\n"
            msg += self.displayOptions()
            socket.send(msg.encode())
            return

        msg = "\n"
        for mail in self.db[username]['recv']:
            msg += str(mail) + "\n"

        msg += "\n" + "="*10 + self.displayOptions()
        socket.send(msg.encode())

class UserModeFactory:
    def manufacture(self, cmd):
        if (cmd == '1'):
            return SendService()
        elif (cmd == '2'):
            return ListMailService()
        elif (cmd == '3'):
            return Login.LogoutService()
        else:
            return None