from django.contrib import admin

from common.admin import DjangoJokesAdmin
from .models import Joke, JokeVote, Category, Tag

@admin.register(Category)
class CategoryAdmin(DjangoJokesAdmin):
    model = Category
    list_display = ['category', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        return ()
    
@admin.register(Joke)
class JokeAdmin(DjangoJokesAdmin):
    model = Joke

    date_hierarchy = 'updated'
    list_display = ['question', 'created', 'updated']
    list_filter = ['updated', 'category', 'tags']
    ordering = ['-updated']
    search_fields = ['question', 'answer']
    
    
    

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')

        return ()
    
@admin.register(JokeVote)
class JokeVoteAdmin(DjangoJokesAdmin):
    model = JokeVote
    list_display = ['joke', 'user', 'vote']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created', 'updated')
        return ()
    
@admin.register(Tag)
class TagAdmin(DjangoJokesAdmin):
    model: Tag
    list_display = ['tag', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        return ()