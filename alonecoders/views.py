from django.shortcuts import render, get_object_or_404
from .models import Text, User


def get_text_detail(request, text_id):
    text = get_object_or_404(Text, pk=text_id)
    return render(request, 'alonecoders/text_detail.html', {'text': text})


def get_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'alonecoders/author_detail.html', {'user': user})


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
