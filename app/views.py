# -*- coding=utf-8 -*-
import datetime
from django.shortcuts import render, render_to_response, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from app.models import *
from app.forms import *
from app.userSession import UserSession
from django.http import JsonResponse
from app.verify_gen import get_verify
from user_tools import *


def verify(request):
    # 生成验证码图片
    img, text = get_verify()
    request.session['verify_text'] = text

    # print(text)
    return HttpResponse(img, content_type='image/jpeg')
    # 返回的内容是图片要用 content_type='image/jpge' 来说明.不能直接return img


def index(request):
    print('index,用户信息:%s' % request.session.get('user',''))
    # 获取字典值一律使用get('','')方法!...否则取不到会报错
    return render_to_response('index.html', locals())


def flow1(request):
    return render_to_response('my/flow1.html', locals())


def flow2(request):
    return render_to_response('my/flow2.html', locals())


def flow3(request):
    return render_to_response('my/flow3.html', locals())


def login(request):
    if request.method == 'GET':
        if user_is_login(request):
            return HttpResponseRedirect('/user/')  # 如果已经登录则跳转到用户中心
        return render_to_response('login.html', locals(), context_instance=RequestContext(request))
        # 没有登录就显示登录页面, context_instance=RequestContext(request)这个参数提供crsf_token
    if request.method == 'POST':
        if user_is_login(request):
            return HttpResponseRedirect('/user/')  # 如果已经登录则跳转到用户中心
        msg = user_login(request)
        return JsonResponse(msg)


def logout(request):
    user_logout(request)
    return HttpResponseRedirect('/')


# 这个视图使用了csrf 下面的render_to_response后面跟上context_instance=RequestContext(request)
def register(request):
    if request.method == 'GET':  # get请求
        return render_to_response('register.html', context_instance=RequestContext(request))
        # 只有带上context_instance = RequestContext(request) 才能带上csrf_token的数据.
        # 模版中表单里要添加{% csrf_token %}
        # ajax传回token,
        # 方法1:使用单独的csrf.js文件处理请求头,从cookie中取得token
        # 方法2:模板中添加下面的js,渲染模板时就取得了token
        # <script type="text/javascript">
        # $.ajaxSetup({headers: {"X-CSRFToken": '{{ csrf_token }}'}});
        # </script>
    if request.method == 'POST':  # post请求
        form = RegisterForm(request.POST)  # 使用form类来验证数据的合法性,只能验证单一字段,不能验证两次密码是否相同
        # print('验证表单前的信息:%s'%locals())
        if not form.is_valid():
            return JsonResponse(msg(7))  # 笼统的返回错误信息
        # 自己验证数据

        username = request.POST.get('username', '')  # 得到用户名
        password1 = request.POST.get('password1', '')  # 得到密码1
        password2 = request.POST.get('password2', '')  # 得到密码2
        u = User.objects.filter(userName=username)
        # 查询用户名是否存在,使用filter方法查询不到返回空列表[],不报错
        # print('用户注册的信息:%s'%locals())
        if u:
            return JsonResponse(msg(5))  # 用户名已存在
        if password1 != password2:
            return JsonResponse(msg(4))  # 两次密码不匹配
        u = User(userName=username, password=password1, )  # 生成一个user对象
        # print(u.userID,u.userName)
        # u 没有save()之前是没有userID的
        u.save()
        # save()之后就是一个完整的user对象了
        # print(u.userID,u.userName)
        myuser = UserSession(u.userID, u.userName)
        request.session["user"] = myuser.toDict()  # 加入session,注意db模式要使用字典，不能直接使用对象
        return JsonResponse(msg(0))


def order(request):
    return render_to_response('my/order.html', locals())


def address(request):
    return render_to_response('my/address.html', locals())


def goods(request):
    return render_to_response('goods.html', locals())


def list(request):
    return render_to_response('list.html', locals())


def user(request):
    if not request.user:
        return HttpResponseRedirect('/login/')
    return render_to_response('user.html', locals())