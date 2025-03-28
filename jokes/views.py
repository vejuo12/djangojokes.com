from django.urls import reverse_lazy

from django.views.generic import (
    CreateView, DeleteView, ListView, DetailView, UpdateView
)
from .models import Joke



class JokeDeleteView(DeleteView):
    model = Joke
    success_url =reverse_lazy('jokes:list')

class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer']

class JokeDetailView(DetailView):
    model = Joke

class JokeListView(ListView):
    model = Joke

class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']

