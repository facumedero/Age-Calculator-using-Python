#!/usr/bin/env python
# coding: utf-8

import argparse
import datetime

## Age Calculator using Python
print("Ingrese su año, mes y dia de nacimiento, en ese orden y separados por un espacio. Por ejemplo: 2022 12 18")
def ageCalculator(y, m, d):
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)

# Define the command line arguments
parser = argparse.ArgumentParser(description='Age Calculator using Python')
parser.add_argument('year', type=int, help='the year of birth')
parser.add_argument('month', type=int, help='the month of birth')
parser.add_argument('day', type=int, help='the day of birth')

# Parse the command line arguments
args = parser.parse_args()
year = args.year
month = args.month
day = args.day

# Calculate and print the age
ageCalculator(year, month, day)
