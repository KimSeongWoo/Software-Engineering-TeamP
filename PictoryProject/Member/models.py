from django.db import models
from django.conf import settings

# null : True면 db에 null로 저장한다. db에서 null허용시킴
# blank : 빈칸을 허용한다. 필수 필드가 아님을 선언한다.

class Profile(models.Model) :
    #myiamge = imagefield
    myid = models.ForeignKey(settings.AUTH_USER_MODEL)
    #mypw = models.CharField(max_length = 20, blank = True)
    myname = models.CharField(max_length = 30, null = True, blank = True)
    myemail = models.CharField(max_length = 30, null = True, blank = True)
    myphone = models.CharField(max_length = 20, null = True, blank = True)
    introduction = models.CharField(max_length = 100, default = '안녕하세요!',blank = True)
    leaveparty = models.BooleanField(default = False); # 탈퇴용 boolean

    def __str__(self):  #User의 대표적으로 보일 것을 지정하는 것
        return self.myname;

