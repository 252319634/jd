# -*- coding: utf-8 -*-

import re
from django.http import HttpResponse
# from django.shortcuts import render_to_response
from django.template import loader, Context
# 必须返回 HttpResponse ,不能用render_to_response


class CheckSession(object):
    def process_request(self, request):
        # process_request 方法不用返回request
        print('中间件request处理程序开始>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

        request.user = request.session.get('user', '')
                       # | request.COOKIE.get('userName') 提示'WSGIRequest' object has no attribute 'COOKIE'
        # print('user:'+request.user)
        # 取出session中的user,存到request.user中
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<中间件request处理程序结束')
        # # 获得所有request的数据
        # # 先获得mete数据
        # # request_csrf_token = request.META.get('HTTP_X_CSRFTOKEN', '')
        # # print(request_csrf_token)
        # for k, v in request.META.items():
        # print('%s:%s' % (k, v))
        #
        # print(request.method)
        #
        # request_csrf_token = ""
        # csrf_token的处理过程:
        # if request.method == "POST":
        # try:
        #         print('request.POST.csrfmiddlewaretoken:',request.POST.get('csrfmiddlewaretoken', ''))
        #     except IOError:
        #         # Handle a broken connection before we've completed reading
        #         # the POST data. process_view shouldn't raise any
        #         # exceptions, so we'll ignore and serve the user a 403
        #         # (assuming they're still listening, which they probably
        #         # aren't because of the error).
        #         pass
        #
        # if request_csrf_token == "":
        #     # Fall back to X-CSRFToken, to make things easier for AJAX,重点在这一句
        #     # and possible for PUT/DELETE.
        #     request_csrf_token = request.META.get('HTTP_X_CSRFTOKEN', '')
        #     print('request.META.HTTP_X_CSRFTOKEN:',request_csrf_token)


    def process_response(self, request, response):
        print('中间件response处理程序开始>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # print(response.content[:200])
        # print(response.cookies)
        # print(response.status_code)
        print (u'图片验证中的内容是:' + request.session.get('verify_text', ''))
        # if response.status_code == 403:
        # response.content = "403 Forbidden"
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<中间件response处理程序结束')
        return response  # process_response方法必须返回一个response

