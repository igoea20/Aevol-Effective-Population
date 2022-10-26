import csv
import numpy as np
from itertools import zip_longest

## Gets the Coalescent Effective Population at every generation for
## a population. Uses the Time since Most Recent Common Ancestor, which
## is calculated from the Coalescence times outputted by Aevol.
def get_coalescence_eff_pop(tmrca_file, output_ne_file, pop_size):
    gens = []
    tmrca = []

    with open(tmrca_file,'r') as csvfile:
        c = csv.reader(csvfile, delimiter = ',')
        next(csvfile)
        for row in c:
            gens.append(float(row[0]))
            tmrca.append(float(row[1]))

    ## Calculate the coalescent effective population size per generation,
    ## adapted by myself from the formula for Diploids proposed by Wakely in his 2021 review.
    ## John Wakeley. Coalescent models. In Human Population Genomics, pages 3–30. Springer, 2021.
    ne_c = [value/(2 - 2/inputPopSize) for value in tmrca]

    #write coalescent effective population to file
    d = [gens_t, ne_c]
    export_data = zip_longest(*d, fillvalue = '')
    with open(output_ne_file, 'w', encoding="ISO-8859-1", newline='') as myfile:
          wr = csv.writer(myfile)
          wr.writerow(("Generation", "Coalescent effective population"))
          wr.writerows(export_data)
    myfile.close()

input_tmrca_file = input("Enter the tmrca file name: ")
output_file = input("Enter the output file name: ")
population_size = input("Enter the size of the population: ")
get_variance_eff_pop(input_tmrca_file, output_file, population_size)
