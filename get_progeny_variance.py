import csv
import statistics
import numpy as np
from itertools import zip_longest

## Takes the progeny file from Aevol, and returns the
## generation in number of progeny per generation.
def get_variance(progeny_file, output_variance_file):
        progeny = []
        variance = []
        times = []
        with open(progeny_file,'r') as csvfile:
            c = csv.reader(csvfile, delimiter = ',')

            generation=0
            for row in c:
                    if(int(row[0])!=generation):
                        if(progeny!=[]):
                            progeny = progeny + [0]*(int(inputPopSize)- reproducers)
                            variance.append(statistics.pvariance(progeny))
                            progeny = []
                            times.append(generation)
                    progeny.append(int(row[2]))
                    generation=int(row[0])

        progeny = progeny + [0]*(int(inputPopSize)- reproducers)
        variance.append(statistics.pvariance(progeny))
        times.append(generation)

        #write variance values to file so we dont keep recalculating
        d = [times, variance]
        export_data = zip_longest(*d, fillvalue = '')
        with open(output_variance_file, 'w', encoding="ISO-8859-1", newline='') as myfile:
              wr = csv.writer(myfile)
              wr.writerow(("Generation", "Variance of progeny"))
              wr.writerows(export_data)
        myfile.close()

input_progeny_file = input("Enter the progeny file name: ")
output_file = input("Enter the output file name: ")
get_variance(input_progeny_file, output_file)
