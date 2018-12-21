from matplotlib import pyplot

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
oscars = [5, 11, 3, 8, 10]

pyplot.bar(movies, oscars)
pyplot.ylabel("# of Academy Awards")
pyplot.title("My Favoriate Movies")
pyplot.show()