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


# class GoodsClassL1(models.Model):
# classID = models.AutoField(primary_key=True, unique=True, null=False)
#     classL1 = models.SmallIntegerField('一级分类', unique=True, null=True)
#     className = models.CharField('一级类名', max_length=20, unique=True, null=False)
#
#     def __str__(self):
#         return self.className
#
#     class Meta:
#         db_table = "tb_goodsclassl1"
#
#
# class GoodsClassL2(models.Model):
#     classID = models.AutoField(primary_key=True, unique=True, null=False)
#     classL1 = models.SmallIntegerField('一级分类', unique=True, null=True)
#     classL2 = models.SmallIntegerField('二级分类', unique=True, null=True)
#     className = models.CharField('二级类名', max_length=20, unique=True, null=False)
#
#     def __str__(self):
#         return self.className
#
#     class Meta:
#         db_table = "tb_goodsclassl2"

class GoodsClass(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    pid = models.SmallIntegerField('父级cid', unique=False, null=False)
    # 父级cid
    cn = models.CharField('类名', max_length=20, unique=False, null=False)
    # 本分类名称
    state = models.SmallIntegerField('是否启用', null=False, default=1)
    # 是否启用该分类
    priority = models.SmallIntegerField('优先级', null=False, default=1)
    # 优先级,越高同级排序越靠前

    def __str__(self):
        return self.cn

    class Meta:
        db_table = "tb_goodsclass"
# 原始的分类模型
# class GoodsClass(models.Model):
#     id = models.AutoField(primary_key=True, unique=True, null=False)
#     pid = models.SmallIntegerField('父级cid', unique=False, null=False)
#     # 父级cid
#     cid = models.SmallIntegerField('id', unique=True, null=False)
#     # 本分类的全id
#     cn = models.CharField('类名', max_length=20, unique=False, null=False)
#     # 本分类名称
#     state = models.SmallIntegerField('是否启用', null=False, default=1)
#     # 是否启用该分类
#     priority = models.SmallIntegerField('优先级', null=False, default=1)
#     # 优先级,越高同级排序越靠前
#
#     def __str__(self):
#         return self.cn
#
#     class Meta:
#         db_table = "tb_goodsclass"

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

