from django.shortcuts import render
from .models import Text


def get_text_detail(request, text_id):
    text = Text.objects.get(pk=text_id)
    return render(request, 'alonecoders/text_detail.html', {'text': text})
