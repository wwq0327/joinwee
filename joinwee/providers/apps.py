from django.apps import AppConfig


class ProvidersConfig(AppConfig):
    name = 'providers'
    verbose_name = 'OAuth Providers'

    def ready(self):
        from allauth.socialaccount.providers import registry
        from providers.douban.provider import DoubanProvider
        from providers.weibo.provider import WeiboProvider
        from providers.douban.views import DoubanOAuth2Adapter
        from providers.weibo.views import WeiboOAuth2Adapter

        DoubanProvider.oauth2_adapter_class = DoubanOAuth2Adapter
        WeiboProvider.oauth2_adapter_class = WeiboOAuth2Adapter

        registry.register(DoubanProvider)
        registry.register(WeiboProvider)
