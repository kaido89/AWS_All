import os
import csv
from datetime import datetime
try:
    import yaml
except Exception as e:
    print(e)
    print("Run the command:\n pip3 install pyyaml --user")
today = datetime.now().date()


class OptionInvalid(Exception):
    pass


# create output file
def create_output_file():
    csv_filename = input('Insert you csv filename: ')
    if not os.path.exists(os.path.expanduser('output/')):
        os.makedirs(os.path.expanduser('output'))
    output_path = os.path.expanduser('output/')
    output_file = open(output_path+csv_filename+'_'+str(today)+'.csv', 'w')
    output_csv = csv.writer(output_file)
    return output_csv


def setup_config():
    # save to yml file
    return


def main():
    print('Option:\n1- Setup\n2- Load Settings\n3- Create new output file')
    option = input('Choose one of the options: ')
    try:
        if '1' == option:
            setup_config()
        elif '2' == option:
            create_output_file()
        else:
            raise OptionInvalid
    except OptionInvalid:
        print("*** Error *** Invalid Option")


main()
