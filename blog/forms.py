from django import forms
from .models import Post, Category, Comment


# Add Post Form
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'header_image', 'title_tag', 'category', 'snippet', 'author', 'content']

        # Styling my custom django form with Bootstrap.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title here...'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'author_name', 'value': '', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

        # Styling my custom django form with Bootstrap.
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category here...'}),
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']

        # Styling my custom django form with Bootstrap.
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


# Update Post Form
class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'category', 'snippet', 'content']

        # Styling my custom django form with Bootstrap.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title here...'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }
