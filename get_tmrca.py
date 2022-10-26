import csv
import numpy as np
from itertools import zip_longest
## Takes in the Coalescence time output from Aevol, and reverses the selective
## sweeps to get the Time Since Most Recent Common Ancestor.

def get_tmrca(coalescence_file, output_file):
    x = []
    y = []
    times = []
    current = 0
    previous = 0
    tmrca = []
    sweep_number = 0

    with open(coalescence_file,'r') as csvfile:
        c = csv.reader(csvfile, delimiter = ',')

        next(csvfile)
        for row in c:
            x.append(int(row[0]))
            y.append(int(row[1]))

    #take in a value
    #start a list
    #when the value is more than the previous value that is the start of a new sweep
    #reverse the old list and add it to the tmrca

    for gen in y:
        current = gen
        if current > previous:
            #reverse times
            times.reverse()
            tmrca.extend(times)
            sweep_number = sweep_number + 1
            times = []
        times.append(current)
        previous = current


    #write values to file so we dont keep recalculating
    d = [range(0,len(tmrca)), tmrca]
    export_data = zip_longest(*d, fillvalue = '')
    with open(output_file, 'w', encoding="ISO-8859-1", newline='') as myfile:
          wr = csv.writer(myfile)
          wr.writerow(("Generation", "Tmrca"))
          wr.writerows(export_data)
    myfile.close()


input_coalescence_file = input("Enter the coalescence file name: ")
output_file = input("Enter the output file name: ")
get_tmrca(input_coalescence_file, output_file)
