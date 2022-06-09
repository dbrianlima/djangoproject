from django import forms
from .models import EmailEntry


class EmailEntryForm(forms.ModelForm):
    class Meta:
        model = EmailEntry
        fields = ['email', 'name', 'bio']

    qs = EmailEntry.objects.filter(email__iexact='email')
    if qs.exists():
        raise forms.ValidationError(
            'Thank you, you already have an email entry')
