import pandas as pd 
from matplotlib import pyplot as plt
whole_data = pd.read_csv("C:/Users/Ahmad Kabeer/Downloads/6087_8975_bundle_archive/weatherHistory.csv")
temp_data = whole_data['Temperature (C)']

# #Creatung Histogram
# =============================================================================
# #In the histogram, the data is divided into a pre-specified number of groups called bins. 
# #The data is then sorted into each bin and the count of the number of observations in each bin is retained.
# #The plot shows the bins across the x-axis maintaining their ordinal relationship, and the count 
# #in each bin on the y-axis.
# #A sample of data has a Gaussian distribution of the histogram plot, showing the familiar bell shape.
# =============================================================================
plt.hist(temp_data)
plt.show()

# #q-q plot
# =============================================================================
# This plot generates its own sample of the idealized distribution that we are comparing with, in this case 
# the Gaussian distribution. The idealized samples are divided into groups (e.g. 5), called quantiles. 
# Each data point in the sample is paired with a similar member from the idealized distribution at the 
# same cumulative distribution.
# The resulting points are plotted as a scatter plot with the idealized value on the x-axis and the data 
# sample on the y-axis.
# A perfect match for the distribution will be shown by a line of dots on a 45-degree angle from the bottom 
# left of the plot to the top right. Often a line is drawn on the plot to help make this expectation clear. 
# Deviations by the dots from the line shows a deviation from the expected distribution.
# =============================================================================
import scipy.stats as stats
stats.probplot(temp_data,dist='norm', plot=plt)
plt.show()

#Shapiro Wilk test
# =============================================================================
# The Shapiro-Wilk test evaluates a data sample and quantifies how likely it is that the data was 
# drawn from a Gaussian distribution, named for Samuel Shapiro and Martin Wilk.
# In practice, the Shapiro-Wilk test is believed to be a reliable test of normality, although there 
# is some suggestion that the test may be suitable for smaller samples of data, e.g. thousands of 
# observations or fewer.
# The shapiro() SciPy function will calculate the Shapiro-Wilk on a given dataset. 
# The function returns both the W-statistic calculated by the test and the p-value.
# =============================================================================
from scipy.stats import shapiro
stat_para, p_value = shapiro(temp_data)
print('P-value of Shapiro wilk test = '+ str(p_value))
if p_value > 0.05:
    print('Shapiro-Wilk test:-Data looks gaussian')
else:
    print('Shapiro-Wilk test:- Data does not look normal')
    
#Skew & Kurtosis test
# =============================================================================
# Skew is a quantification of how much a distribution is pushed left or right, a measure of 
# asymmetry in the distribution.
# Kurtosis quantifies how much of the distribution is in the tail. It is a simple and 
# commonly used statistical test for normality.
# =============================================================================
from scipy.stats import normaltest
stat_snk, p_snk = normaltest(temp_data)
print('P-value of Skew and Kurtosis test = '+ str(p_snk))
if p_snk > 0.05:
	print('Skew and kurtosis test:- Data looks Gaussian')
else:
	print('Skew and kurtosis test:- Data does not look Gaussian')

#Anderson-Darling Test
# =============================================================================
# Anderson-Darling Test is a statistical test that can be used to evaluate whether a data 
# sample comes from one of among many known data samples, named for Theodore Anderson and Donald Darling.
# It can be used to check whether a data sample is normal?
# A feature of the Anderson-Darling test is that it returns a list of critical values rather than a 
# single p-value. This can provide the basis for a more thorough interpretation of the result.
# from scipy.stats import anderson
# =============================================================================
result = anderson(temp_data)
print('Statistics result of Anderson darling test = '+ str(result.statistic))
for i in range(len(result.critical_values)):
	sl, cv = result.significance_level[i], result.critical_values[i]
	if result.statistic < result.critical_values[i]:
		print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
	else:
		print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))
