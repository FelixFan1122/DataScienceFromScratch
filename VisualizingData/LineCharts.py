from matplotlib import pyplot

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]

xs = range(len(variance))
pyplot.plot(xs, variance, 'g-', label = 'variance')
pyplot.plot(xs, bias_squared, 'r-.', label = 'bias^2')
pyplot.plot(xs, total_error, 'b:', label = 'total error')
pyplot.legend(loc = 9)
pyplot.xlabel("model complexity")
pyplot.title("The Bias-Variance Tradeoff")
pyplot.show()