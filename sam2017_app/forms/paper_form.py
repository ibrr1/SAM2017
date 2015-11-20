from django import forms


class PaperSubmission(forms.Form):
    paper = forms.FileField()
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    authors_list = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    author_contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    PAPER_FORMAT= (
        ('PDF', 'PDF'),
        ('DOC', 'DOC'),
    )

    REVISION_PAPER= (
        ('No', 'No'),
        ('Yes', 'Yes'),
    )

    paper_format = forms.ChoiceField(choices=PAPER_FORMAT, widget=forms.Select(attrs={'class': 'form-control'}))
    is_this_a_revision_of_a_previously_submitted_paper = forms.ChoiceField(choices=REVISION_PAPER, widget=forms.Select(attrs={'class': 'form-control'}))
