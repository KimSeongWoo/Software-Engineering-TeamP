from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date=models.DateTimeField('ch add date')
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    like=models.IntegerField(default=0)
    TMP=models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #포스트를 user와 연결

    def __str__(self):     
        return self.title

class Comment(models.Model):
    body = models.TextField()
    #Blog모델과 관계설정 1:N에서 N의 속성으로 들어간다
    #on_delete:Blog객체 삭제되면 관련 클래스도 사라지는거
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)  #comment를 포스트랑 연결
    
    def __str__(self):
        return self.body