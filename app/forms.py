# -*- coding: utf-8 -*-
from django import forms


class AddForm(forms.Form):
    title = forms.CharField(max_length=150, label='标题', error_messages={'required': '请输入题目'})
    body = forms.CharField(widget=forms.Textarea, max_length=10000, label='正文', error_messages={'required': '请输入内容'})


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='用户名', error_messages={'required': '请输入用户名'})
    password = forms.CharField(widget=forms.PasswordInput, max_length=20, label='密码',
                               error_messages={'required': '请输入密码'})
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label='用户名', error_messages={'required': '请输入用户名'})
    password1 = forms.CharField(widget=forms.PasswordInput, max_length=20, label='密码',
                               error_messages={'required': '请输入密码'})
    password2 = forms.CharField(widget=forms.PasswordInput, max_length=20, label='密码',
                               error_messages={'required': '请输入密码'})

class ChangePassWordForm(forms.Form):
    password0 = forms.CharField(widget=forms.PasswordInput, max_length=30, label='原密码',
                                error_messages={'required': '请输入原密码'})
    password1 = forms.CharField(widget=forms.PasswordInput, max_length=20, label='新密码',
                                error_messages={'required': '请输入新密码'})
    password2 = forms.CharField(widget=forms.PasswordInput, max_length=20, label='重复密码',
                                error_messages={'required': '请重复新密码'})