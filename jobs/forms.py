from django import forms

class JobAplicationForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(
        required=False,
        label="Website",
    )
    EMPLOYMENT_CHOICES = [
        (None, '--Please choose--'),
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract work'),
    ]

    employment_type = forms.ChoiceField(
        choices=EMPLOYMENT_CHOICES,
        label="Employment Type"
    )

    start_date = forms.DateField(
        label="Start Date",
        help_text="The earliest date you can start working.",
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
        label="Available Days"
    )

    desired_hourly_wage = forms.DecimalField(
        label="Desired Hourly Wage",
        max_digits=6,   
        decimal_places=2,  
        min_value=0,
    )

    cover_letter = forms.CharField(label="Cover Letter")

    confirmation = forms.BooleanField(
        required=True,
        label="I certify that the information I have provided is true.",
        error_messages={
            'required': 'You must certify that the information is true.'
        }
    )