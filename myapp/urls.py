from django.conf.urls import url
from . import views

urlpatterns = [
	#主页
    url(r'^$', views.index,name="index"),

    #相册信息管理路由
    url(r'^pics/(?P<pIndex>[0-9]+)$', views.pics, name="pics"),#浏览相册信息、数据分页
    url(r'^pics/add$', views.picsAdd, name="picsAdd"),#加载添加表单
    url(r'^pics/insert$', views.picsInsert, name="picsInsert"),#执行相册发布（添加）
    url(r'^pics/delete/(?P<uid>[0-9]+)$', views.picsDelete, name="picsDelete"),#删除相册信息
    url(r'^pics/edit/(?P<uid>[0-9]+)$', views.picsEdit, name="picsEdit"),#加载修改信息(编辑）
    url(r'^pics/update$', views.picsUpdate, name="picsUpdate"),#执行相册修改
]
