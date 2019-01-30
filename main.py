import os, sys, csv
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
    if not os.path.exists(os.path.expanduser('configuration/')):
        os.makedirs(os.path.expanduser('configuration'))
    aws_config_path = os.path.expanduser('configuration/')
    aws_config = open(aws_config_path + "aws.conf", "w+")
    profile = input('AWS profile: ')
    aws_config.write("profile : \""+profile+"\"\n")
    region = input('AWS region: ')
    aws_config.write("region : \"" + region + "\"\n")
    return main()


def load_settings():
    aws_config_path = os.path.expanduser('configuration/')
    aws_config = open(aws_config_path + "aws.conf", "r")
    aws_yml = yaml.load(aws_config)
    print('Profile: '+aws_yml['profile']+', Region: '+aws_yml['region'])
    return


def main():
    print('Option:\n1 - Setup AWS\n2 - Load Settings\n3 - Create new output file\n0 - Exit')
    option = input('Choose one of the options: ')
    try:
        if '1' == option:
            setup_config()
        elif '2' == option:
            load_settings()
        elif '3' == option:
            create_output_file()
        elif '0' == option:
            print('Successfully exited the program')
            sys.exit()
        else:
            raise OptionInvalid
    except OptionInvalid:
        print("*** Error *** Invalid Option")


main()
