class BaseAdvertiser:

    def __init__(self,views=0,clicks=0):
        self.views = views
        self.clicks = clicks




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
