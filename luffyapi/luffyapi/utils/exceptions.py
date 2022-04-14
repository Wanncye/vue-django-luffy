from cgitb import handler
from django.db import DatabaseError
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

import logging
logger = logging.getLogger("django")


#内置的错误处理并没有包含处理数据库等错误的方法，我们需要自定义一些处理额外错误的方法

def custom_exception_handle(exc, contex):
    """
    自定义异常处理
    :param exc: 本次请求发生的异常信息
    :param context: 本次请求发送一场的执行上下文（包括request对象、异常发送的时间、行号等）
    :return:
    """
    response = exception_handler(exc, contex)
    if response is None:
        """两种情况：一种是没有错误发生，一种是rest_framework处理不了的错误"""
        view = contex["view"]
        if isinstance(exc, DatabaseError):
            logger.error('[%s] %s' % (view, exc))
            reponse = Response({'message' : '服务器内部错误，请联系客服工作人员'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return reponse
