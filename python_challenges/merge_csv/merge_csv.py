# challenge is to create a program to merge CSV files

import csv

def merge_csv(csv_list, output_path):
    fieldnames= list() #empty list
    #create a list
    for file in csv_list:
        with open(file,'r') as input_csv:
            fn = csv.DictReader(input_csv).fieldnames #extract field names from file
            fieldnames.extend(x for x in fn if x not in fieldnames)

    with open(output_path,'w',newline='') as output_csv: #context manager
        writer = csv.DictWriter(output_csv,fieldnames=fieldnames) #dict
        writer.writeheader()
        for file in csv_list: #iterate list
            with open(file,'r') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)

if __name__ == '__main__':
    pass