import os
import csv
from datetime import datetime
today = datetime.now().date()


# create output file
def create_output_file():
    csv_filename = input('Insert you csv filename: ')
    if not os.path.exists(os.path.expanduser('output/')):
        os.makedirs(os.path.expanduser('output'))
    output_path = os.path.expanduser('output/')
    output_file = open(output_path+csv_filename+'_'+str(today)+'.csv', 'w')
    output_csv = csv.writer(output_file)
    return output_csv


def main():
    create_output_file()


main()
