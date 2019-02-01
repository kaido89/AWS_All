This function delete iam user.

Function that we can use to delete iam user
* delete_user_with_profile(profile, region, user)
* delete_user_with_instance_role(user)
* delete_user_with_new_role(user, new_role_arn, region)

Requirements to delete the user:
* iam:DeactivateMFADevice<br>
* iam:DeleteAccessKey<br>
* iam:RemoveUserFromGroup<br>
* iam:DeleteVirtualMFADevice<br>
* iam:ListAttachedUserPolicies<br>
* iam:DeleteUser<br>
* iam:ListMFADevices<br>
* iam:DetachUserPolicy<br>
* iam:TagUser<br>
* iam:DeleteLoginProfile<br>
* iam:ListUserTags<br>
* iam:ListAccessKeys<br>