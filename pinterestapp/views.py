from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from .models import ImageModel


def index(request):
    images = ImageModel.objects.all()
    return render(request, 'index.html', {'images': images})


def about(request):
    return render(request, 'about.html')


def SearchView(request):
    search = ''
    images_search = ImageModel.objects.filter(name__contains=search)
    if request.method == 'POST':
        search = request.POST.get('search', '')
        if search:
            images_search = ImageModel.objects.filter(name__contains=search)
    return render(request, 'search.html', {
        'search': search,
        'images_search': images_search
    })


def SingleView(request, id):
    images = ImageModel.objects.filter(id=id)
    return render(request, 'single.html', {'images': images})


class add(CreateView):
    model = ImageModel
    template_name = 'add_image.html'
    fields = ['image', 'name', 'description']
    success_url = reverse_lazy('index')


class delete(DeleteView):
    model = ImageModel
    template_name = 'delete_image.html'
    success_url = reverse_lazy('index')
