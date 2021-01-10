import BaseAdvertising
class Advertiser(BaseAdvertising.BaseAdvertiser):


    def __init__(self,id,name,views = 0 , clicks = 0):
        super().__init__(views,clicks)
        self.id = id
        self.name = name
    totalClciks = 0
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName
    @staticmethod
    def help():
        message = "this is help message"
        return message

    def describeMe(self):
        description = "this class is advertiser"
        return description

    def incClicks(self):
        super().incClicks()
        Advertiser.totalClciks+=1

    @staticmethod
    def getTotalClicks():
        return Advertiser.totalClciks

