from django.urls import reverse_lazy

from django.views.generic import (
    CreateView, DeleteView, ListView, DetailView, UpdateView
)
from .models import Joke
from .forms import JokeForm



class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

class JokeCreateView(CreateView):
    model = Joke
    form_class = JokeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JokeDetailView(DetailView):
    model = Joke

class JokeListView(ListView):
    model = Joke

class JokeUpdateView(UpdateView):
    model = Joke
    form_class = JokeForm

