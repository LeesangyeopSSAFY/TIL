from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'palceholder': 'Enter the title',
                'maxlength': 10,
            }
        ),
    )

    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': 'Please entet your content'
        }
    )

    class Meta:
        model = Article
        fields = '__all__'
        
