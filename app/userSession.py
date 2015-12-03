# -*- coding: utf-8 -*-
class UserSession():
    def __init__(self, userID, userName):
        self.userID = userID
        self.userName = userName

    def toDict(self):
        return {"userName": self.userName, "userID": self.userID}