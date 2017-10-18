import math as m
import matplotlib.pyplot as p
def mean(values):
	"""Mean of the iterable."""
	return (sum(values)/float(len(values)))

def variance(values,mean):
	"""Variance of the iterable."""
	return sum([(x-mean)**2 for x in values])

def covariance(xvalues,xmean,yvalues,ymean):
	"""Covariance of the two iterables"""	
	cov=0.0
	for i in range(len(xvalues)):
		cov+=(xvalues[i]-xmean)*(yvalues[i]-ymean)
	return cov

def coeff(dataset):
	"""This function calculates the values of the coefficients a,b which will further help in prediction of the values"""
	x=[r[0] for r in dataset]
	y=[r[1] for r in dataset]
	xmean,ymean=mean(x),mean(y)
	b = covariance(x,xmean,y,ymean)/variance(x,xmean)
	a = ymean-b*xmean
	return [a,b]

	
def simple_linear_regression(train, test):
	"""This is where we are predicting the b value based on the a values, train set builds
the model(calculates the coefficients) and the prediction is done on the test set."""
	predictions = []
	a,b = coeff(train)
	for row in test:
		yhat = b + a * row
		predictions.append(yhat)
	return predictions

def test_set(dataset):
	"""convert the dataset into test set"""
	test=[row[0] for row in dataset]
	return test

dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
x=[r[0] for r in dataset]
y=[r[1] for r in dataset]
print coeff(dataset)
test = test_set(dataset)
a=simple_linear_regression(dataset,test)
# p.plot(x,y)
print a
p.plot(x,y)
p.show()
