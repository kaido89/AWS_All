import boto3
from botocore.exceptions import ClientError


def delete_user(iam_session, user):
    try:
        iam_session.delete_user(UserName=user)
    except ClientError as ex:
        print(ex)


def delete_mfa(iam_session, user):
    try:
        for mfa in iam_session.list_mfa_devices(UserName='user_delete')['MFADevices']:
            iam_session.deactivate_mfa_device(UserName=user, SerialNumber=mfa['SerialNumber'])
            iam_session.delete_virtual_mfa_device(SerialNumber=mfa['SerialNumber'])
    except ClientError as ex:
        print(ex)


def delete_access_keys(iam_session, user):
    try:
        for access_key in iam_session.list_access_keys(UserName=user)['AccessKeyMetadata']:
            iam_session.delete_access_key(UserName=user, AccessKeyId=access_key['AccessKeyId'])
    except ClientError as ex:
        print(ex)


def detach_user_from_policies(iam_session, user):
    try:
        for policy in iam_session.list_attached_user_policies(UserName=user)['AttachedPolicies']:
            boto3.client('iam').detach_user_policy(UserName=user, PolicyArn=policy['PolicyArn'])
    except ClientError as ex:
        print(ex)


def detach_user_from_groups(iam_session, user):
    try:
        for group in iam_session.list_groups_for_user(UserName=user)['Groups']:
            iam_session.remove_user_from_group(UserName=user, GroupName=group['GroupName'])
    except ClientError as err:
        print(err)


def delete_login_profile(iam_session, user):
    try:
        iam_session.delete_login_profile(UserName=user)
    except ClientError as err:
        print(err)


def function_delete_user(iam_session, user):
    delete_login_profile(iam_session, user)
    detach_user_from_groups(iam_session, user)
    detach_user_from_policies(iam_session, user)
    delete_access_keys(iam_session, user)
    delete_mfa(iam_session, user)
    delete_user(iam_session, user)


def delete_user_with_profile(profile, region, user):
    session = boto3.Session(profile_name=profile, region_name=region)
    iam_session = session.client('iam')
    function_delete_user(iam_session, user)


def delete_user_with_instance_role(user):
    iam_session = boto3.client('iam')
    function_delete_user(iam_session, user)


def delete_user_with_new_role(user, new_role_arn, region):
    sts = boto3.client('sts', region_name=region)
    response = sts.assume_role(RoleArn=new_role_arn, RoleSessionName="role_to_delete_user", DurationSeconds=3600)
    session = boto3.Session(aws_access_key_id=response['Credentials']['AccessKeyId'],
                            aws_secret_access_key=response['Credentials']['SecretAccessKey'],
                            aws_session_token=response['Credentials']['SessionToken'], region_name='us-east-1')
    iam_session = session.client('iam')
    function_delete_user(iam_session, user)
