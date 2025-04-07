import datetime
from django import forms

class JobAplicationForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True
            }
        )
    )

    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                'size': '50'
            }
        )
        
    )
    EMPLOYMENT_CHOICES = [
        (None, '--Please choose--'),
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract work'),
    ]

    employment_type = forms.ChoiceField(
        choices=EMPLOYMENT_CHOICES,
    )
    current_year = datetime.datetime.now().year
    next_year = current_year + 1

    start_date = forms.DateField(
        help_text="The earliest date you can start working.",
        widget=forms.SelectDateWidget(
            years=[current_year, next_year]
        )
        
    )
    
    WEEKDAY_CHOICES = [
        ('MON', 'Mon'),
        ('TUE', 'Tue'),
        ('WED', 'Wed'),
        ('THU', 'Thu'),
        ('FRI', 'Fri'),
    ]

    available_days = forms.MultipleChoiceField(
        choices=WEEKDAY_CHOICES,
        help_text="Select all days that you can work.",
        widget=forms.CheckboxSelectMultiple(
            attrs={'checked':True}
        )
    )

    desired_hourly_wage = forms.DecimalField(
        max_digits=6,   
        decimal_places=2,  
        min_value=0,
        widget=forms.NumberInput(
            attrs={'min' : '10', 'max': '100', 'step' : '.25'}
        )
        
    )

    cover_letter = forms.CharField(
        widget=forms.Textarea(
            attrs={'cols': '75', 'rows': '5'}
        )
    )

    confirmation = forms.BooleanField(
        required=True,
        label="I certify that the information I have provided is true.",
        error_messages={
            'required': 'You must certify that the information is true.'
        }
    )