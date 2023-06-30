from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextUploadingField(blank=True, null=True)
    cover = models.ImageField(default="default.jpg",upload_to='cover-photos')
    date_posted = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Blog :- {self.title}"
    
    def save(self,*args,**kwargs):              #Overriding save method to set size of the image
        super().save()
        img=Image.open(self.cover.path)
        if img.height>350 or img.width>350:
            output_size=(350,350)
            img=img.resize(output_size)
            img.save(self.cover.path)

