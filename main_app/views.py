from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView
from .models import Wish
from .forms import WishForm

# Create your views here.

def home(request):
    wishlist = Wish.objects.all()
    return render(request, 'index.html', {'wishlist': wishlist})

def add(request):
    form = WishForm(request.POST)
    return render(request, 'add.html', {'form': form})

def wish_create(request):
    form = WishForm(request.POST)
    if form.is_valid():
        new_wish = form.save(commit=False)
        new_wish.save()
    return redirect('home')

class DeleteWish(DeleteView):
    model = Wish
    fields = '__all__'

    success_url = '/'