from django.shortcuts import render
from .models import MultimediaItem

def index(request):
    items = MultimediaItem.objects.all()
    return render(request, 'media_app/index.html', {'items': items})