
from django.forms import ModelForm
from django.contrib.auth.models import User
from Member.models import Profile

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        
class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

 #pw변경은 set_password(raw_password)을 사용
class PasswordModifyForm(ModelForm) :
    class Meta :
        model = User
        fields = ["password"]

#-------------profile--------------

class ProfileShowForm(ModelForm): #변경도 일단은 동일하게
    class Meta:
        model = Profile
        fields = ['name','email','phone','introduction']

class ProfileModifyForm(ModelForm) :
    class Meta:
        model = Profile
        fields = ['name','email','phone','introduction'] 
        #leaveparty는 차후 수정, isactive 필드를 false하는것이 바람직하다고 함


