#!/usr/bin/env python
# coding: utf-8

## Age Calculator using Python

def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)

# Format: y=year m=month d=day    
ageCalculator(2009 , 10, 19)
