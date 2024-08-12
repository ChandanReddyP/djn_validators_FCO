from django import forms

class StudentForm(forms.Form):
    sid=forms.IntegerField()
    sn=forms.CharField()
    sa=forms.IntegerField()
    em=forms.EmailField()
    rem=forms.EmailField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)

    def clean(self):
        em=self.cleaned_data['em']
        rem=self.cleaned_data['rem']
        if em != rem:
            raise forms.ValidationError('emails is not matching')


    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>=1:
            raise forms.ValidationError('bot')