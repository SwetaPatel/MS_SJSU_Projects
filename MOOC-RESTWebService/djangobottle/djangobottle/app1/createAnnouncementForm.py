__author__ = 'swetapatel'

from django import forms


class createAnnouncementForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    postDate = forms.CharField()
    status = forms.IntegerField()


    def clean_title(self):
        cd = self.cleaned_data

        title = cd.get('title')


        if len(title) == 0:
           raise forms.ValidationError("title cannot be null")

        return title

    def clean_description(self):
        cd = self.cleaned_data

        description = cd.get('description')

        if len(description) == 0:
           raise forms.ValidationError("Description cannot be null")

        return description

    def clean_postDate(self):
        cd = self.cleaned_data

        postDate = cd.get('postDate')

        #if len(fname) == 0:
           # raise forms.ValidationError("First name cannot be null")

        return postDate

    def clean_status(self):
        cd = self.cleaned_data

        status = cd.get('status')

        #if len(lname) == 0:
            #raise forms.ValidationError("Last name cannot be null")

        return status
