# coding:utf-8
from django.db import models

# Create your models here.
class User(models.Model):
    userID = models.AutoField(primary_key=True, unique=True, null=False)
    userName = models.CharField(max_length=30, db_index=True, unique=True, null=False)
    password = models.CharField(max_length=20, null=False)
    registTime = models.DateTimeField(auto_now=True, null=False)
    loginTime = models.DateTimeField(auto_now=True, null=False)
    gbh = models.CommaSeparatedIntegerField(max_length=20, null=True)

    def __str__(self):
        return self.userName

    class Meta:
        db_table = "tb_user"


class GoodsClass(models.Model):
    classID = models.AutoField(primary_key=True, unique=True, null=False)
    classL1 = models.SmallIntegerField('一级分类', unique=True, null=True)
    classL2 = models.SmallIntegerField('二级分类', unique=True, null=True)
    classL3 = models.SmallIntegerField('三级分类', unique=True, null=True)
    className = models.CharField('类名', max_length=20, unique=True, null=False)

    def __str__(self):
        return self.className

    class Meta:
        db_table = "tb_goodsclass"


class Goods(models.Model):
    goodsID = models.AutoField('商品编号', primary_key=True, unique=True, null=False)
    classID = models.SmallIntegerField('分类', unique=False, null=False)
    goodsName = models.CharField('商品名称', max_length=30, db_index=True, unique=True, null=False)
    dingjia = models.FloatField('定价', null=False)
    bendianjia = models.FloatField('本店价', null=False)
    shangjiashijian = models.DateField('上架时间', auto_now=True)

    def __str__(self):
        return self.goodsName

    class Meta:
        db_table = "tb_goods"

