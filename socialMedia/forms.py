from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    description2 = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Please enter the  description'}))

class loginForm(forms.Form):
    userName = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
