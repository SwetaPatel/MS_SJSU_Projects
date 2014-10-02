__author__ = 'vidhi110'

from django import forms

class DiscussionSuccessForm(forms.Form):
    content = forms.CharField()
    title = forms.CharField()
    # createdby = forms.CharField()



    def clean_content(self):
        cd = self.cleaned_data

        content = cd.get('content')
        print 'In content', content


        # if len(content) == 0:
        #     raise forms.ValidationError("Please Enter Message.")

        return content

    def clean_title(self):
        cd = self.cleaned_data

        title = cd.get('title')
        print 'In title', title


        # if len(title) == 0:
        #     raise forms.ValidationError("Please Enter Title.")

        return title


    # def clean_createdby(self):
    #     cd = self.cleaned_data
    #
    #
    #     createdby = cd.get('createdby')
    #     print 'In createdby', createdby
    #
    #
    #     # if len(email) < 3:
    #     #     raise forms.ValidationError("Please Title more then two word..")
    #
    #     return createdby