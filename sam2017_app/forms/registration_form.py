from django import forms
from sam2017_app.forms.validate_name_function import validate_name



class UserRegistrar(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    password_verification = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))

    first_password = ''  # helps as a holder to test the password comparison

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']

        return validate_name(first_name, 'First')

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']

        return validate_name(last_name, 'Last')

    def clean_password(self):
        password = self.cleaned_data['password']

        if len(password) < 6:
            raise forms.ValidationError('Password should contain at least 6 characters.')

        UserRegistrar.first_password = password

        return password

    def clean_password_verification(self):
        password = self.cleaned_data['password_verification']

        if password != UserRegistrar.first_password:
            raise forms.ValidationError('Passwords should be equal')

        return password
