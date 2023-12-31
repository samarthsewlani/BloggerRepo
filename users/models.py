from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Profile(models.Model):
    #address=models.TextField()
    contact=models.CharField(default="6560377549",max_length=12)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default="default.jpg",upload_to='profile-pics')
    location=models.CharField(blank=True,null=True,max_length=50)
    title=models.CharField(blank=True,null=True,max_length=50)

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self,*args,**kwargs):              #Overriding save method to set size of the image
        super().save()
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img=img.resize(output_size)
            img.save(self.image.path)
    
    def get_absolute_url(self):
        return reverse('home')

    