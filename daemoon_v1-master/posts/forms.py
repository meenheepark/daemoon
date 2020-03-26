from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력해 주세요.')

class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator],max_length=100)
    body = forms.CharField(widget=CKEditorUploadingWidget())
    
    def save(self,commit=True):
        post = Post(**self.cleaned_data)
        if commit:
            post.save()
        return post
