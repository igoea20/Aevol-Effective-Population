import csv
from operator import itemgetter
from itertools import zip_longest

## This code takes in population and pheno files from Aevol
## It performs some needed post-processing so that the results
## can be graphed in R, using ggMuller.



generations = []
identities = []
pop = []
parents = []
strains = []

pre_sorted_pop = []
pre_sorted_pheno = []

inputPopFileName = input("Enter the population file name: ")
inputPhenoFileName = input("Enter the pheno file name: ")
outputPopFileName = input("Enter the output population file name: ")
outputPhenoFileName = input("Enter the output pheno file name: ")


with open(inputPopFileName,'r') as csvfile:
    c = csv.reader(csvfile, delimiter = ',')
    next(csvfile)
    for row in c:
        pre_sorted_pop.append([float(i) for i in row])

with open(inputPhenoFileName,'r') as csvfile:
    c = csv.reader(csvfile, delimiter = ',')
    next(csvfile)
    for row in c:
        pre_sorted_pheno.append([float(i) for i in row])

#sort them in order of generation
pre_sorted_pop.sort()
pre_sorted_pheno.sort()

#get them into individual list form for easier initialisation
for gen in pre_sorted_pop:
    generations.append(int(gen[0]))
    identities.append(int(gen[1]))
    pop.append(gen[2])

#check that all the we're only adding strains that are needed
for strain in pre_sorted_pheno:
    if(identities.count(int(strain[1]))!=0):
        parents.append(int(strain[0]))
        strains.append(int(strain[1]))


#initialise the first pheno types
generations.insert(0,generations[0])
identities.insert(0,int(parents[0]))
pop.insert(0,0)


#write to file
d = [generations, identities, pop]
export_data = zip_longest(*d, fillvalue = '')
with open(outputPopFileName, 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Generation", "Identity", "Population"))
      wr.writerows(export_data)
myfile.close()

d = [parents, strains]
export_data = zip_longest(*d, fillvalue = '')
with open(outputPhenoFileName, 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Parent", "Identity"))
      wr.writerows(export_data)
myfile.close()
