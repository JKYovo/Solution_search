
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.scheme_list),
    # 解决方案搜索
    path('scheme/list', views.scheme_list),
    path('scheme/<int:nid>/edit', views.scheme_edit),
    path('scheme/<int:nid>/delete', views.scheme_delete),
    path('scheme/add', views.scheme_add),
    # 请求搜索
    path('request/list', views.request_list),
    path('request/<int:nid>/edit', views.request_edit),
    path('request/<int:nid>/delete', views.request_delete),
    path('request/add', views.request_add),
    # 帮助
    path('help', views.help),
    # 搜索引擎
    path('search', views.search),




    path('bing/', views.bing, name='bing'),
    path('google/', views.google, name='google'),
    path('', views.baidu, name='search')
]
