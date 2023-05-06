class DiscordImage:
    def __init__(self, link):
        self.link = link
        self.ratings = []

    def getURL(self) -> str:
        return str(self.link)

    def getRatings(self) -> str:
        return self.ratings