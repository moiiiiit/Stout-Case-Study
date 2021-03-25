import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("casestudy.csv")
# FOR EACH YEAR
years = df.year.unique()
dfInYears = []
for i in years:
    dfInYears.append(df[df.year==i])

# •	Total revenue for the current year
totalRevenue=[]
for i in dfInYears:
    totalRevenue.append(i['net_revenue'].sum())
print(totalRevenue)

# •	New Customers
newCustomers = []
for i in range(len(dfInYears)-1):
    x = dfInYears[i+1]['customer_email']
    y = dfInYears[i]['customer_email']
    z = x[~x.isin(y)]
    newCustomers.append(z)
print(newCustomers)

# •	Lost Customers
lostCustomers = []
for i in range(len(dfInYears)-1):
    x = dfInYears[i]['customer_email']
    y = dfInYears[i+1]['customer_email']
    z = x[~x.isin(y)]
    lostCustomers.append(z)
print(lostCustomers)

# •	Total Customers Current Year
totalCustomers = []
for i in dfInYears:
    totalCustomers.append(len(pd.unique(i['customer_email'])))
print(totalCustomers)

# •	Total Customers Previous Year
totalCustomersPrevious = [0]
for i in totalCustomers:
    totalCustomersPrevious.append(i)
totalCustomersPrevious = totalCustomersPrevious[0:-1]
print(totalCustomersPrevious)

# •	New Customer Revenue e.g. new customers not present in previous year only
# •	Existing Customer Growth, Revenue of existing customers for current year – Revenue of existing customers from existing year
# •	Revenue lost from attrition
# •	Existing Customer Revenue Current Year
# •	Existing Customer Revenue Prior Year


