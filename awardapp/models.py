from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    profile_photo = models.ImageField(default='default.png',upload_to='profiles/')
    bio = HTMLField(max_length=500,default="Rate")
    website = URLOrRelativeURLField() 
    phone_number = models.CharField(max_length=10,default= 788494207)
    
    @classmethod
    def get_by_id(cls,id):
        profile = Profile.objects.get(user = id)
        return profile
    
    @classmethod
    def filter_by_id(cls,id): 
        profile = Profile.objects.filter(user = id).first()
        return profile

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
     
    @receiver(post_save, sender=User) 
    def save_profile(sender,instance,**kwargs):
        instance.profile.save()  
        
    def __str__(self):
        return self.bio
    