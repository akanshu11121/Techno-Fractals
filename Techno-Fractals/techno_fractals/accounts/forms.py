from django import forms
from accounts.models import UserProfileInfo,Blog
from django.contrib.auth.models import User

class UserProfileInfoForm(forms.ModelForm):
    firstname = forms.CharField(max_length=256,required=False)
    lastname = forms.CharField(max_length=256,required=False)
    picture = forms.ImageField(required=False)
    class Meta():
        model = UserProfileInfo
        exclude = ('user',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password')
       
class BlogForm(forms.ModelForm):

    class Meta():
        model = Blog
        fields = ('writer','title','text')
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'blog_form_title'}),
            'text' : forms.Textarea(attrs={'rows': 10,'cols': 60,'class' : 'blog_form_text'}) 
        }