#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


for line in sys.stdin:
    line = line.strip()

    words = line.split(" ")

    for word in words:
        key = word
        value = 1

        print '%s\t%s' % (key,value)