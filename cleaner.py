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
    line = line.replace('"', "")

    if '\t' in line:
        line = line[line.find('\t')+1:]         # Clip the verb form data
    processed = line.split(maxsplit=1)          # Split Ojibwe from raw English
    index = processed[1].rindex("(")            # Split off the conjugation feature
    processed[1:] = [processed[1][:index-1], processed[1][index:]]

    # clean up some punctuation
    processed[1] = processed[1].strip("'")
    processed[2] = processed[2].strip("()")

    intermediate.append(processed)

#DEBUG - display data after preprocessing
print("____INTER_____")
for line in intermediate[:20]:
    print(line)         

#DEBUG - pull out 'maacaa - to leave' examples 
maacaa = []
for line in intermediate:
    if "maacaa" in line[0] or "leav" in line[1]:
        maacaa.append(line)


#TODO: decide on english formatting
#test commit for linter





# final formatting
# fields = ["Southwestern Ojibwe", "English(raw)", "Conjugation", "English(formatted)" ]
fields = ["Southwestern Ojibwe", "English(raw)", "Conjugation"]

rows = intermediate     #TODO: change this to final

with open('cleaned.txt', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(rows)

#DEBUG - maacaa examples
with open('maacaa.txt', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(maacaa)