from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from phone_field import PhoneField

    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phoneNo = PhoneField(blank=True, help_text='Contact phone number')
 
    def __str__(self):
        return f'{self.user.username} Profile'
    
   
            
