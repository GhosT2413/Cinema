
from .models import Contact
from django import forms


class Contact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "@" in email:
            raise forms.ValidationError("Please enter a valid email address")
        return email