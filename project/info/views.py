from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from django.contrib.auth.models import User,auth
from .models import Container
#from .cryptography_function import Encryptor
from cryptography.fernet import Fernet
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
def login(request):
    if request.method=='POST':
        user = request.POST['username']
        pass_1 = request.POST['password']
        user = auth.authenticate(username = user,password=pass_1)
        if user is not None:
            auth.login(request,user)
            return render(request,'home.html')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    return render(request,'home.html')

def upload_file(request):
    return render(request,'upload.html')

def encrypt(request):
    if request.method == "POST":
        input_file = request.FILES['file']
        key = Fernet.generate_key()
        with open(input_file, 'rb') as f:
            file_data = f.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(file_data)
        with open(input_file, 'wb') as f:
            f.write(encrypted)
        obj = Container(file_field = input_file)
        obj.save()
        
    return render(request,'success.html')


def view_file(request):
    return render(request,'view.html')

def download(request):
    row = Container.objects.all()
    return render(request,'download.html', {'data':row})


