from celery import Celery

# 创建Celery的主程序对象
app = Celery()

# 加载配置
app.config_from_object("mycelery.config")

# 注册celery任务
app.autodiscover_tasks(["mycelery.sms"])

# 通过终端来启动celery
# celery -A mycelery.main worker --loglevel=info
