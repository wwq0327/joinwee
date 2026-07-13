from django.apps import AppConfig


class ProvidersConfig(AppConfig):
    name = 'providers'
    verbose_name = 'OAuth Providers'

    def ready(self):
        from allauth.socialaccount.providers import registry
        from providers.douban.provider import DoubanProvider
        from providers.weibo.provider import WeiboProvider
        registry.register(DoubanProvider)
        registry.register(WeiboProvider)
