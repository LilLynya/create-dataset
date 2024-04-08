from django.shortcuts import render
from django.views import View

from .forms import PhotoForm


# Create your views here.

class PhotoView(View):
    def get(self, request):
        form = PhotoForm()
        return render(request, 'photo.html', context={'form': form})

    def get(self, request):
        form = PhotoForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'photo.html', context={'form': form})

