from collections import Counter
from matplotlib import pyplot

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

histogram = Counter(grade // 10 * 10 for grade in grades)
pyplot.bar(histogram.keys(), histogram.values())
pyplot.xlabel("Decile")
pyplot.ylabel("# of Students")
pyplot.title("Distribution of Exam 1 Grades")
pyplot.show()