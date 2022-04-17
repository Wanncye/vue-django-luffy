from mycelery.main import app

@app.task(name="send_email")
def send_sms():
    """发送邮件"""
    return "send a email"