# JoinWEE

开放教育平台——围绕"微课"（WEE Lesson）构建的在线学习社区，支持课程创建、线下聚会、研修活动、讨论交流。

## 技术栈

| 层 | 技术 |
|---|---|
| 后端 | Python 3.12 + Django 4.2 LTS |
| 数据库 | SQLite（开发）/ MySQL（生产） |
| 前端 | Bootstrap 3.4.1 + jQuery 3.7.1 |
| 编辑器 | Pagedown (Markdown) + EpicEditor |
| 认证 | django-allauth（邮箱注册 + 社交登录） |
| 权限 | django-guardian |
| 缩略图 | easy-thumbnails / Pillow |

## 模块

| 应用 | 功能 |
|------|------|
| `home` | 首页、关于页 |
| `weelesson` | 微课（核心）：创建/编辑/发布/收藏 |
| `weemeet` | 微聚：线下聚会报名与管理 |
| `study` | 研修：定时分期的在线学习活动 |
| `topics` | 讨论：微课/聚会下的主题讨论 + 回复 |
| `blog` | 博客公告 + 评论 |
| `profiles` | 用户资料、个人主页 |
| `fav` | 通用收藏与参与 |
| `providers` | 自定义豆瓣/微博 OAuth provider |

## 快速开始

```bash
# 创建虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 安装依赖
pip install -r requirements/prj.txt

# 数据库迁移
cd joinwee
python manage.py migrate

# 创建测试账号
python manage.py createsuperuser

# 启动服务
python manage.py runserver
```

访问 http://127.0.0.1:8000/

## 配置

复制 `.env.example` 为 `.env`，按需修改：

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `SECRET_KEY` | Django 密钥 | **必须设置** |
| `DEBUG` | 调试模式 | `True` |
| `DB_ENGINE` | 数据库引擎 | `django.db.backends.sqlite3` |
| `DB_NAME` | 数据库名称 | `db.sqlite3` |

## 测试数据

```bash
python manage.py shell < scripts/seed_data.py
```

测试用户密码统一为 `test123`。

## 部署

生产环境建议：

```
DEBUG=False
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
DB_ENGINE=django.db.backends.mysql
```

## 从旧版迁移

本项目原基于 Django 1.5 + Python 2.7，已迁移至 Django 4.2 LTS。旧版 South 迁移文件归档在 `archive/south_migrations/`。

## License

Creative Commons BY-NC-SA 3.0
