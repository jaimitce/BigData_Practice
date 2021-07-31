#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

year = None
current_year = None
max_temp = -99999

for line in sys.stdin:

    line = line.strip()

    year, temperature = line.split("\t")

    try:
        year = int(year)
        temperature = int(temperature)
    except ValueError:
        continue

    if current_year == year:
        max_temp = max(max_temp, temperature)
    else:
        if current_year:
            print '%s\t%s' % (current_year,max_temp)
        max_temp = temperature
        current_year = year

if current_year == year:
    print '%s\t%s' % (year,max_temp)
