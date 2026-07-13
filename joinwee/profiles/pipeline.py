from django.contrib.auth.models import User
from guardian.shortcuts import assign, get_perms_for_model

from profiles.models import Profile

def create_profile(user=None, profile=None, *args, **kwargs):
    """
    Create user profile if necessaryxs
    """
    if profile:
        return {'profile': profile}

    if not user:
        return

    return {'profile': Profile.objects.get_or_create(user=user)[0]}

def set_guardian_permissions(user=None, profile=None, *args, **kwargs):
    """
    Give the user permission to modify themselves
    """
    if not user or not user.is_authenticated:
        return

    if profile:
        # Give permissons to view and change profile
        for perm in get_perms_for_model(Profile):
            assign(perm.codename, user, profile)

    # Give permissions to view and change itself
    for perm in get_perms_for_model(User):
        assign(perm.codename, user, user)
