from django import forms

class PaperSubmission(forms.Form):
    paper = forms.FileField()
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    authors_list = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    author_contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    paper_format = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    REVISION_PAPER= (
        ('No', 'No'),
        ('Yes', 'Yes'),
    )

    is_this_a_revision_of_a_previously_submitted_paper = forms.ChoiceField(choices= REVISION_PAPER , widget=forms.Select(attrs={'class': 'form-control'}))
