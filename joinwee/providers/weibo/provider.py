from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class WeiboAccount(ProviderAccount):
    def get_profile_url(self):
        return self.account.extra_data.get('profile_url')

    def get_avatar_url(self):
        return self.account.extra_data.get('avatar_large')

    def to_str(self):
        return self.account.extra_data.get('screen_name', super().to_str())


class WeiboProvider(OAuth2Provider):
    id = 'weibo'
    name = 'Weibo'
    account_class = WeiboAccount
    oauth2_adapter_class = None  # set by views.py after import

    access_token_url = 'https://api.weibo.com/oauth2/access_token'
    authorize_url = 'https://api.weibo.com/oauth2/authorize'
    profile_url = 'https://api.weibo.com/2/users/show.json'

    default_scope = []

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        return dict(
            username=data.get('screen_name'),
            name=data.get('name'),
        )

    def extract_email_addresses(self, data):
        return []


provider_classes = [WeiboProvider]
