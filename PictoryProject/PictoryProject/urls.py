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
    url(r'^profile/my_profile/',member.myprofile, name='myprofile'),
    #url(r'^profile/(?P<userid>[a-zA-Z0-9]+)',member.profile_detail, name='profile_detail'),
    

    #---------------edit----------------
    url(r'^profile/my_profile/edit',member.profile_edit, name='profile_edit'),
]
