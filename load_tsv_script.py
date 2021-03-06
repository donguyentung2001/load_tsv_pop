import sys 
import csv

input_file = sys.argv[1]
value = sys.argv[2]
output_file = sys.argv[3]

tsv_file = open(input_file)
output = [] 
with open(input_file) as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    col_index  = None 
    count = 0
    for row in rd:
        if col_index is None: 
            col_index = row.index("Population code")
        else: 
            if row[col_index] == value:
                output.append(row[0])
print(output)
tsv_file.close() 

f= open(output_file,"w+")

f.write('\n'.join(output) + '\n')

f.close()