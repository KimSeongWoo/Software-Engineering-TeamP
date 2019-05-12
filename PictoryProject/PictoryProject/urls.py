"""
Definition of urls for PictoryProject.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.contrib import admin
import Posting.views as post
import Member.views as member

#from django.urls import path 2.0에서 추가된 기능
#url(r'^sum/(?P<x>\d+)/$', views.mysum) : ()안에 d+가 부합한다면, x값을 view로 넘긴다


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #path('admin/', admin.site.urls),

    #-------------Regist, login, logout------------

	url(r'^$',member.home, name ='home'),
    url(r'^register/',member.register,name='register'),
    url(r'^login/',member.loginview,name='login'),
    url(r'^logout/',member.logoutview,name = 'logout'),
   
    #--------------posting----------------
    url(r'^posting',post.posting,name="posting"),

    #--------------profile----------------
    url(r'^my_profile/profile',member.myprofile, name='myprofile'),
    url(r'^user_list/', member.user_list, name="user_list"),
    url(r'^(?P<user_pk>[a-zA-Z0-9]+)/profile',member.user_detail, name='user_detail'),
    

    #---------------edit----------------
    url(r'^proflie/edit',member.profile_edit, name='profile_edit'),
]
