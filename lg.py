import math as m
import matplotlib.pyplot as p
import csv
import operator as o
import math as m


def csvread(a):
	"""This is to read any dataset from a csv file"""
	with open(a,'rb') as f:
		row = csv.reader(f,delimiter='\t')				# set whatever the delimiter you want(',' or '\t')
		l = lambda row : [map(float,x) for x in row]
		return l(row)

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
		y = b + a * row
		predictions.append(y)
	return predictions

def test_set(dataset):
	"""convert the dataset into test set"""
	test=[row[0] for row in dataset]
	return test

def plot_act_vs_pre(x,y1,y2):
	p.scatter(x,y1)
	p.plot(x,y2)
	p.show()

def rmse(y1,y2):
	a=map(o.__sub__,y2,y1)
	a=[x**2 for x in a]
	a=sum(a)/len(a)
	a=m.sqrt(a)
	return a

def main():
	"""This is the starting point of the program. \nJust put the desired filename below \nBy default it is 1.csv"""
	file_name='1.csv'
	dataset=csvread(file_name)
	test=test_set(dataset)				# To check using the same dataset,for user defined values use below line(uncommented)

	# test=[5,6,7]							# can give external testset to predict y values for, just comment out above line

	predictions = simple_linear_regression(dataset,test)

	x=[x[0] for x in dataset]
	y1=[y[1] for y in dataset]
	y2=predictions
	plot_act_vs_pre(x,y1,y2)

	print "The predicted values are :\n"
	for i in predictions:
		print i
	print "\nThe RMS Error is :",rmse(y1,y2)
	 
main()

