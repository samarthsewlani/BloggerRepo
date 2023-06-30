from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from image_uploader_widget.widgets import ImageUploaderWidget
from .models import Blog

class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Enter title for your blog'}))
    body = forms.CharField(widget=CKEditorUploadingWidget(attrs={'class': 'form-control mb-2', 'placeholder': 'Write your blog here...'}))
    cover = forms.ImageField(widget=ImageUploaderWidget())

    class Meta:
        model = Blog
        fields = ('title', 'body', 'cover')