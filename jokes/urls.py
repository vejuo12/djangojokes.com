from django.urls import path
from .views import (
    JokeCreateView, JokeDetailView, JokeListView,  JokeUpdateView, JokeDeleteView
)

app_name = 'jokes'

urlpatterns = [
    path('', JokeListView.as_view(), name ='list'),
    path('Joke/<int:pk>', JokeDetailView.as_view(), name ='detail'),
    path('joke/<int:pk>/update/', JokeUpdateView.as_view(), name ='update'),
    path('joke/create/', JokeCreateView.as_view(), name ='create'),
    path('joke/<int:pk>/delete/', JokeDeleteView.as_view(), name ='delete'),
    
]
