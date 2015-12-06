# -*- coding: utf-8 -*-
import datetime
from django.shortcuts import render, render_to_response, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from app.models import *
from app.forms import *
from app.userSession import UserSession
from django.http import JsonResponse
from app.verify_gen import get_verify
from app.user_tools import *

def admin_index(request):
    return render_to_response('admin_index.html', locals(), context_instance=RequestContext(request))


def admin_goods(request):
    return render_to_response('admin_goods.html', locals(), context_instance=RequestContext(request))

def admin_goodsclass(request):
    return render_to_response('admin_goodsclass.html', locals(), context_instance=RequestContext(request))

def admin_user(request):
    users = User.objects.all()
    return render_to_response('admin_user.html', locals(), context_instance=RequestContext(request))