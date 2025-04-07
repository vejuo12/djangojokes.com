from django.forms import Textarea, ModelForm

from .models import Joke

class JokeForm(ModelForm):
    class Meta:
        model = Joke
        fields = ['question', 'answer', 'category']
        widgets = {
            'question': Textarea(
                attrs={'cols': 80, 'rows': 3, 'autofocus': True}
            ),
            'answer': Textarea(
                attrs={'cols': 80, 'rows': 2, 'placeholder': 'Make it Funny!'}
            )
        }
        help_texts = {'question': 'No dirty jokes please.'}