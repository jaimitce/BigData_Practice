#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:

    line = line.strip()
    datas = line.split(",")

    _date = datas[0]
    _year = _date.split("-")[-1]
    temperature = datas[2] 

    key_year   = _year
    value_temp = temperature

    print '%s\t%s' % (key_year,value_temp)
