import csv


# load file
f = open("../data/redlist.csv", "rb")
g = open("../data/southernOcean.csv", "rb")

# csv reader
redlist = csv.reader(f)
southernOcean = csv.reader(g)

# species_status_dict = { species in red list : status }
species_status_dict = {}
for line in redlist:
	species = line[1]
	status = line[14]
	if species == "tname":
		continue
	else:
		species_status_dict[species] = status

# append status to new column in southernOcean.csv
oceanPlusRedlist = []

# header
row0 = next(southernOcean)
row0.append("redstatus")
oceanPlusRedlist.append(row0)

for line in southernOcean:
	species = line[27]
	if species in species_status_dict.keys():
		line.append(species_status_dict[species])
		oceanPlusRedlist.append(line)
	else:
		line.append("")
		oceanPlusRedlist.append(line)

# write into new file
with open("../data/southernOcean_redlist.csv", "w+") as outfile:
	writer = csv.writer(outfile, lineterminator="\n")
	writer.writerows(oceanPlusRedlist)

outfile.close()
f.close()
g.close()