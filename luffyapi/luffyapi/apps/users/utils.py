def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    :param token    本次登录成功后返回的jwt
    :param user     本次登录成功以后从数据库中查询到的用户模型信息
    :param token    本次客户端的请求对象
    """
    return {
        'token': token,
        'id': user.id,
        'username': user.username
    }