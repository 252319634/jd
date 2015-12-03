# coding:utf-8
from django.db import models

# Create your models here.
class User(models.Model):
    userID = models.AutoField(primary_key=True, unique=True, null=False)
    userName = models.CharField(max_length=30, db_index=True, unique=True, null=False)
    password = models.CharField(max_length=20, null=False)
    registTime = models.DateTimeField(auto_now=True, null=False)
    loginTime = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        db_table = "tb_user"


class Goods(models.Model):
    goodsID = models.AutoField('商品编号', primary_key=True, unique=True, null=False)
    goodsName = models.CharField('商品名称', max_length=30, db_index=True, unique=True, null=False)
    dingjia = models.FloatField('定价', null=False)
    bendianjia = models.FloatField('本店价', null=False)
    shangjiashijian = models.DateField('上架时间', auto_now=True)


    class Meta:
        db_table = "tb_goods"
