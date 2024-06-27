from django import forms
from allauth.account.forms import SignupForm
from .models import Post

class CustomSignupForm(SignupForm):
    username = forms.CharField(max_length=30, label='Username')
    email = forms.EmailField(required=False, label='Email')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.username = self.cleaned_data['username']
        if self.cleaned_data['email']:
            user.email = self.cleaned_data['email']
        user.save()
        return user
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
