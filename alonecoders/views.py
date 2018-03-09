from django.shortcuts import render, get_object_or_404
from .models import Text, User


def get_text_detail(request, text_id):
    text = get_object_or_404(Text, pk=text_id)
    return render(request, 'alonecoders/text_detail.html', {'text': text})


def get_profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'alonecoders/*.html', {'user': user})
