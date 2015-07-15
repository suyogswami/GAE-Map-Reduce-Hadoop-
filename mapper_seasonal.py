#!/usr/bin/env python
from operator import itemgetter
import sys
current_year = 0
avg_temp = 0
year = 0
temp_counter=0
temp_dict={}
current_season=None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    year,season,temp=line.split()
    if current_year==year and current_season==season:
        temp_counter=int(temp_counter)+1
        avg_temp=float(avg_temp)+float(temp)
        #print temp_counter
    else:
        if current_year and current_season:
            try:
                avg_temp=float(avg_temp)/float(temp_counter)
                temp_dict[current_year+" "+current_season]=avg_temp
                print '%s\t%s: \t%s' % (current_year,current_season,avg_temp)

            except ZeroDivisionError:
                print 'divide zero'
        temp_counter=0
        current_year=year
        current_season=season
        avg_temp=float(avg_temp)+float(temp)

if current_year==year and current_season==season:
    avg_temp=float(avg_temp)/float(temp_counter)
    temp_dict[current_year+" "+current_season]=avg_temp
    print '%s\t%s: \t%s' % (current_year,current_season,avg_temp)

sum_temp_win=0.0
sum_temp_summ=0.0
sum_temp_spr=0.0
sum_temp_fall=0.0
i=0
j=0
m=0
l=0
print temp_dict

for k,v in temp_dict.items():
    if 'Winter:' in k:
        i=i+1
        sum_temp_win=sum_temp_win+float(v)
    if 'Spring:' in k:
        j=j+1
        sum_temp_spr=sum_temp_spr+float(v)
    if 'Summer:' in k:
        m=m+1
        sum_temp_summ=sum_temp_summ+float(v)
    if 'Fall:' in k:
        l=l+1
        sum_temp_fall=sum_temp_fall+float(v)

avg_tem_win=float(sum_temp_win)/(i)
avg_tem_spr=float(sum_temp_spr)/(j)
avg_tem_summ=float(sum_temp_summ)/(m)
avg_tem_fall=float(sum_temp_fall)/(l)
#print avg_tem
for k,v in temp_dict.items():
    if 'Winter:' in k:
        if float(v) > float(avg_tem_win):
            print '%s was hotter than normal' % (k)
        if float(v) < float(avg_tem_win):
            print '%s was cooler than normal' % (k)
    if 'Spring:' in k:
        if float(v) > float(avg_tem_spr):
            print '%s was hotter than normal' % (k)
        if float(v) < float(avg_tem_spr):
            print '%s was cooler than normal' % (k)
    if 'Summer:' in k:
        if float(v) > float(avg_tem_summ):
            print '%s was hotter than normal' % (k)
