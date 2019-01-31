import boto3
from botocore.exceptions import ClientError


def delete_login_profile(iam_session, user):
    try:
        iam_session.delete_login_profile(UserName=user)
    except ClientError:
        print('No Login Profile')


def function_delete_user(iam_session, user):
    delete_login_profile(iam_session, user)
    # # To be Fixed
    # iam_session.remove_user_from_group(UserName='', GroupName=user)
    # iam_session.detach_user_policy(UserName=user, PolicyArn='')
    # iam_session.delete_access_key(UserName=user, AccessKeyId='')
    # iam_session.deactivate_mfa_device(UserName=user, SerialNumber='')
    # iam_session.delete_virtual_mfa_device(SerialNumber='')
    # iam_session.delete_user(UserName=user)


def delete_user_with_profile_iam(profile, region, user):
    session = boto3.Session(profile_name=profile, region_name=region)
    iam_session = session.client('iam')
    function_delete_user(iam_session, user)


def delete_user_with_instance_role(user):
    iam_session = boto3.client('iam')
    function_delete_user(iam_session, user)


def delete_user_with_new_role(user, new_role_arn, region):
    sts = boto3.client('sts', region_name=region)
    session = sts.assume_role(RoleArn=new_role_arn, RoleSessionName="role_to_delete_user", DurationSeconds=3600)
    iam_session = session('iam')
    function_delete_user(iam_session, user)
