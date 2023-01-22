class Recipe:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.ingredients = kwargs["ingredients"]
        self.steps = kwargs["steps"]
        self.rating = kwargs["rating"]

    def get_rating(self):
        return sum(self.rating)

    def __lt__(self, other):
        return self.get_rating() < other.get_rating()

    def __eq__(self, other):
        return self.get_rating() < other.get_rating()
