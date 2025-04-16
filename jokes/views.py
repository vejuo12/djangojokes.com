from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView, DeleteView, ListView, DetailView, UpdateView
)
from .models import Joke
from .forms import JokeForm



class JokeDeleteView(UserPassesTestMixin, DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        return result

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Joke deleted.')
        return super().form_valid(form)

class JokeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Joke
    form_class = JokeForm
    success_message = 'Joke created Successfully'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JokeDetailView(DetailView):
    model = Joke

class JokeListView(ListView):
    model = Joke

class JokeUpdateView(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Joke
    form_class = JokeForm
    success_message = 'Joke updated Successfully'

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user