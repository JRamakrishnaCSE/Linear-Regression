import math as m
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
	predictions = []
	a,b = coeff(train)
	for row in test:
		yhat = b + a * row[0]
		predictions.append(yhat)
	return predictions


dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
print coeff(dataset)
print simple_linear_regression(dataset,dataset)
