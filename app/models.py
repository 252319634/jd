# coding:utf-8
from django.db import models

# Create your models here.
class User(models.Model):
    userID = models.AutoField(primary_key=True, unique=True, null=False)
    userName = models.CharField(max_length=30, db_index=True, unique=True, null=False)
    password = models.CharField(max_length=20, null=False)
    registTime = models.DateTimeField(auto_now_add=True, null=False)
    loginTime = models.DateTimeField(auto_now=True, null=False)
    gbh = models.CommaSeparatedIntegerField(max_length=20, null=True)

    def __str__(self):
        return self.userName

    class Meta:
        db_table = "tb_user"


class GoodsClass(models.Model):
    pid = models.SmallIntegerField('父级分类id', null=False, default=0)
    gcl = models.SmallIntegerField('分类级别',null=False)
    cid = models.AutoField('分类id',primary_key=True, unique=True, null=False)
    cn = models.CharField('一级类名', max_length=20, unique=False, null=False)
    state = models.SmallIntegerField('是否启用', null=False, default=1)
    # 是否启用该分类
    priority = models.SmallIntegerField('优先级', null=False, default=1)
    # 优先级,越小同级排序越靠前
    description = models.TextField('类别描述',null=False)
    def __str__(self):
        return self.cn

    class Meta:
        db_table = "tb_goodsclass"


# class GCL2(models.Model):
#     pid = models.SmallIntegerField('父类id', unique=False, null=False)
#     cid = models.AutoField(primary_key=True, unique=True, null=False)
#     cn = models.CharField('二级类名', max_length=20, unique=True, null=False)
#     state = models.SmallIntegerField('是否启用', null=False, default=1)
#
#     # 是否启用该分类
#     priority = models.SmallIntegerField('优先级', null=False, default=1)
#     # 优先级,越小同级排序越靠前
#     def __str__(self):
#         return self.className
#
#     class Meta:
#         db_table = "tb_gcl2"
#
#
# class GCL3(models.Model):
#     pid = models.SmallIntegerField('父类id', unique=False, null=False)
#     # 父级cid
#     cid = models.AutoField(primary_key=True, unique=True, null=False)
#     cn = models.CharField('类名', max_length=20, unique=False, null=False)
#     # 本分类名称
#     state = models.SmallIntegerField('是否启用', null=False, default=1)
#     # 是否启用该分类
#     priority = models.SmallIntegerField('优先级', null=False, default=1)
#     # 优先级,越小同级排序越靠前
#
#     def __str__(self):
#         return self.cn
#
#     class Meta:
#         db_table = "tb_gcl3"


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

