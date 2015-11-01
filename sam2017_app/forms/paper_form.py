from django import forms

# form found in the login page
class PaperSubmission(forms.Form):
    paper = forms.FileField()
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    authors_list = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    author_contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    paper_format = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))





# end UserLogger