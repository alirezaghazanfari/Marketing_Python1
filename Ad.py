import BaseAdvertising


class Ad(BaseAdvertising.BaseAdvertiser):
    def __init__(self, id, title, img_url, link, advertiser):
        super().__init__(id)
        self.title = title
        self.img_url = img_url
        self.link = link
        self.advertiser = advertiser

    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title

    def get_img_url(self):
        return self.img_url

    def set_img_url(self, new_url):
        self.img_url = new_url

    def get_link(self):
        return self.link

    def set_link(self, new_link):
        self.link = new_link

    def get_advertiser(self):
        return self.advertiser

    def set_advertiser(self, new_advertiser):
        self.advertiser = new_advertiser

    def incClicks(self):
        super().incClicks()
        self.advertiser.incClicks()

    def incViews(self):
        super().incViews()
        self.advertiser.incViews()

    def describeMe(self):
        message = "this is class Ad"
        return message
