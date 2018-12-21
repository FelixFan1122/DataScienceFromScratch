from matplotlib import pyplot

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]

pyplot.scatter(friends, minutes)
pyplot.title("Daily Minutes vs. Number of Friends")
pyplot.xlabel("# of friends")
pyplot.ylabel("daily minutes spent on the site")
pyplot.show()