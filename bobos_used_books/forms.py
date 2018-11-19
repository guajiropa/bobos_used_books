"""
AUTHOR      :   Robert James Patterson
DATE        :   11/17/2018
SYNOPSIS    :   Work-thru file for 'Mastering Django: Core'.
"""
from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(min_length=3, max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.clean_data['message']
        num_words = len(message.split( ))

        if num_words < 4:
            raise forms.ValidationError("Message must contain at lest four words!")

        return message
        