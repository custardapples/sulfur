import csv
pathhits_aprA_Mags = set()
with open ('SR_pathhits_strong.csv', newline='') as Pathhits:
    reader = csv.reader(Pathhits , delimiter = ',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if row[23] == "\"aprA\"":
            full_MAG_name = row[11]
            pathhits = full_MAG_name[1:5]
            pathhits_aprA_Mags.add(pathhits)
print("MAGs with aprA in Pathhits:")
print(pathhits_aprA_Mags)
print("The length of this list is", len(pathhits_aprA_Mags))

dram_Mags_aprA = set()
with open ('metabolism_summary.csv', newline='') as DRAM:
    reader = csv.reader(DRAM, delimiter = ',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for i, row in enumerate(reader): 
        if i == 0:
            column_labels = row
        if i == 675:
            for j,entry in enumerate(row):
             if entry != "0": 
                MAG_position = j
                dram = column_labels[j][0:4]
                dram_Mags_aprA.add(dram)
print("MAGs with genes for aprA in DRAM: ", dram_Mags_aprA)
print("The length of this list is", len(dram_Mags_aprA))

print("overlapping aprA mags are:")
overlapping_aprA_MAGs = set (pathhits_aprA_Mags) & set (dram_Mags_aprA)
print("The number of overlapping MAGs:", len(overlapping_aprA_MAGs))

dram_Mags_aprB = set()
with open ('metabolism_summary.csv', newline='') as DRAM:
    reader = csv.reader(DRAM, delimiter = ',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for i, row in enumerate(reader): 
        if i == 0:
            column_labels = row
        if i == 676:
            for j,entry in enumerate(row):
             if entry != "0": 
                MAG_position = j
                dram = column_labels[j][0:4]
                dram_Mags_aprB.add(dram)
print("MAGs with genes for aprB in DRAM: ")
print(dram_Mags_aprB) 
print("The length of this list is", len(dram_Mags_aprB))

pathhits_aprB_Mags = set()
with open ('SR_pathhits_strong.csv', newline='') as Pathhits:
    reader = csv.reader(Pathhits , delimiter = ',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if row[23] == "\"aprB\"":
            full_MAG_name = row[11]
            pathhits = full_MAG_name[1:5]
            pathhits_aprB_Mags.add(pathhits)
print("MAGs with aprB in Pathhits:")
print(pathhits_aprB_Mags)
print("The length of this list is", len(pathhits_aprB_Mags))

print("overlapping aprB mags are:")
overlapping_aprB_MAGs = set (pathhits_aprB_Mags) & set (dram_Mags_aprB)
print("The number of overlapping MAGs:", len(overlapping_aprB_MAGs))

dram_Mags_sat1 = set()
with open ('metabolism_summary.csv', newline='') as DRAM:
    reader = csv.reader(DRAM, delimiter = ',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for i, row in enumerate(reader): 
        if i == 0:
            column_labels = row
        if i == 677:
            for j,entry in enumerate(row):
             if entry != "0": 
                MAG_position = j
                dram = column_labels[j][0:4]
                dram_Mags_sat1.add(dram)
print("MAGs with genes for sat subunit 1 in DRAM: ")
print(dram_Mags_sat1) 
print("The length of this list is", len(dram_Mags_sat1))

dram_Mags_sat2 = set()
with open ('metabolism_summary.csv', newline='') as DRAM:
    reader = csv.reader(DRAM, delimiter = ',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for i, row in enumerate(reader): 
        if i == 0:
            column_labels = row
        if i == 678:
            for j,entry in enumerate(row):
             if entry != "0": 
                MAG_position = j
                dram = column_labels[j][0:4]
                dram_Mags_sat2.add(dram)
print("MAGs with genes for sat subunit 2 in DRAM: ")
print(dram_Mags_sat2) 
print("The length of this list is", len(dram_Mags_sat2))

dram_Mags_sat = set()
with open ('metabolism_summary.csv', newline='') as DRAM:
    reader = csv.reader(DRAM, delimiter = ',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for i, row in enumerate(reader): 
        if i == 0:
            column_labels = row
        if i == 679:
            for j,entry in enumerate(row):
             if entry != "0": 
                MAG_position = j
                dram = column_labels[j][0:4]
                dram_Mags_sat.add(dram)
print("MAGs with genes for sat (general) in DRAM: ")
print(dram_Mags_sat) 
print("The length of this list is", len(dram_Mags_sat))

pathhits_sat_Mags = set()
with open ('SR_pathhits_strong.csv', newline='') as Pathhits:
    reader = csv.reader(Pathhits , delimiter = ',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if row[23] == "\"sat\"":
            full_MAG_name = row[11]
            pathhits = full_MAG_name[1:5]
            pathhits_sat_Mags.add(pathhits)
print("MAGs with sat in Pathhits:")
print(pathhits_sat_Mags)
print("The length of this list is", len(pathhits_sat_Mags))

print("overlapping sat mags are:")
overlapping_sat_MAGs = set (pathhits_sat_Mags) & set (dram_Mags_sat)
print("The number of overlapping MAGs:", len(overlapping_sat_MAGs))

dram_Mags_dsrA = set()
with open ('metabolism_summary.csv', newline='') as DRAM:
    reader = csv.reader(DRAM, delimiter = ',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for i, row in enumerate(reader): 
        if i == 0:
            column_labels = row
        if i == 680:
            for j,entry in enumerate(row):
             if entry != "0": 
                MAG_position = j
                dram = column_labels[j][0:4]
                dram_Mags_dsrA.add(dram)
print("MAGs with genes for dsrA in DRAM: ")
print(dram_Mags_dsrA) 
print("The length of this list is", len(dram_Mags_dsrA))

pathhits_dsrA_Mags = set()
with open ('SR_pathhits_strong.csv', newline='') as Pathhits:
    reader = csv.reader(Pathhits , delimiter = ',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if row[23] == "\"dsrA\"":
            full_MAG_name = row[11]
            pathhits = full_MAG_name[1:5]
            pathhits_dsrA_Mags.add(pathhits)
print("MAGs with dsrA in Pathhits:")
print(pathhits_dsrA_Mags)
print("The length of this list is", len(pathhits_dsrA_Mags))

print("overlapping sat mags are:")
overlapping_dsrA_MAGs = set (pathhits_dsrA_Mags) & set (dram_Mags_dsrA)
print("The number of overlapping MAGs:", len(overlapping_dsrA_MAGs))

dram_Mags_dsrB = set()
with open ('metabolism_summary.csv', newline='') as DRAM:
    reader = csv.reader(DRAM, delimiter = ',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for i, row in enumerate(reader): 
        if i == 0:
            column_labels = row
        if i == 681:
            for j,entry in enumerate(row):
             if entry != "0": 
                MAG_position = j
                dram = column_labels[j][0:4]
                dram_Mags_dsrB.add(dram)
print("MAGs with genes for dsrB in DRAM: ")
print(dram_Mags_dsrB) 
print("The length of this list is", len(dram_Mags_dsrB))

pathhits_dsrB_Mags = set()
with open ('SR_pathhits_strong.csv', newline='') as Pathhits:
    reader = csv.reader(Pathhits , delimiter = ',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if row[23] == "\"dsrB\"":
            full_MAG_name = row[11]
            pathhits = full_MAG_name[1:5]
            pathhits_dsrB_Mags.add(pathhits)
print("MAGs with dsrB in Pathhits:")
print(pathhits_dsrB_Mags)
print("The length of this list is", len(pathhits_dsrB_Mags))

print("overlapping dsrB mags are:")
overlapping_dsrB_MAGs = set (pathhits_dsrB_Mags) & set (dram_Mags_dsrB)
print("The number of overlapping MAGs:", len(overlapping_dsrB_MAGs))

pathhits_dsrC_Mags = set()
with open ('SR_pathhits_strong.csv', newline='') as Pathhits:
    reader = csv.reader(Pathhits , delimiter = ',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if row[23] == "\"dsrC\"":
            full_MAG_name = row[11]
            pathhits = full_MAG_name[1:5]
            pathhits_dsrC_Mags.add(pathhits)
print("MAGs with dsrC in Pathhits:")
print(pathhits_dsrC_Mags)

