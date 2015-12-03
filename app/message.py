# -*- coding: utf-8 -*-
class Message:
    def __init__(self, state, msg):
        self.state = state
        self.msg = msg

    def getJson(self):
        return "{\"state\":" + str(self.state) + ",\"msg\":\"" + self.msg + "\"}"

# state
# 0:登录成功
# 1:用户名不存在
# 2:密码不正确
# 3:验证码输入错误
# 4:两次密码不匹配
# 5:用户名已存在