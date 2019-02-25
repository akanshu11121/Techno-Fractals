from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class UserProfileInfo (models.Model):

    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    firstname = models.CharField(max_length=256, blank=True)
    lastname = models.CharField(max_length=256, blank=True)
    picture = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
    
class Blog(models.Model):

    writer = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50,blank=False)
    text = models.TextField(blank=False)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('accounts:blog_detail',kwargs={'pk':self.pk})

    def publish(self):
        self.create_date = timezone.now()
        self.save()
    