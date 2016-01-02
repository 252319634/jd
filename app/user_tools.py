# -*- coding: utf-8 -*-
import re
from app.models import User
from app.verify_gen import verifyTheText


def msg(state):
    """
        # 返回一个字典形式的状态的编码和说明
        # msg(1) --> {"state": 1, "msg": "信息有错误!"}
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


def toDict(userID, userName):
    """
    返回一个字典，session中的user字典，包括userID，userName两个keys
    :param userID: 123
    :param userName: aaa
    :return:{"userName": aaa, "userID": 123}
    """
    return {"userName": userName, "userID": userID}


def user_add_to_session(request, u):
    request.session["user"] = {"userName": u.userName, "userID": u.userID}
    # 加入session,注意db模式要使用字典，不能直接使用对象


def create_user(request):
    """

    :param request:
    :return:
    """


def user_name_is_valid(user_name):
    """
    验证用户名时候符合命名规则:用户名必须是3-20位字符，可由字母、数字和下划线组成,以字母开头,中文暂时不考虑
    :param user_name: 一个字符串
    :return: 符合规则返回True,否则返回False
    """

    if not re.match(r'^[a-zA-Z]\w{2,19}$', user_name):
        return False
    return True


def user_name_is_used(user_name):
    """
    验证用户名是否被使用
    :param ruquest:
    :return: 被 使用返回True 否则返回False
    """
    # user_name = request.POST.get('username', '')  # 得到用户名
    u = User.objects.filter(userName=user_name)
    # 查询用户名是否存在,使用filter方法查询不到返回空列表[],不报错
    # print('用户注册的信息:%s'%locals())
    if u:
        return True
    return False


def user_is_login(request):
    """
    判断用户是否登录
    :param request: 提供一个request,判断这个request里面是否包含了session.user信息, 包含user就是登陆了,不包含就是没有登录
    :return: 登录了就返回True 否则返回False
    """
    if request.session.get('user', ''):
        return True
    return False


def user_register(request):
    """
    用户注册
    :param request:
    :return:
    """
    if not verifyTheText(request):
        return msg(3)  #验证码错误
    password1 = request.POST.get('password1', '')  # 得到密码1
    password2 = request.POST.get('password2', '')  # 得到密码2
    username = request.POST.get('username', '')  # 得到用户名
    if user_name_is_used(username):
        return msg(5)  # 用户名已存在
    if password1 != password2:
        return msg(4)  # 两次密码不匹配
    u = User(userName=username, password=password1)
    u.save()  # 生成一个user对象
    # u 没有save()之前是没有userID的, save()之后就是一个完整的user对象了
    user_add_to_session(request, u)
    return msg(0)  # 注册成功

def user_login(request):
    """
    用户登录流程,验证用户名和密码,验证码,是否保存登录信息,登录成功后把用户身份添加到session
    :param request: 这个request里面有post过来的数据
    :return:返回一个字典,代表登录状态,状态说明在msg函数里
    """
    if not verifyTheText(request):
        return msg(3)
    userName = request.POST.get("username", '')  # 获得表单中的用户名
    password = request.POST.get("password", '')  # 获得表单中的密码

    ifSave = request.POST.get("ifsave")
    u = None
    try:
        u = User.objects.get(userName=userName)
    except:
        pass
    if not u:
        return msg(1)
    if u.password != password:
        return msg(2)
    if ifSave == "true":
        request.session.set_expiry(3600 * 24 * 30)
        # 默认是1800秒,选择了保存登录信息,则保存一个月
        # 你可以传递四种不同的值给它：
        # * 如果value是个整数，session会在些秒数后失效（适用于整个Django框架，即这个数值时效时整个页面都会session失效）。
        # * 如果value是个datatime或timedelta，session就会在这个时间后失效。
        # * 如果value是0,用户关闭浏览器session就会失效。
        # * 如果value是None,session会依赖全局session失效策略。
        # response.set_cookie("userName", u.userName)
        # 如果保存信息就存到cookie里,只存用户名,可以使用这个来识别是哪个用户,但是要操作个人信息还是要从新登陆的
    else:
        request.session.set_expiry(0)
        # 没选择保存登录信息,关闭浏览器就失效,下次访问需要重新登录
        # response.delete_cookie("userName")
        # 如果不保存信息就从cookie里删除用户名
        # response.set_cookie("password", user.password, expires=dt)

    user_add_to_session(request, u)
    u.save()  # 保存一下可以更新登录时间
    return msg(0)


def user_logout(request):
    """
    用户登出
    :param request: 提供一个request,这个request里面包含了session.user信息, 当session过期后,就没有session了,也不会提示的.
    :return: 没有返回值
    """
    try:
        del request.session['user']
    except:
        pass