from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Article
from django.urls import reverse_lazy
from django import forms
# Create your views here.
class ArtecilList(ListView):
    model = Article
    template_name = 'artecil_list.html'

class CreateView(CreateView):
    model = Article
    template_name = "creat_list.html"
    fields = ( 'title', 'summer', 'img', 'body', )
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)