"""
Definition of urls for PictoryProject.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.contrib import admin
import Posting.views
import Login.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$',Login.views.home, name ='home'),
    url(r'^register/',Login.views.register,name='register'),
    url(r'^login/',Login.views.loginview,name='login'),
    url(r'^logout/',Login.views.logoutview,name = 'logout'),
    url(r'^posting/',Posting.views.posting,name="posting"),
]
