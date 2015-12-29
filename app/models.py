# coding:utf-8
from django.db import models


class User(models.Model):
    userID = models.AutoField(primary_key=True, unique=True, null=False)
    userName = models.CharField(max_length=30, db_index=True, unique=True, null=False)
    password = models.CharField(max_length=20, null=False)
    registTime = models.DateTimeField(auto_now_add=True, null=False)
    loginTime = models.DateTimeField(auto_now=True, null=False)
    gbh = models.CommaSeparatedIntegerField('浏览记录', max_length=20, null=True)

    def __str__(self):
        return self.userName

    class Meta:
        db_table = "tb_user"


class GoodsClass(models.Model):
    pid = models.SmallIntegerField('父级分类id', null=False, default=0)
    gcl = models.SmallIntegerField('分类级别', null=False)
    cid = models.AutoField('分类id', primary_key=True, unique=True, null=False)
    cn = models.CharField('类名', max_length=20, unique=False, null=False)
    state = models.SmallIntegerField('是否启用', null=False, default=1)
    # 是否启用该分类
    priority = models.SmallIntegerField('优先级', null=False, default=1)
    # 优先级,越小同级排序越靠前
    description = models.TextField('类别描述', null=False)

    def __str__(self):
        return self.cn

    class Meta:
        db_table = "tb_goodsclass"


class Goods(models.Model):
    """
    商品是属于店铺的,下面的属性都是店铺定义的,

    """
    # goodsAttribute=
    goodsID = models.AutoField('商品编号', primary_key=True, unique=True, null=False)
    classID = models.SmallIntegerField('商品分类', unique=False, null=False)
    goodsName = models.CharField('商品名称', max_length=30, db_index=True, unique=True, null=False)
    price = models.FloatField('定价', null=False)
    myprice = models.FloatField('本店价', null=False)
    launchdate = models.DateField('上架时间', auto_now=True)

    def __str__(self):
        return self.goodsName

    class Meta:
        db_table = "tb_goods"


class GoodsAttribute(models.Model):
    attributeid = models.IntegerField('属性id', primary_key=True)
    goodsclass = models.ForeignKey(GoodsClass, related_name='attr_class')
    attributename = models.CharField('属性名称', max_length=20, null=False)

    def __str__(self):
        return self.attributename

    class Meta:
        db_table = "tb_goodsattribute"


class AttributeValue(models.Model):
    attributevalueid = models.IntegerField('属性值id', primary_key=True)
    attributenameid = models.ForeignKey(GoodsAttribute, related_name='value_attr')
    attributevalue = models.CharField('属性值', max_length=50)

    def __str__(self):
        return self.attributevalue

    class Meta:
        db_table = "tb_goodsattributevalue"


