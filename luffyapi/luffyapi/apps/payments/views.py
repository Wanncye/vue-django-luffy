from rest_framework.views import APIView
from alipay import AliPay
from django.conf import settings
from rest_framework.response import Response
from order.models import Order
from rest_framework import status
from datetime import datetime
# from coupon.models import UserCoupon
from django.db import transaction
# from users.models import UserCourse
from course.models import CourseExpire

import logging
log = logging.getLogger("django")

class AlipayAPIView(APIView):
    def get(self,request):
        """获取支付宝的支付地址"""
        # 获取订单号
        order_number = request.query_params.get("order_number")
        # 判断订单是否存在
        try:
            order = Order.objects.get(order_number=order_number)
        except Order.DoesNotExist:
            return Response({"message":"对不起，订单不存在！"}, status=status.HTTP_400_BAD_REQUEST)

        # 初始化支付对象
        """
        self,
        appid,
        app_notify_url=None,
        app_private_key_string=None,
        alipay_public_key_string=None,
        sign_type="RSA2",
        debug=False,
        verbose=False,
        config=None
        """
        # app_public_key_cert_string=settings.ALIAPY_CONFIG["app_public_key_path"],
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay = AliPay(
            appid=settings.ALIAPY_CONFIG["appid"],
            app_notify_url=settings.ALIAPY_CONFIG["app_notify_url"],  # 默认回调url
            app_private_key_string=settings.ALIAPY_CONFIG["app_private_key_path"],
            alipay_public_key_string=settings.ALIAPY_CONFIG["alipay_public_key_path"],
            sign_type=settings.ALIAPY_CONFIG["sign_type"],
            debug = settings.ALIAPY_CONFIG["debug"]  # 默认False
        )
        
        # 调用接口
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=order.order_number,
            total_amount=float(order.real_price),
            subject=order.order_title,
            return_url=settings.ALIAPY_CONFIG["return_url"],
            notify_url=settings.ALIAPY_CONFIG["notify_url"]  # 可选, 不填则使用默认notify url
        )

        url = settings.ALIAPY_CONFIG["gateway_url"] + order_string

        return Response(url)

# from django.http.response import HttpResponse
# class AliPayResultAPIView(APIView):
#     def get(self,request):
#         """处理支付宝同步通知结果"""
#         # 初始化支付对象
#         alipay = AliPay(
#             appid=settings.ALIAPY_CONFIG["appid"],
#             app_notify_url=settings.ALIAPY_CONFIG["app_notify_url"],  # 默认回调url
#             app_private_key_path=settings.ALIAPY_CONFIG["app_private_key_path"],
#             # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
#             alipay_public_key_path=settings.ALIAPY_CONFIG["alipay_public_key_path"],
#             sign_type=settings.ALIAPY_CONFIG["sign_type"],
#             debug = settings.ALIAPY_CONFIG["debug"]  # 默认False
#         )

#         data = request.query_params.dict()
#         signature = data.pop("sign")
#         # verification
#         success = alipay.verify(data, signature)
#         if success:
#             return self.change_order_status(data)
#         return Response({"message":"对不起，当前订单支付失败！"})

#     def post(self,request):
#         """处理支付宝异步通知结果"""
#         # 初始化支付对象
#         alipay = AliPay(
#             appid=settings.ALIAPY_CONFIG["appid"],
#             app_notify_url=settings.ALIAPY_CONFIG["app_notify_url"],  # 默认回调url
#             app_private_key_path=settings.ALIAPY_CONFIG["app_private_key_path"],
#             # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
#             alipay_public_key_path=settings.ALIAPY_CONFIG["alipay_public_key_path"],
#             sign_type=settings.ALIAPY_CONFIG["sign_type"],
#             debug = settings.ALIAPY_CONFIG["debug"]  # 默认False
#         )

#         data = request.data
#         signature = data.pop("sign")
#         success = alipay.verify(data, signature)
#         if success and data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED" ):
#             response = self.change_order_status(data)
#             if "credit" in response.data:
#                 return HttpResponse("success")

#         return Response({"message":"对不起，当前订单支付失败！"})


#     def change_order_status(self,data):
#         # 补充支付成功以后的代码
#         order_number = data.get("out_trade_no")
#         try:
#             order = Order.objects.get(order_number=order_number, order_status=0)
#         except Order.DoesNotExist:
#             return Response({"message": "对不起，支付结果查询失败！订单不存在！"}, status=status.HTTP_400_BAD_REQUEST)

#         with transaction.atomic():
#             save_id = transaction.savepoint()
#             # 更新订单状态、记录支付时间
#             try:
#                 order.pay_time = datetime.now()
#                 order.order_status = 1
#                 order.save()

#                 # 如果有使用优惠券或者积分，则修改优惠券的使用状态和扣除积分
#                 # user_coupon_id = order.coupon
#                 # if user_coupon_id > 0:
#                 #     user_coupon = UserCoupon.objects.get(pk=user_coupon_id, is_use=False, is_show=True,
#                 #                                          is_deleted=False)
#                 #     user_coupon.is_use = True
#                 #     user_coupon.save()

#                 credit = order.credit
#                 if credit > 0:
#                     user = order.user
#                     user.credit -= credit
#                     user.save()

#                 # 记录用户成功购买课程的记录, 增加课程的购买人数
#                 order_detail_list = order.order_courses.all()
#                 course_list = []
#                 for order_detail in order_detail_list:
#                     """循环本次订单中所有购买的商品课程"""
#                     course = order_detail.course
#                     course.students += 1
#                     course.save()

#                     pay_timestamp = order.pay_time.timestamp()
#                     if order_detail.expire > 0:
#                         # 有效期间购买
#                         expire = CourseExpire.objects.get(pk=order_detail.expire)
#                         expire_timestamp = expire.expire_time * 24 * 60 * 60
#                         out_time = datetime.fromtimestamp(pay_timestamp + expire_timestamp)
#                     else:
#                         # 永久购买
#                         out_time = None

#                     UserCourse.objects.create(
#                         user_id=user.id,
#                         course_id=course.id,
#                         trade_no=data.get("trade_no"),
#                         buy_type=1,
#                         pay_time=order.pay_time,
#                         out_time=out_time
#                     )

#                     course_list.append({
#                         "id": course.id,
#                         "name": course.name
#                     })

#             except:
#                 log.error("订单结果处理出现故障!无法修改订单相关记录的状态")
#                 transaction.savepoint_rollback(save_id)
#                 return Response({"message": "对不起，更新订单相关记录失败！"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#         # 返回结果

#         return Response({
#             "message": "支付成功！",
#             "pay_time":order.pay_time,
#             "real_price":order.real_price,
#             "course_list": course_list
#         })