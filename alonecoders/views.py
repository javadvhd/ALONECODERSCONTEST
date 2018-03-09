from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import *
from .froms import *
# Create your views here.


def login(request):
    return render(request, 'login.html')

def save_user(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Email = request.POST['Email']
        Password = request.POST['Password']
        Student_id = request.POST['Student_id']
        Name = request.POST['Name']
        Major = request.POST['Major']
        User(
            Username=Username,
            Password=Password,
            Email=Email,
            Student_id=Student_id,
            Name=Name,
            Major=Major
        ).save()
