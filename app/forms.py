from django import forms

class StudentForm(forms.Form):
    sid=forms.IntegerField()
    sn=forms.CharField()
    sa=forms.IntegerField()
    em=forms.EmailField()
    rem=forms.EmailField()


    def clean(self):
        em=self.cleaned_data['em']
        rem=self.cleaned_data['rem']
        if em != rem:
            raise forms.ValidationError('emails is not matching')