from django import forms
from allauth.account.forms import SignupForm
from .models import Diary, Sidenote
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# class CustomSignupForm(SignupForm):
#     username = forms.CharField(max_length=30, label='Username')
#     email = forms.EmailField(required=False, label='Email')

#     def save(self, request):
#         user = super(CustomSignupForm, self).save(request)
#         user.username = self.cleaned_data['username']
#         if self.cleaned_data['email']:
#             user.email = self.cleaned_data['email']
#         user.save()
#         return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Login'))
    
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

class SidenoteForm(forms.ModelForm):
    class Meta:
        model = Sidenote
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }