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

# Minor preprocessing
intermediate = []
for line in data:
    if '\t' in line:
        line = line[line.find('\t')+1:]         # Clip the verb form data
    intermediate.append(line.split(maxsplit=1)) # Split Ojibwe from raw English

#DEBUG - display data after preprocessing
print("____INTER_____")
for line in intermediate[:10]:
    print(line)         


#TODO: decide on english formatting



# final formatting
fields = ["Southwestern Ojibwe", "English(raw)", "English(formatted)" ]
