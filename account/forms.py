from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms





class CustomUserCreationFrom(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', )
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'user_n',}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'user_n',}))
    

        



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username',)
        
