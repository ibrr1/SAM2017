from django import forms

__author__ = 'Adi'


class ReviewPaper(forms.Form):

    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    RATINGS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )

    rating = forms.ChoiceField(choices=RATINGS, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        app_label = 'sam2017_app'