# -*- coding=utf-8 -*-
from django.contrib import admin

from .models import *


class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 0
    show_change_link = True


class GoodsImgInline(admin.TabularInline):
    model = GoodsImg
    extra = 0
    show_change_link = True


class GoodsclassInline(admin.TabularInline):
    model = GoodsClass
    fields = ('cn',)  # 外键关系模型列表中显示的字段
    extra = 0
    verbose_name = '子类'
    show_change_link = True


class GoodsAttrInline(admin.TabularInline):
    # admin.StackedInline   admin.TabularInline
    # 这个类可以继承自两个类,他们的区别是显示的样子不一样,一个水平显示一个模型,一个是垂直显示一个模型
    model = GoodsAttribute  # 修改主模型时同时显示的外键关系模型,
    fields = ('attributename',)  # 外键关系模型列表中显示的字段
    extra = 0  # 用于添加外键关系模型的空行
    verbose_name = '类别属性'  # 外键关系模型列表最下面的添加另外一个***,所用的名字
    show_change_link = True  # 显示修改连接,这个很有用啊!!!!
    can_delete = False  # 是否显示删除框
    fk_name = "goodsclass"  #


class GoodsAdmin(admin.ModelAdmin):
    inlines = [GoodsImgInline]


class GoodsAttributeAdmin(admin.ModelAdmin):
    inlines = [AttributeValueInline]  # Inline
    list_display = ('my_attr_class', 'attributename')
    search_fields = ('attributename',)
    # list_filter = ('gc',)


class GoodsClassAdmin(admin.ModelAdmin):
    inlines = [GoodsclassInline, GoodsAttrInline]  # 修改模型时同时在页面内显示的外键模型
    fields = ('pid','gcl','cn','state','priority','description')  # 修改模型时显示的字段
    raw_id_fields = ('pid',)  # 字段显示成下拉列表还是搜索项
    list_display = ('pcn', 'cid', 'cn', )  # 列表页显示的字段
    list_display_links = ('cn',)  # 列表页显示的字段中带连接的字段
    list_filter = ('gcl',)  # 列表页过滤选项,
    search_fields = ('cn',)  # 列表页搜索框
    ordering = ('cid',)  # 列表页的默认排序方式,加负号表示降序
    # list_select_related = True
    # list_editable = ('cn',)  # 列表页就可以修改的字段,不能和带连接选项同时使用

    def get_readonly_fields(self, request, obj=None):
        return ['gcl']


class GoodsObjectsAdmin(admin.ModelAdmin):
    filter_horizontal = ('attributevalue',)  # 模型修改页面中,monytomonyfield字段的显示成水平方式


  # 先上代码，在讲解
class BlogArticleAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sort_id":
            kwargs["queryset"] = Tags.objects.filter(user=request.user)
        return super(BlogArticleAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # formfield_for_foreignkey该方法和其他方法（delete model ,save_model()方法一样，都会django 内置的
    # db_field.name == "sort_id":设置数据字段，也就是外键
    # kwargs["queryset"] = Tags.objects.filter(user=request.user)定义过滤方案
    # 返回结果。。。。




admin.site.register(User)
admin.site.register(GoodsClass, GoodsClassAdmin)
admin.site.register(GoodsAttribute, GoodsAttributeAdmin)
admin.site.register(AttributeValue)
admin.site.register(GoodsObjects, GoodsObjectsAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsImg)
