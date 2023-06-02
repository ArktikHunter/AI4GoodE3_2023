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
    #line = line.replace('"', "")

    if '\t' in line:
        line = line[line.find('\t')+1:]         # Clip the verb form data
    processed = line.split(maxsplit=1)          # Split Ojibwe from raw English
    index = processed[1].rindex("(")                                # Split off the conjugation feature
    processed[1:] = [processed[1][:index-1], processed[1][index:]]

    # clean up some punctuation
    processed[1] = processed[1].strip("'")
    processed[2] = processed[2].strip("()")

    intermediate.append(processed)

#DEBUG - display data after preprocessing
print("____INTER_____")
for line in intermediate[:10]:
    print(line)         



#TODO: decide on english formatting
final = []
for entry in intermediate:
    fin_entry = [a for a in entry]   # make a copy
    raw = entry[1]
    

    # get rid of current grammar tags
    if "(" in raw:
        start = raw.index("(")
        end = raw.index(")")

        fin_entry[1] = raw[:start-1] + raw[end+1:]
        raw = fin_entry[1]

    if "," in raw:     # need to duplicate this entry
        fin_entry.append(raw.replace("they", "").replace("s/he, ", "they(sing.)"))

        fin_entry2 = [a for a in entry]
        fin_entry2.append(raw.replace("s/he, ", "").replace("they", "they(plur.)"))

        final.append(fin_entry2)

    else:                   # else just swap one or the other
        if "s/he" in raw:    
            if "Indicative" in entry[2]: #sets "FLAG" for human to verify english grammar 
                fin_entry.append("FLAG" + raw.replace("s/he", "they(sing.)"))   
            else:   # no grammar issues in the other tenses
                fin_entry.append(raw.replace("s/he", "they(sing.)"))   

        elif "they" in raw:
            fin_entry.append(raw.replace("they", "they(plur.)"))

    if len(fin_entry) != 4:
        fin_entry.append(raw)
        
    final.append(fin_entry)


#DEBUG - display data after preprocessing
print("____FINAL_____")
for line in final[:10]:
    print(line)  

#DEBUG - pull out 'maacaa - to leave' examples 
maacaa = []
for line in final:
    if "maacaa" in line[0] or "leav" in line[1]:
        maacaa.append(line)

        






# final formatting
fields = ["Southwestern Ojibwe", "English(raw)", "Conjugation", "English(formatted)" ]
#fields = ["Southwestern Ojibwe", "English(raw)", "Conjugation"]

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