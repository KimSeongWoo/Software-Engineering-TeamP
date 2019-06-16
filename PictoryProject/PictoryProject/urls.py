"""
Definition of urls for PictoryProject.
"""
from datetime import datetime
#from django.conf.urls import url
from django.urls import path,include
import django.contrib.auth.views
from django.contrib import admin
import Posting.views as post
import Member.views as member
from django.conf import settings #settings.py에서 설정한 내용 불러옴
from django.conf.urls.static import static  #urlpatterns 연결

#from django.urls import path 2.0에서 추가된 기능
#url(r'^sum/(?P<x>\d+)/$', views.mysum) : ()안에 d+가 부합한다면, x값을 view로 넘긴다


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    path('admin/', admin.site.urls),

    #-------------Regist, login, logout------------

	#url(r'^$',member.home, name ='home'),
    path('',member.home,name='home'),
    #url(r'^register/',member.register,name='register'),
    path('register/',member.register,name='register'),
    #url(r'^login/',member.loginview,name='login'),
    path('login/',member.loginview,name='login'),
    #url(r'^logout/',member.logoutview,name = 'logout'),
    path('logout/',member.logoutview,name='logout'),
   
    #--------------posting----------------
    #url(r'^posting/',post.posting,name='posting'),
    path('posting/',post.posting,name='posting'),
    #url(r'^new/',post.new,name='new'),
    path('posting/new/',post.new,name='new'),
    #url(r'create/',post.create,name='create'),
    path('posting/create/',post.create,name='create'),
    #url(r'delete/(?P<post_id>[a-zA-Z0-9]+)/',post.delete,name='delete_post'),
    path('posting/delete/<int:post_id>/',post.delete,name='delete_post'),
    #url(r'edit/(?P<post_id>[a-zA-Z0-9]+)/',post.edit,name='edit_post'),
    path('posting/edit/<int:post_id>/',post.edit,name='edit_post'),
    #url(r'update/(?P<post_id>[a-zA-Z0-9]+)/',post.update,name='update_post'),
    path('posting/update/<int:post_id>/',post.update,name='update_post'),

    #--------------profile----------------
    #url(r'^my_profile/profile',member.myprofile, name='myprofile'),
    path('my_profile/profile/',member.myprofile,name='myprofile'),
    #url(r'^user_list/', member.user_list, name="user_list"),
    path('my_profile/user_list/',member.user_list,name='user_list'),
    #url(r'^(?P<user_pk>[a-zA-Z0-9]+)/profile',member.user_detail, name='user_detail'),
    path('my_profile/profile/<user_pk>',member.user_detail,name='user_detail'),
    
    #---------------edit----------------
    #url(r'^my_profile/edit',member.profile_edit, name='profile_edit'),
    path('my_profile/edit/',member.profile_edit,name='profile_edit'),
    #url(r'^my_profile/password_edit',member.password_edit, name='password_edit'),
    path('my_profile/password_edit/',member.password_edit,name='password_edit'),
   #url(r'^my_profile/password_edit/error',member.password_edit, name='password_edit_error'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
