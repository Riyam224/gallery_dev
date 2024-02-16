from django.shortcuts import render

# Create your views here.

from .models import Gallery
def index(request):
    photos = Gallery.objects.all()
    context = {
        'photos': photos
    }
    return render(request , 'index.html', context)

