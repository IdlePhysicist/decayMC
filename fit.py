#
#   FIT.PY VERSION III
#   Eoghan Conlon O'Neill 2016
#
#   Script to fit a curve to a txt of data
#   Now can fit data from any directory
#   new fitting functions
#

from pylab import *
from scipy.optimize import curve_fit

def pow2(x, a, b, c):
	return	(a*pow(2,(-x/b))) + c
    #return (a*exp(-x*b)) + c

def analyticalDau1(x, a, b, c, d):
    #return  a*(1-pow(2,(-x/b))*(pow(2,(-x/c))) + d)
    return	a*(1-exp(-x/b))*(exp(-x/c)) + d

def analyticalDau2(x, a, b, c, d):
    return a*(1-exp(-x/a) + (exp(-x/a)*exp(-x/b)) - exp(-x/b))*exp(-x/c) + d

address = "decayP.txt"
input = loadtxt(address, dtype='float_', skiprows=1)
x = input[:,0]
y = input[:,1]
y2 = input[:,2]
y3 = input[:,3]

y2_maxVal = max(y2)
print y2_maxVal #270
x2_y2_max = input[270:,0]
y2_max = input[270:,2]

#print x2_y2_max, "\n", y2_max, "\n"

y3_maxVal = max(y3)
print y3_maxVal #1045
x3_y3_max = input[1045:,0]
y3_max = input[1045:,3]

parameter, covariance_matrix = curve_fit(pow2, x, y)
print "Data 1 Fit Parameters\n", "a =", parameter[0], "+/-", covariance_matrix[0,0]**0.5
print                            "b =", parameter[1], "+/-", covariance_matrix[1,1]**0.5
print                            "c =", parameter[2], "+/-", covariance_matrix[2,2]**0.5, "\n"

parameter2, covariance_matrix2 = curve_fit(analyticalDau1, x, y2)
print "Data 2 Fit Parameters\n", "a =", parameter2[0], "+/-", covariance_matrix2[0,0]**0.5
print                            "b =", parameter2[1], "+/-", covariance_matrix2[1,1]**0.5
print                            "c =", parameter2[2], "+/-", covariance_matrix2[2,2]**0.5
print                            "d =", parameter2[3], "+/-", covariance_matrix2[3,3]**0.5, "\n"

parameter3, covariance_matrix3 = curve_fit(analyticalDau2, x, y3)
print "Data 3 Fit Parameters\n", "a =", parameter3[0], "+/-", covariance_matrix3[0,0]**0.5
print                            "b =", parameter3[1], "+/-", covariance_matrix3[1,1]**0.5
print                            "c =", parameter3[2], "+/-", covariance_matrix3[2,2]**0.5
print                            "d =", parameter3[3], "+/-", covariance_matrix3[3,3]**0.5, "\n"

#   Plotting
figure(figsize=(12,8))
rc('font', family='sans')
rc('xtick', labelsize='small')
rc('ytick', labelsize='small')

plot(x, y, color='Blue', label='Data 1')
plot(x, pow2(x, parameter[0], parameter[1], parameter[2]), 'b--', label='Data 1 Fit')

plot(x, y2, color='Red', label='Data 2')
plot(x, analyticalDau1(x, parameter2[0], parameter2[1], parameter2[2], parameter2[3]), 'r--', label='Data 2 Fit')

plot(x, y3, color='Green', label='Data 3')
#plot(x, analyticalDau2(x, parameter3[0], parameter3[1], parameter3[2], parameter3[3]), 'g--', label='Data 3 Fit')

#print log(2)/parameter[1]

#x_title = raw_input('X units: ')
xlabel("X")
#y_title = raw_input('Y units: ')
ylabel("Y")
#yscale('log')
ylim(0,max(y))
legend(loc='upper right')
savefig("Fit Plot.png")
#show() # Uncomment this to see plot as it's produced
