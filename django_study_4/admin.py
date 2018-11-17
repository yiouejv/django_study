from django.contrib import admin
from .models import *

# Register your models here.


# 定义高级管理类
class AuthorAdmin(admin.ModelAdmin):
    # 定义显示在列表页上的字段们
    list_display = ['name', 'email', 'age']

    # 定义列表页上也能够链接到详情页的字段们
    list_display_links = ['name', 'email']

    # 定义在列表也上就能修改的字段们
    list_editable = ['age']

    # 定义允许搜索的字段值们
    search_fields = ['age', 'email', 'name']

    # 在列表页中添加过滤器
    list_filter = ['age', 'name']

    # 在详情页上显示的顺序
    # fields = ['name', 'age', 'email']

    # # 创建详情页分组
    # fieldsets = [
    #     ('分组1',{
    #         'fields': ['name'],
    #         'classes': [],
    #     }),
    #
    #     ['分组2',{
    #         'fields': ['age'],
    #         'classes': ['collapse']
    #     }],
    #
    #     ['分组3', {
    #         'fields': ['email'],
    #         'classes': ['collapse']
    #     }]
    # ]


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publicate_date']
    list_filter = ['publisher', 'title']

    # 添加时间选择器
    date_hierarchy = 'publicate_date'


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city', 'country', 'website']
    list_display_links = ['website']
    list_editable = ['address', 'city']
    list_filter = ['city']
    search_fields = ['name', 'website']
    fieldsets = [
        ['基本选项', {
            'fields': ['name', 'address', 'city'],
            'classes': [],
        }],
        ['高级选项', {
            'fields': ['country', 'website'],
            'classes': ['collapse']
        }]
    ]


class WifeAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']


# 注册要管理的Models类，只有注册之后才能管理
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Wife, WifeAdmin)

