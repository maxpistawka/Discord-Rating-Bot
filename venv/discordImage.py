class DiscordImage:
    def __init__(self, link):
        self.link = link
        self.ratings = []

    def getURL(self) -> str:
        return str(self.link)

    def getRatings(self) -> str:
        return self.ratings

    def addRating(self, rating):
        self.ratings.append(rating)


class Rating:
    def __init__(self, userName, rating):
        self.userName = userName
        self.rating = rating

    def __str__(self):
        return self.userName + " " + str(self.rating)
