#!/usr/bin/env python
from operator import itemgetter
import sys
current_year = 0
avg_temp = 0
year = 0
temp_counter=0
temp_dict={}
for line in sys.stdin:
    line = line.strip()
    year,temp=line.split()
    if current_year==year:
        temp_counter=int(temp_counter)+1
        avg_temp=float(avg_temp)+float(temp)
    else:
        if current_year:
            try:
                avg_temp=float(avg_temp)/float(temp_counter)
                temp_dict[current_year]=avg_temp
                print current_year,avg_temp
            except ZeroDivisionError:
                print 'divide zero'
        current_year=year
        temp_counter=1
        avg_temp=float(temp)
if current_year==year:
    avg_temp=float(avg_temp)/float(temp_counter)
    temp_dict[current_year]=avg_temp
    print current_year,avg_temp
sum_temp=0.0
for k,v in temp_dict.iteritems():
    sum_temp=sum_temp+float(v)
avg_tem=sum_temp/len(temp_dict)
print avg_tem
for k,v in temp_dict.iteritems():
    if float(v) > float(avg_tem):
        print '%s was hotter than normal' % (k)
    if float(v) < float(avg_tem):
        print '%s was cooler than normal' % (k)
