from email.mime import image
from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Profile(models.Model):
    profile =models.ImageField(upload_to ='photos/',blank = True)
    bio = models.CharField(max_length= 200)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()


    @classmethod
    def delete_profile(cls, id):
        profile=cls.objects(profile_id=id).delete()
        return profile

    @classmethod
    def update_profile(cls,profile_id,profiel):
        profile=cls.objects.fileter(id=profile_id).update(profile=profile)
        return profile

    @classmethod
    def filter_profile_by_id(cls,profile):
        profile =cls.objects.filter(id_in=profile)
        return profile




class Image(models.Model):
    name=models.CharField(max_length=60)
    caption=models.CharField(max_length=200)
    image=models.ImageField(upload_to='photos/',blank=True)
    likes=models.IntegerField(default=0)
    dislikes=models.IntegerField(default=0)
    comments=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)


    def _str__(self):
        return self.name

    class Meta:
        ordering=['name']

    def save_profile(self):
        self.save()

    @classmethod
    def delte_image(cls,id):
        image.cls.objects.filter(image_id=id).delete()
        return image

    @classmethod
    def filter_by_profile(cls, profile):
        images=cls.objects.filter(profile__in=profile)
        return images

    @classmethod
    def search_by_image(cls,search_term):
        images=cls.objects.filter(name__icontains=search_term)
        return images





class Preference(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image= models.ForeignKey(Image,on_delete=models.CASCADE)
    value=models.IntegerField()
    date=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.user +":" +str(self.image) + ":" + str(self.value)
    
    class Meta:
        unique_together = ("user","image", "value")

    def save_preference(self):
        self.save()


        