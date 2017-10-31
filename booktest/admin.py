#encoding:utf-8
from django.contrib import admin

# Register your models here.
#注：引用当前项目下模块，2.7.x版本直接from模块名即可，而3.x需要.模块名
from models import *
#自定义admin模块显示：1.创建自定义模块类(继承自admin.ModelAdmin) 2.注册

#嵌入类(继承自admin.StackedInline即为列表展示效果,继承自admin.TabularInline为表格显示效果)
class HeroInfoInline(admin.TabularInline):
    model = Hero#注册嵌入模型类
    extra = 3#注册展示几个

class Bookinfoadmin(admin.ModelAdmin):
    #1.列表显示页面自定义：

    #list_display显示字段
    list_display = ['id','bname','bpub_date']
    #list_filter条件过滤字段
    list_filter = ['bname']
    #search_fields搜索过滤字段
    search_fields = ['bname']
    #list_per_page分页页码数
    list_per_page = 10
    #2.修改页面分组展示
    fieldsets = [
        ('基础',{'fields':['bname']}),
        ('时间',{'fields':['bpub_date']})
    ]
    #inlines注册嵌入类
    inlines = [HeroInfoInline]
admin.site.register(Book,Bookinfoadmin)
admin.site.register(Hero)
