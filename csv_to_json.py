#!/usr/bin/env python

"""
Turn csv into json
"""

import csv
import json


# create the dict
data = {}

# Read in the data
with open("cleaned_final.txt", encoding = 'utf-8') as f:
    csv_reader = csv.DictReader(f)

    for i, row in enumerate(csv_reader):
        key = i
        data[i] = row

# Write to json
with open("cleaned_final_OE.json", 'w', encoding = 'utf-8') as f:
    f.write(json.dumps(data, indent = 4))
