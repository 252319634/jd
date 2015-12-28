# -*- coding: utf-8 -*-
import datetime
import json
from django.core import serializers
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
    if request.method == "GET":
        return render_to_response('admin_goods.html', locals(), context_instance=RequestContext(request))
    if request.method == "POST":
        return JsonResponse({'state': 0, 'msg': '商品信息!'})


def admin_goodsclass(request, cid):
    if request.method == 'GET':
        if cid:
            try:
                gc = GoodsClass.objects.get(cid=cid)
                if gc.gcl == 3:
                    gcp = GoodsClass.objects.get(cid=gc.pid)
                    gcpp = GoodsClass.objects.get(cid=gcp.pid)
                if gc.gcl == 2:
                    gcp = GoodsClass.objects.get(cid=gc.pid)
            except:
                gc = ''
            return render_to_response('admin_goodsclassedit.html', locals(), context_instance=RequestContext(request))
        gcs = GoodsClass.objects.all()
        return render_to_response('admin_goodsclass.html', locals(), context_instance=RequestContext(request))
    if request.method == 'POST':
        post_method = request.POST.get('method', '')
        print(post_method)
        # if post_method == 'load':
        # pid = request.POST.get('pid', '')  # 得到传回来的pid
        # if not pid:
        #         return HttpResponse('')
        #         # gcs_json = serializers.serialize('json', gcl1)
        #         # return HttpResponse(gcs_json)
        if post_method == 'save':
            gc_cid = request.POST.get('gc_cid', 'None')
            gc_cn = request.POST.get('gc_cn', 'None')
            gc_state = request.POST.get('gc_state', 'None')
            gc_priority = request.POST.get('gc_priority', 'None')
            if not (gc_cid and gc_cn and gc_state and gc_priority):
                return JsonResponse({'state': 1, 'msg': '修改失败!,信息不够'})
            if gc_cid:
                try:
                    gc = GoodsClass.objects.get(cid=gc_cid)
                except:
                    return JsonResponse({'state': 1, 'msg': '修改失败,分类id错误'})
                if gc:
                    gc.cn = gc_cn
                    gc.state = gc_state
                    gc.priority = gc_priority
                    gc.save()
                    return JsonResponse({'state': 0, 'msg': '修改成功!'})

        if post_method == 'add':
            # gc_id = request.POST.get('gc_id')
            gc_pid = request.POST.get('gc_pid', 'None')
            gc_cn = request.POST.get('gc_cn', 'None')
            gc_state = request.POST.get('gc_state', 'None')
            gc_priority = request.POST.get('gc_priority', 'None')
            if not (gc_pid and gc_cn and gc_state and gc_priority):
                return JsonResponse({'state': 1, 'msg': '添加失败!,信息不够'})
            gcp = GoodsClass.objects.get(cid=gc_pid)
            gc = GoodsClass(gcl=gcp.gcl + 1, pid=gc_pid, cn=gc_cn, state=gc_state, priority=gc_priority)
            gc.save()
            return JsonResponse({'state': 0, 'msg': '添加成功!'})
            # return JsonResponse({'state': 0, 'msg': '添加成功!'})

        if post_method == 'del':
            gc_cid = request.POST.get('gc_cid')
            if gc_cid:
                gc = GoodsClass.objects.filter(cid=gc_cid)
                if gc[0].gcl == 3:
                    gc[0].delete()
                    return JsonResponse({'state': 0, 'msg': '删除成功!'})
                elif GoodsClass.objects.filter(pid=gc[0].cid):
                    return JsonResponse({'state': 1, 'msg': '删除失败,此类下有子分类!'})
                    # return JsonResponse({'state': 0, 'msg': '删除成功!'})


def admin_goodsclassedit(request):
    if request.method == 'GET':
        cid = request.REQUEST.get('cid', '')
        if cid:
            pass
        return render_to_response('admin_goodsclassedit.html', locals(), context_instance=RequestContext(request))


def admin_user(request):
    """
    用户管理页面的功能,包括读取,修改,删除用户信息
    :param request:
    :return:
    """
    if request.method == 'GET':
        users = User.objects.all()
        return render_to_response('admin_user.html', locals(), context_instance=RequestContext(request))
    if request.method == 'POST':
        post_method = request.POST.get('method', '')
        # print(post_method)
        if post_method == 'save':
            u = User.objects.filter(userName=request.POST.get('user_name', ''))
            p = request.POST.get('user_password', '')
            if len(u) == 1 and p:
                u[0].password = p
                u[0].save()
                return JsonResponse({'state': 0, 'msg': '保存成功!'})
        if post_method == 'del':
            u = User.objects.filter(userID=request.POST.get('user_id', ''))
            u.delete()
            return JsonResponse({'state': 0, 'msg': '删除成功!'})
            pass
        if post_method == 'load':
            pass
        return JsonResponse({'state': 0, 'msg': '保存成功!'})
