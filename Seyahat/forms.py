from django import forms 
from .models import Seyahat
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Seyahat
        fields = ["title","content","seyahat_image"]