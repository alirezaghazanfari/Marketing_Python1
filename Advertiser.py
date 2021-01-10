import BaseAdvertising
class Advertiser(BaseAdvertising.BaseAdvertiser):

    advertisers = []
    def _init_(self,id,name):
        self.id = id
        self.name = name
        Advertiser.advertisers.__add__(self)
    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName
    def help(self):
        message = "this is help message"
        return message

    def describeMe(self):
        description = "this class is advertiser"
        return description
    @staticmethod
    def getTotalClicks():
        totalClickNumber = 0
        for i in Advertiser.advertisers:
            totalClickNumber = totalClickNumber + i.getClicks
        return totalClickNumber

