from django import forms

s=[('male','MALE'),('femlae','FEMALE')]
c=[('python','PYTHON'),('sql','SQL'),('django','DJANGO')]

class SignUpForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=s)
    gender=forms.ChoiceField(choices=s,widget=forms.RadioSelect)
    courses=forms.MultipleChoiceField(choices=c)