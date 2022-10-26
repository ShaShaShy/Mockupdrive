from django.forms import ModelForm
from .models import Files, UserUpload

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class UploadForm(ModelForm):
	class Meta:
		model = Files
		fields = '__all__' 


class CreateUserForm (UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class MyUpload(ModelForm):
	class Meta:
		model = UserUpload
		fields = '__all__' 