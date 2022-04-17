from mycelery.main import app

@app.task(name="send_sms")
def send_sms():
    """发送短信"""
    return "send a sms"