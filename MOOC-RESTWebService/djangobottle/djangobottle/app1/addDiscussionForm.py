__author__ = 'swetapatel'

from django import forms

class addDiscussionForm(forms.Form):
    title = forms.CharField()
    print 'In form'

    def clean_title(self):
        cd = self.cleaned_data
        title = cd.get('title')
        return title