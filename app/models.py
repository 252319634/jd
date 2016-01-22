# coding:utf-8
from django.db import models
import datetime
from jd2 import settings


class User(models.Model):
    userID = models.AutoField(primary_key=True, unique=True, null=False)
    userName = models.CharField(max_length=30, db_index=True, unique=True, null=False)
    password = models.CharField(max_length=20, null=False)
    registTime = models.DateTimeField(auto_now_add=True, null=False)
    loginTime = models.DateTimeField(auto_now=True, null=False)
    gbh = models.CommaSeparatedIntegerField('浏览记录', max_length=20, null=True)

    def __str__(self):
        return self.userName

    # @property
    def _get_age(self):
        age = datetime.date().year - self.registTime.year
        return age

    get_age = property(_get_age)
    # get_age.short_description = '用户年龄'

    class Meta:
        db_table = "tb_user"
        verbose_name = '用户'
        verbose_name_plural = '用户'


class UserAuthority():
    # 用户权限
    pass


class GoodsClass(models.Model):
    cid = models.AutoField('分类id', primary_key=True, unique=True, null=False)
    cn = models.CharField('类名', max_length=20, unique=False, null=False)
    gcl = models.SmallIntegerField('分类级别', null=False)
    pid = models.ForeignKey('self', verbose_name='父类', null=False)
    state = models.SmallIntegerField('是否启用', choices=((1, '启用'), (0, '不启用')), null=False, default=1, blank=True)
    # 是否启用该分类
    priority = models.SmallIntegerField('优先级', null=False, default=1, blank=True)
    # 优先级,越小同级排序越靠前
    description = models.TextField('类别描述', null=False, default='描述', blank=True)
    # 想要哪个字段是可选填写的，就在该Model的该字段的选项中（括号内）加上blank=True即可

    def pcn(self):
        # 返回这个类的父类的名称
        return self.pid.cn

    pcn.short_description = '父级名称'  # 定义这个字段的显示名称

    # def get_cn(self):
    # # 给类名前面增加前缀,用来表示级别的缩进
    #     if self.gcl==0:
    #         perfix = ''
    #     elif self.gcl==1:
    #         perfix = '+-'
    #     elif self.gcl==2:
    #         perfix = '+--'
    #     else:
    #         perfix = '+----'
    #
    #     return perfix+self.cn
    # get_cn.short_description = '类名'

    def get_gcl(self):
        # 初始化数据库的分类级别,数据库初始化时才使用.
        # 返回本类的分类级别,(父类的分类级别+1)
        self.gcl = self.pid.gcl + 1
        self.save()

    def __str__(self):
        return self.cn

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # 重写保存方法,计算分类级别.
        # self.pid 是一个GoodsClass的对象, 要用self.pid_id来引用父类的id,相当于self.pid.cid
        self.gcl = self.pid.gcl + 1
        return super(self.__class__, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        db_table = "tb_goodsclass"
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name


class GoodsImg(models.Model):
    """
    商品的图片,一个商品有多个图片
    """
    imgid = models.AutoField('商品图片', primary_key=True)
    goodsid = models.ForeignKey('Goods', null=False)
    imgname = models.CharField('图片名', null=False, max_length=50)
    img = models.ImageField('图片', upload_to='')
    # uplaod_to是指定存储目录,主目录在settings.MEDIA_ROOT定义

    def __str__(self):
        return self.imgname

    class Meta:
        db_table = "tb_goodsimg"
        verbose_name = '商品图片'
        verbose_name_plural = '商品图片'


class Goods(models.Model):
    """
    商品是属于店铺的,比如物品是没有价格的,商品是有价格的,每个店铺的商品的图片不一样,
    上架时间不一样,价格不一样,货号不一样,商品的名字也是自定义的
    """
    # goodsAttribute=
    goodsID = models.AutoField('商品编号', primary_key=True, unique=True, null=False)
    objectID = models.ForeignKey('GoodsObjects', verbose_name='物品', unique=False, null=False)
    goodsName = models.CharField('商品名称', max_length=30, db_index=True, unique=True, null=False)
    price = models.FloatField('定价', default=0.00)
    myprice = models.FloatField('本店价', default=0.00)
    launchdate = models.DateField('上架时间')
    amount = models.IntegerField('库存数量')
    salesquantity = models.IntegerField('销售数量')
    launch = models.BooleanField('是否上架')

    # img = models.ForeignKey('GoodsImg', verbose_name='商品图片')


    def __str__(self):
        return self.goodsName

    class Meta:
        db_table = "tb_goods"
        verbose_name = '商品'
        verbose_name_plural = '商品'


class GoodsAttribute(models.Model):
    """
    物品属性表,用来描述物品时使用的各种特性,品牌就是物品的一个特性
    """
    attributeid = models.AutoField('属性id', primary_key=True)
    goodsclass = models.ForeignKey('GoodsClass', related_name='attr_class')
    attributename = models.CharField('属性名称', max_length=20, null=False)
    filtrate = models.BooleanField('是否筛选', help_text='可以通过这个属性筛选商品')

    @property
    def my_attr_class(self):
        return self.goodsclass.cn

    def __str__(self):
        return self.my_attr_class + "-" + self.attributename

    class Meta:
        db_table = "tb_goodsattribute"
        verbose_name = '分类属性'
        verbose_name_plural = '分类属性'


class AttributeValue(models.Model):
    """
    属性值表,属性的各种可能的值
    """
    attributevalueid = models.AutoField('属性值id', primary_key=True)
    attributenameid = models.ForeignKey('GoodsAttribute', verbose_name='属性名', related_name='value_attr')
    attributevalue = models.CharField('属性值', max_length=50)

    def __str__(self):
        return self.attributevalue

    class Meta:
        db_table = "tb_goodsattributevalue"
        verbose_name = '属性值'
        verbose_name_plural = '属性值'


class GoodsObjects(models.Model):
    """
    物品表,每一个物品都是特性的集合,
    """
    objectsid = models.AutoField('物品编号', primary_key=True, unique=True, null=False)
    objectname = models.CharField('物品名称', max_length=50, null=False)
    objectdescription = models.CharField('物品描述', max_length=500)
    objectclass = models.ForeignKey('GoodsClass', verbose_name='物品分类')
    attributevalue = models.ManyToManyField(AttributeValue, verbose_name='物品属性', null=False)


    def __str__(self):
        return self.objectname

    class Meta:
        db_table = "tb_objects"
        verbose_name = '物品'
        verbose_name_plural = '物品'
