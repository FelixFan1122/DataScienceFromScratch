from matplotlib import pyplot

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

pyplot.plot(years, gdp, color = 'green', marker = 'o', linestyle = 'solid')
pyplot.title("Nominal GDP")
pyplot.ylabel("Billions of $")
pyplot.show()