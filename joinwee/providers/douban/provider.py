from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class DoubanAccount(ProviderAccount):
    def get_profile_url(self):
        return self.account.extra_data.get('alt')

    def get_avatar_url(self):
        return self.account.extra_data.get('avatar')

    def to_str(self):
        return self.account.extra_data.get('name', super().to_str())


class DoubanProvider(OAuth2Provider):
    id = 'douban'
    name = 'Douban'
    account_class = DoubanAccount
    oauth2_adapter_class = None  # set by views.py after import

    access_token_url = 'https://www.douban.com/service/auth2/token'
    authorize_url = 'https://www.douban.com/service/auth2/auth'
    profile_url = 'https://api.douban.com/v2/user/~me'

    default_scope = ['douban_basic_common']

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        return dict(
            username=data.get('name') or data.get('uid'),
            name=data.get('name'),
        )

    def extract_email_addresses(self, data):
        return []


provider_classes = [DoubanProvider]
