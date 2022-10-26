from genericpath import isfile
import pickle
import os

class Service:
    def __init__(self):
        self.msg = ""
        self._isFinished = False
        
        self._script_path = os.path.abspath(os.path.dirname(__file__))
        self._db_path = os.path.join(self._script_path, "../Data/server.db.pickle")
        self.db = self.loadDB()

        self.username = None

    def serve(self):
        None

    def loadDB(self):
        if not os.path.isfile(self._db_path):
            self.db = {}
            self.saveDB()
        
        with open(self._db_path, "rb") as f:
            self.db = pickle.load(f)
        
        return self.db

    def saveDB(self):
        with open (self._db_path, "wb") as f:
            pickle.dump(self.db, f)

    def refreshDB(self):
        self.saveDB()
        self.loadDB()

    def isFinished(self):
        return self._isFinished
