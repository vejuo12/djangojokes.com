from django.urls import path
from .views import (
    JokeCreateView, JokeDetailView, JokeListView,  JokeUpdateView
)

app_name = 'jokes'

urlpatterns = [
    path('', JokeListView.as_view(), name ='list'),
    path('Joke/<int:pk>/', JokeDetailView.as_view(), name = 'detail'),
    path('joke/<int:pk>', JokeUpdateView.as_view(), name = 'update'),
    path('joke/create', JokeCreateView.as_view(), name='create'),
    
]
