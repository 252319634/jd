# -*- coding=utf-8 -*-
import datetime
from django.shortcuts import render, render_to_response, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from app.models import *
from app.forms import *
from app.userSession import UserSession
from django.http import JsonResponse
from app.verify_gen import get_verify


def verify(request):
    img, text = get_verify()
    request.session['verify_text'] = text
    # print(text)
    return HttpResponse(img, content_type='image/jpeg')
    # 返回的内容是图片要用 content_type='image/jpge' 来说明.不能直接return img


def msg(state):
    """
        # state
        # 0:"登录成功"
        # 1:"用户名不存在"
        # 2:"密码不正确"
        # 3:"验证码输入错误"
        # 4:"两次密码不匹配"
        # 5:"用户名已存在"
        # 6:"注册成功"
        # 7:"信息有错误"
    """
    state_dict = {0: "登录成功", 1: "用户名不存在", 2: "密码不正确", 3: "验证码输入错误",
                  4: "两次密码不匹配", 5: "用户名已存在", 6: "注册成功", 7: "信息有错误!", 8: "注销成功!"}
    return {"state": state, "msg": state_dict[state]}


def index(request):
    return render_to_response('index.html', locals())


def flow1(request):
    return render_to_response('my/flow1.html', locals())


def flow2(request):
    return render_to_response('my/flow2.html', locals())


def flow3(request):
    return render_to_response('my/flow3.html', locals())


def login(request):
    if request.method == 'GET':
        if request.user:
            return HttpResponseRedirect('/user/')  # 如果已经登录则跳转到用户中心
        return render_to_response('login.html', locals(), context_instance=RequestContext(request))
        # 没有登录就显示登录页面, context_instance=RequestContext(request)这个参数提供crsf_token
    if request.method == 'POST':
        userName = request.POST.get("userName")  # 获得表单中的用户名
        password = request.POST.get("password")  # 获得表单中的密码
        checkCode = request.POST.get("checkCode").strip().lower()  # 表单中的验证码
        theCheckCode = request.session.get('verify_text').strip().lower()
        # 正确的验证码,verify()方法中,生成的时候存进session中了 .
        # print('checkCode:',checkCode)
        # print('thecheckCode:',theCheckCode)
        ifSave = request.POST.get("ifSave")
        user = None
        try:
            user = User.objects.get(userName=userName)
        except:
            pass
        # print(user)
        if (user == None):
            return JsonResponse(msg(1))

        if (user.password != password):
            return JsonResponse(msg(2))

        if (checkCode != theCheckCode):
            return JsonResponse(msg(3))

        myUser = UserSession(user.userID, user.userName)
        request.session["user"] = myUser.toDict()  # 加入session,注意db模式要使用字典，不能直接使用对象

        # if ifSave == "true":
        # dt = datetime.datetime.now() + datetime.timedelta(hours=5)
        # response = HttpResponse()
        # response.set_cookie("userName", user.userName, expires=dt)
        # response.set_cookie("password", user.password, expires=dt)
        return JsonResponse(msg(0))


def logout(request):
    del request.session['user']
    return HttpResponseRedirect('/')
    # return JsonResponse(msg_dict(8))


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
        #     $.ajaxSetup({headers: {"X-CSRFToken": '{{ csrf_token }}'}});
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
        user1 = User.objects.filter(userName=username)
        # 查询用户名是否存在,使用filter方法查询不到返回空列表[],不报错
        # print('用户注册的信息:%s'%locals())
        if user1:
            return JsonResponse(msg(5))  # 用户名已存在
        if password1 != password2:
            return JsonResponse(msg(4))  # 两次密码不匹配
        u = User(userName=username, password=password1, )  # 生成一个user对象
        # print(u.userID,u.userName)
        # u 没有save()之前是没有userID的
        u.save()
        # save()之后就是一个完整的user对象了
        # print(u.userID,u.userName)
        myUser = UserSession(u.userID, u.userName)
        request.session["user"] = myUser.toDict()  # 加入session,注意db模式要使用字典，不能直接使用对象
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