import boto3
from datetime import datetime
today = str(datetime.now().date())


def put_ssm(session, table_id):
    ssm = session.client('ssm')
    ssm.put_parameter(Name='table_name_id', Description='This is dynamodb table id', Value=table_id,
                      Type='String', Overwrite=True)


def set_dynamodb_items(file, session, table_name, table_id):
    dynamodb = session.client('dynamodb')
    for line in file:
        first_collumn = str(line.split(',')[0])
        table_id += 1
        dynamodb.put_item(TableName=table_name, Item={'ID': {"N": str(table_id)}, 'Name': {"S": str(first_collumn)},
                                                      'Date': {"S": str(today)}})
    return table_id


def get_ssm(session):
    ssm = session.client('ssm')
    try:
        return ssm.get_parameter(Name='table_name_id', WithDecryption=True)
    except Exception as ex:
        print(ex)
        return 0


def get_dynamodb_table_name(session):
    dynamodb = session.client('dynamodb')
    table_name = dynamodb.list_tables()['TableNames'][0]
    return table_name


def get_session(profile_name, region_name):
    session = boto3.Session(profile_name=profile_name, region_name=region_name)
    return session


def main():
    profile_name = 'kaido89'
    region_name = 'eu-west-1'
    session = get_session(profile_name, region_name)
    table_name = get_dynamodb_table_name(session)
    file = open('~/open_file.csv', 'r')
    table_id = get_ssm(session)
    table_id = set_dynamodb_items(file, session, table_name, table_id)
    put_ssm(session, table_id)


main()