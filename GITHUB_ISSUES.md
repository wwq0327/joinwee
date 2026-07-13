# GitHub Issues 待创建清单

网络恢复后运行以下命令创建：

```bash
# P0
gh issue create -t "模型字段警告修复" -b "FineLesson.lesson 改为 OneToOneField\nStudy/WEEMeet IntegerField 移除 max_length"

# P1
gh issue create -t "清理 userena 模板残留" -b "移除 userena_activation_required/activation_days 变量\n修复 email_change_complete.html 模板\n修复 confirmation_email_message_new.txt 邮件模板\n修复 profile_list.html 分页链接"

# P2
gh issue create -t "密钥外置到 .env 文件" -b "已实现，使用 python-decouple\nSECRET_KEY/DB_PASS/EMAIL_PASS/社交 API 密钥均移至 .env"
gh issue create -t "补充生产环境安全配置" -b "已添加 SECURE_SSL_REDIRECT/SESSION_COOKIE_SECURE/CSRF_COOKIE_SECURE/SECURE_HSTS_SECONDS/SECURE_CONTENT_TYPE_NOSNIFF"

# P3
gh issue create -t "归档未使用的 app" -b "brands/tags/weeteam 已移至 archive/apps/"

# P4
gh issue create -t "添加 weemeet 列表页" -b "已完成，访问 /meet/ 可查看全部微聚"
gh issue create -t "添加 topics 全局列表页" -b "低优先级，/discuss/ 仍需补一个全局讨论列表"

# P5
gh issue create -t "前端资源版本更新" -b "jQuery 1.10.2 → 3.7.1\nBootstrap 3.x/fancyBox/css 后续可升级"
```
