from django.db import models
from django.conf import settings

# null : True면 db에 null로 저장한다. db에서 null허용시킴
# blank : 빈칸을 허용한다. 필수 필드가 아님을 선언한다.

class Profile(models.Model) :
    #myiamge = imagefield
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #mypw = models.CharField(max_length = 20, blank = True)
    name = models.CharField(max_length = 30, null = True, blank = True)
    email = models.CharField(max_length = 30, null = True, blank = True)
    phone = models.CharField(max_length = 20, null = True, blank = True)
    introduction = models.CharField(max_length = 100, default = '안녕하세요!',blank = True)
    leaveparty = models.BooleanField(default = False); # 탈퇴용 boolean

    def __str__(self):  #profile의 대표적으로 보일 것을 지정하는 것
        return self.owner.username;

    class Meta:
        ordering = ['-owner_id'] #정렬 -면 반대

