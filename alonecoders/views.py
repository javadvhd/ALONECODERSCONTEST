from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Text, User


def get_text_detail(request, text_id):
    text = get_object_or_404(Text, pk=text_id)
    return render(request, 'alonecoders/text_detail.html', {'text': text})


def get_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'alonecoders/*.html', {'user': user})


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