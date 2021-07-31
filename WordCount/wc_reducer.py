#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

word = None
current_word = None
current_count = 0

for line in sys.stdin:
    line= line.strip()

    kv_pair = line.split("\t", 1)

    word = kv_pair[0]
    #convert count(i.e. value) into integer
    try:
        count = int(kv_pair[1])
    except ValueError:
        #IF we cannot convert string to integer then
        #silently igonre.
        continue

    if word == current_word:
        current_count += count
    else:
        if current_word:
            print '%s\t%s' % (current_word,current_count)
        current_word = word
        current_count = count

#for last word
if current_word == word:
    print '%s\t%s' % (current_word,current_count)