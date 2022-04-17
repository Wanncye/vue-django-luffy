from celery import Celery

# 创建Celery的主程序对象
app = Celery("luffy")

# 将jango和celery结合，需要先启动django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffyapi.settings.dev')
import django
django.setup()

# 加载配置
app.config_from_object("mycelery.config")

# 注册celery任务
app.autodiscover_tasks(["mycelery.sms"])

# 通过终端来启动celery
# celery -A mycelery.main worker --loglevel=info
