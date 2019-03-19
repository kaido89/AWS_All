import boto3


def function_copy(bucket, key, output_directory, output_filename, s3_session):
    s3_session.download_file(bucket, key, output_directory + output_filename)


def copy_s3(bucket, key, output_directory, output_filename, new_role_arn):
    sts = boto3.client('sts')
    response = sts.assume_role(RoleArn=new_role_arn, RoleSessionName="copy_s3_session", DurationSeconds=3600)
    session = boto3.Session(aws_access_key_id=response['Credentials']['AccessKeyId'],
                            aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                            aws_session_token=response['Credentials']['SessionToken'], region_name='us-east-1')
    s3_session = session.client('s3')
    function_copy(bucket, key, output_directory, output_filename, s3_session)


def main():
    new_role_arn = 'arn:aws:iam::---CHANGE TO ACCOUNT ID---:role/---CHANGE Role Name---'
    bucket = '---CHANGE TO BUCKET NAME---'
    key = '---CHANGE TO OBJECT KEY---'
    output_directory = '---CHANGE TO OUTPUT DIRECTORY---'
    output_filename = '---CHANGE TO OUTPUT FILE NAME---'
    copy_s3(bucket, key, output_directory, output_filename, new_role_arn)
