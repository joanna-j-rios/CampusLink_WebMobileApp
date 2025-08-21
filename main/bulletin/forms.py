    # bulletin/forms.py
from django import forms
from .models import Post # Import your Post model

class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ['title', 'content', 'is_event']
            widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}),
                'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your post here...'}),
                'is_event': forms.CheckboxInput(attrs={'class': 'form-check-input'})
            }
    