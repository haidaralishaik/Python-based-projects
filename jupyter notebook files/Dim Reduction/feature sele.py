# -*- coding: utf-8 -*-
"""
Created on Sun May 26 07:39:06 2019

@author: ganapathi raju
"""




print('---------chisquare--------')
from scipy.stats import chisquare
a=chisquare([16, 18, 16, 14, 12, 12])
print(a)


print('---------SelectKBest--------')

from sklearn.datasets import load_digits
from sklearn.feature_selection import SelectKBest, chi2
X, y = load_digits(return_X_y=True)
print(X.shape)
X_new = SelectKBest(chi2, k=20).fit_transform(X, y)
print(X_new.shape)


print('---------SelectPercentile--------')



from sklearn.datasets import load_digits
from sklearn.feature_selection import SelectPercentile, chi2
X, y = load_digits(return_X_y=True)
print(X.shape)

X_new = SelectPercentile(chi2, percentile=10).fit_transform(X, y)
print(X_new.shape)



print('---------GenericUnivariateSelect--------')



from sklearn.datasets import load_breast_cancer
from sklearn.feature_selection import GenericUnivariateSelect, chi2
X, y = load_breast_cancer(return_X_y=True)
print(X.shape)

transformer = GenericUnivariateSelect(chi2, 'k_best', param=20)
X_new = transformer.fit_transform(X, y)
print(X_new.shape)