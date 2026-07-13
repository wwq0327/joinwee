# joinwee 现代化迁移方案

## 目标栈

| 组件 | 旧版 | 新版 |
|------|------|------|
| Python | 2.7 | 3.11 |
| Django | 1.5.4 | 4.2 LTS |
| 数据库驱动 | MySQL-python | mysqlclient |
| 迁移工具 | South | Django 内置迁移 |
| 认证 | django-userena + django-social-auth | django-allauth |

## 第一阶段：依赖替换

| 旧包 | 替换方案 |
|------|----------|
| django-userena | django-allauth（注册/登录/邮箱验证/社交登录） |
| django-social-auth | django-allauth 社交账号 |
| linaro-django-pagination | 移除，用 Django 内置 Paginator |
| MySQL-python | mysqlclient |
| South | 移除 |
| distribute / argparse / wsgiref / readline | 全部移除 |

保留升级：django-guardian, django-hitcount, django-notifications-hq, django-taggit, easy-thumbnails, django-bootstrap3, Pillow, Markdown

## 第二阶段：Django API 迁移

| 旧写法 | 新写法 |
|--------|--------|
| `django.core.urlresolvers.reverse` | `django.urls.reverse` |
| `patterns('', ...)` | `urlpatterns = [...]` |
| `render_to_response` + `RequestContext` | `render(request, ...)` |
| `contenttypes.generic` | `contenttypes.fields` |
| `@models.permalink` | 方法内 `reverse()` |
| `get_query_set()` | `get_queryset()` |
| `MIDDLEWARE_CLASSES` | `MIDDLEWARE` |
| 散列 TEMPLATE_* 配置 | TEMPLATES 字典 |
| `django.contrib.comments` | django-contrib-comments 或重构 |
| `django.contrib.markup` | 直接用 Python Markdown |
| `python_2_unicode_compatible` | 移除 |
| `from django.conf.urls import patterns, url` | `from django.urls import path, re_path` |

## 第三阶段：用户认证重构

django-userena + django-social-auth → django-allauth
- 保留 profiles.Profile 模型
- pipeline.py 逻辑移植到 allauth 信号
- 豆瓣 OAuth 需要自定义 provider
- URL 路由重新映射

## 第四阶段：模板迁移

- 移除 `{% load comments %}`, `{% load markup %}`
- 修复 base.html Git 冲突标记
- URL 模板标签适配

## 第五阶段：数据迁移

- 用 Django 内置 makemigrations 生成初始迁移
- 处理 django_comments 旧数据
- South 迁移记录处理

## 工作步骤

参见执行过程中的逐步清单。
