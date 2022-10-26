from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, UploadForm, MyUpload
from .models import Files, UserUpload

import os
from django.conf import settings
from django.http import HttpResponse, Http404

# Create your views here.


def registerPage(request):
	if request.user.is_authenticated:
		return redirect ('userDashboard')
	else:
		form = CreateUserForm()

		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for' + user)
				return redirect('login')
		context = {'form':form}
		return render(request, 'register.html',context)


def userLogin(request):
	if request.user.is_authenticated:
		return redirect ('userDashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username,password=password)

			if user is not None:
				login(request, user)
				return redirect('userDashboard')
			else:
				messages.info(request, 'Username or Password is Incorrect!')


		context = {}
		return render(request, 'index.html', context
)

def logoutUser(request):
	logout(request)
	return redirect('login')


def Register(request):
	return render(request, 'register.html', {}
)

@login_required(login_url='/Login/')
def userDash(request):
	users = UserUpload.objects.all()
	return render(request, 'userDashboard.html', {'users':users}
)

@login_required(login_url='/Login/')
def uploadFile(request):

	form = MyUpload()
	totalNum = UserUpload.objects.count()
	totalSize = os.path.getsize('media')


	if request.method == 'POST':
		form = MyUpload(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Data has been Saved!')
			form = MyUpload()
	return render(request, 'upload.html', {'form':form, 
		'totalNum':totalNum, 'totalSize':totalSize}
)

def onDelete(request, pk):

	userDelete = UserUpload.objects.get(id=pk)
	userDelete.delete()
	return redirect('userDashboard')


def updateFile(request,pk):

	myupdate = UserUpload.objects.get(id=pk)
	form = MyUpload(instance=myupdate)

	if request.method == 'POST':
		form = MyUpload(request.POST, instance=myupdate)
		if form.is_valid():
			form.save()
			messages.success(request, 'Data has been Updated!')
			return redirect('userDashboard')
	return render(request, 'edit.html', {'form':form}
)




