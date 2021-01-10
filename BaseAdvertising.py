class BaseAdvertiser:

    def __init__(self,id):
        self.id = id
    def describeMe(self):
        description = "this class is father of Ad and Advertiser classes. I am BaseAdvertising Class"
        return description
    def getClicks(self):
        return self.clicks
    def getViews(self):
        return self.views
    def incClicks(self):
        self.clicks = self.clicks + 1
    def incViews(self):
        self.views = self.views + 1
