from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import *
from .froms import *
# Create your views here.


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            Username = form.cleaned_data['Username']
            Email = form.cleaned_data['Email']
            Password = form.cleaned_data['Password']
            Student_id = form.cleaned_data['Student_id']
            Name = form.cleaned_data['Name']
            Major = form.cleaned_data['Major']

            User(
                Username=Username,
                Password=Password,
                Email=Email,
                Student_id=Student_id,
                Name=Name,
                Major=Major
            ).save()
            return HttpResponse('/tanks/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})