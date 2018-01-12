# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 16:24:21 2017

@author: bmyers
"""
#Websites and example code I used to figure this out:
#http://www.pythonforbeginners.com/regex/regular-expressions-in-python
#https://stackoverflow.com/questions/23277268/parse-date-strings
#https://stackoverflow.com/questions/14441754/scatter-plot-of-dates-and-times
#http://www.u.arizona.edu/~erdmann/mse350/topics/plotting_with_pylab.html
#https://stackoverflow.com/questions/35839529/count-of-days-of-each-month-from-a-list-of-dates-python
#https://stackoverflow.com/questions/34py96518/python-using-a-dictionary-to-count-the-items-in-a-list
#https://stackoverflow.com/questions/3486121/how-to-plot-data-against-specific-dates-on-the-x-axis-using-matplotlib?rq=1
#https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date-in-python

import csv
import itertools
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import WeekdayLocator
import re
import datetime as dt
import dateutil
from dateutil.parser import *
from datetime import *
import pylab
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *
import collections
from collections import Counter

#-----------------------------------------------
#open file, create csv reader
#-----------------------------------------------
with open("received final.csv", "r", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    
#-----------------------------------------------
#create list to store dates
#-----------------------------------------------
    dates = []   
    
#-----------------------------------------------
#iterate through each row and field in the csv: the indentation of this section continues
#-----------------------------------------------
    for row in reader:
        for field in row:
            
#-----------------------------------------------
#change text dates to datetime objects
#-----------------------------------------------                       
            form_pattern = re.compile("^\d{1,2}\/\d{1,2}\/\d{4}") #look for this date pattern DD/MM/YYYY
            matches = re.findall(form_pattern, field) 
            if matches: #if matches is not empty
               dates.append(matches)
               
dates = list(itertools.chain(*dates)) #flatten list

x = 0 #incrementing the for loop below
datetimes = [] #empty list for datetime objects

for i in dates:  
    datetimes.append(datetime.strptime(str(dates[x]), '%m/%d/%Y')) #look for dates and convert
    x+=1
 
dateslist = Counter(datetimes)  #Counter counts the frequency of each date and put into dateslist dictionary in the format - datetime: key
#-----------------------------------------------
#plot received email dates for academic year
#-----------------------------------------------
x = [] #blank lists for axis
y = []

for freq in dateslist.values(): #get the dictionary values (frequency counts) for the y axis
    y.append(freq)
for dates in dateslist.keys(): #get the dictionary keys (the dates) for the x axis
    x.append(dates)    
    
fig = plt.figure(figsize=(10, 5), dpi=150) #can change size of plot
graph = fig.add_subplot(111)
graph.plot_date(x,y,'g')
ax = fig.gca()
ax.set_xticklabels(['October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June'], fontsize=8)
plt.ylabel('Number of emails')
plt.title('Email distribution through 2016-17 school year')
#plt.savefig('foo.png') #uncomment to save image to directory - can change filename
plt.show()


#-----------------------------------------------
#plot received email dates per quarter ticks per week
#-----------------------------------------------

#fall
fall = []

fall_start_date = datetime(2016, 9, 19, 0, 0)
fall_end_date = datetime(2017, 1, 8, 0, 0)

for i in datetimes:
    if i >= fall_start_date and i <= fall_end_date:
        fall.append(i)
        
fall = Counter(fall)

fallx = [] #blank lists for axis
fally = []

for freq in fall.values(): #get the dictionary values (frequency counts) for the y axis
    fally.append(freq)
for dates in fall.keys(): #get the dictionary keys (the dates) for the x axis
    fallx.append(dates)    
  
fig = plt.figure(figsize=(15, 5), dpi=150) #can change size of plot
graph = fig.add_subplot(111)
ax = fig.gca()
ax.set_xticklabels(['September\n15', 'September\n29', 'October\n13', 'October\n27', 'November\n10', 'November\n24', 'December\n8', 'December\n22', 'January\n5'], fontsize=8)
plt.yticks(np.arange(min(fally), max(fally)+1, 1.0))
graph.plot_date(fallx,fally,color='#3B9AED', linestyle='solid', marker='o')
plt.ylabel('Number of emails')
plt.title('Fall quarter 2016')

plt.show()

#winter
winter = []

winter_start_date = datetime(2017, 1, 9, 0, 0)
winter_end_date = datetime(2017, 4, 2, 0, 0)

for i in datetimes:
    if i >= winter_start_date and i <= winter_end_date:
        winter.append(i)
        
winter = Counter(winter)

winterx = [] #blank lists for axis
wintery = []

for freq in winter.values(): #get the dictionary values (frequency counts) for the y axis
    wintery.append(freq)
for dates in winter.keys(): #get the dictionary keys (the dates) for the x axis
    winterx.append(dates)    
  
fig = plt.figure(figsize=(10, 5), dpi=150) #can change size of plot
graph = fig.add_subplot(111)
ax = fig.gca()
ax.set_xticklabels(['January\n11', 'January\n25', 'February\n8', 'February\n22', 'March\n8', 'March\n22'], fontsize=8)
plt.yticks(np.arange(min(fally), max(fally)+1, 1.0))
graph.plot_date(winterx,wintery,color='#3B9AED', linestyle='solid', marker='o')
plt.ylabel('Number of emails')
plt.title('Winter quarter 2017')

plt.show()

#spring

spring = []

spring_start_date = datetime(2017, 4, 3, 0, 0)
spring_end_date = datetime(2017, 6, 17, 0, 0)

for i in datetimes:
    if i >= spring_start_date and i <= spring_end_date:
        spring.append(i)
        
spring = Counter(spring)

springx = [] #blank lists for axis
springy = []

for freq in spring.values(): #get the dictionary values (frequency counts) for the y axis
    springy.append(freq)
for dates in spring.keys(): #get the dictionary keys (the dates) for the x axis
    springx.append(dates)    
  
fig = plt.figure(figsize=(10, 5), dpi=150) #can change size of plot
graph = fig.add_subplot(111)
ax = fig.gca()
ax.set_xticklabels(['April\n2', 'April\n16', 'April\n30', 'May\n14', 'May\n28', 'June\n11'], fontsize=8)
plt.yticks(np.arange(min(fally), max(fally)+1, 1.0))
graph.plot_date(springx,springy,color='#3B9AED', linestyle='solid', marker='o')
plt.ylabel('Number of emails')
plt.title('Spring quarter 2017')

plt.show()


#-----------------------------------------------
#pie chart number of days in the week
#-----------------------------------------------

sundays = []
mondays = []
tuesdays=[]
wednesdays=[]
thursdays=[]
fridays=[]
saturdays=[]

for i in datetimes:
    if i.weekday() == 6:
        sundays.append(i)
    elif i.weekday() == 0:
        mondays.append(i)
    elif i.weekday() == 1:
        tuesdays.append(i)
    elif i.weekday() == 2:
        wednesdays.append(i)
    elif i.weekday() == 3:
        thursdays.append(i)
    elif i.weekday() == 4:
        fridays.append(i)
    elif i.weekday() == 5:
        saturdays.append(i)
        
sunday_counts = len(sundays)
monday_counts = len(mondays)
tuesday_counts = len(tuesdays)
wednesday_counts = len(wednesdays)
thursday_counts = len(thursdays)
friday_counts = len(fridays)
saturday_counts = len(saturdays)

#show pie chart
labels = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
counts = [sunday_counts, monday_counts, tuesday_counts, wednesday_counts, thursday_counts, friday_counts, saturday_counts]
sizes = [sunday_counts, monday_counts, tuesday_counts, wednesday_counts, thursday_counts, friday_counts, saturday_counts]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'coral', 'blue', 'orange']

plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140, pctdistance=0.8)
plt.axis('equal')
fig = plt.gcf()
fig.set_size_inches(6,6)
plt.suptitle('2016-2017 weekday distribution', fontsize=24)
plt.show()