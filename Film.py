class Film:
    instance = None
    
    def __init__(self, title="", director="", year=0):
        if Film.instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.title = title
            self.director = director
            self.year = year
            self.rating = 0
            self.marks = 0
            Film.instance = self

    def rate(self, rating):
        if rating < 1:
            rating = 1
        elif rating > 10:
            rating = 10
        
        self.rating += rating
        self.marks += 1

    def getCurrentRating(self):
        if self.marks == 0:
            return 0
        else:
            return self.rating / self.marks

    @staticmethod
    def getInstance(title="", director="", year=0):
        if Film.instance is None:
            Film.instance = Film(title, director, year)
        return Film.instance


if __name__ == '__main__':
    film1 = Film.getInstance("Inception", "Christopher Nolan", 2010)
    
    film1.rate(8)
    film1.rate(9)
    film1.rate(10)
    film1.rate(12)  

    film2 = Film.getInstance()
    
    print(f"Current Rating of {film1.title}: {film1.getCurrentRating()}")
    
    print(film1 is film2)
