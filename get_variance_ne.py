import csv
import numpy as np
from itertools import zip_longest


## Takes in the variance in progeny per generation, calculated
## using the Aevol output. Uses this to calculate the Variance
## Effective Population size at every generation.

def get_variance_eff_pop(variance_file, output_ne_file, pop_size):
        variance = []
        times = []

        with open(inputFileName,'r') as csvfile:
            c = csv.reader(csvfile, delimiter = ',')
            next(csvfile)
            for row in c:
                times.append(int(row[0]))
                variance.append(float(row[1]))

        ## get the effective population size using the formula described in
        ##  "A Caballero. Developments in the prediction of effective population size. Heredity,
        ## 73(6):657–679, 1994"

        ne_v = [int(inputPopSize-1)/(value) for value in variance if value != 0]

        #write variance effective population to file
        d = [times, ne_v]
        export_data = zip_longest(*d, fillvalue = '')
        with open(output_ne_file, 'w', encoding="ISO-8859-1", newline='') as myfile:
              wr = csv.writer(myfile)
              wr.writerow(("Generation", "Variance effective population"))
              wr.writerows(export_data)
        myfile.close()

input_variance_file = input("Enter the variance file name: ")
output_file = input("Enter the output file name: ")
population_size = input("Enter the size of the population: ")
get_variance_eff_pop(input_variance_file, output_file, population_size)
