#!/usr/bin/env python

"""
Cleans the data
"""

import csv

# Read in the data
with open("rawdata.txt") as f:
    data = [ line.strip() for line in f.readlines()]

#DEBUG - display raw data
print("____RAW_____")
for line in data[:10]:
    print(line)         

# Clip the verb form data
intermediate = []
for line in data:
    if '\t' in line:
        line = line[line.find('\t')+1:]   
    intermediate.append(line)

#DEBUG - display data after clipping
print("____INTER_____")
for line in intermediate[:10]:
    print(line)         


#TODO: decide on english formatting



# final formatting
fields = ["Southwestern Ojibwe", "English(raw)", "English(formatted)" ]
