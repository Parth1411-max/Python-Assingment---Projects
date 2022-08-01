from django import views
from django.db import models
from django.utils import timezone
import math

# Create your models here.


class user(models.Model):
    email = models.EmailField(unique= True,max_length=50)
    password = models.CharField(max_length = 30)
    otp = models.IntegerField(default = 459)
    role = models.CharField(max_length = 10)
    is_active = models.BooleanField(default=False)
    is_verfied = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self)-> str:
        return self.email


class chairman(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=30)
    contect=models.CharField(max_length=15)
    block_no=models.CharField(max_length=10,null=True)
    house_no=models.CharField(max_length=10,null=True)
    about_me=models.TextField(max_length=50,null=True)
    pic=models.FileField(upload_to='images/',default='media/default_chairman.png')

    def __str__(self)-> str:
        return self.firstname +" "+ self.lastname


class member(models.Model):
    member_id=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    contect=models.CharField(max_length=50)
    DOB=models.CharField(max_length=50)
    totalvehicle=models.CharField(max_length=50)
    familymember=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    workinfo=models.CharField(max_length=50)
    pic=models.ImageField(upload_to='images/Notice',null=True)

    def __str__(self):
        return self.firstname


class notice(models.Model):
    user_id=models.ForeignKey(chairman,on_delete=models.CASCADE)
    notice_title=models.CharField(max_length=85,null=True)
    notice_content=models.TextField(max_length=85,null=True)
    img=models.ImageField(upload_to='images/Notice',null=True)
    video=models.FileField(upload_to='images/Notice/videos',null=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notice_title



    def whenpublished(self):
        now = timezone.now()

        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"
        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

class notice_view(models.Model):
    user_id=models.ForeignKey(chairman,on_delete=models.CASCADE)
    notice_id=models.ForeignKey(notice,on_delete=models.CASCADE)
    member_id=models.ForeignKey(member,on_delete=models.CASCADE)
    view_at=models.DateTimeField(auto_now_add=True,null=True)


class events(models.Model):
    user_id=models.ForeignKey(chairman,on_delete=models.CASCADE)
    events_title=models.CharField(max_length=85,null=True)
    events_content=models.TextField(max_length=85,null=True)
    img=models.ImageField(upload_to='images/Notice',null=True)
    video=models.FileField(upload_to='images/Notice/videos',null=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.events_title

    def whenpublished(self):
        now = timezone.now()

        diff= now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"
        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + " hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            if months == 1:
                return str(months) + " month ago"
            else:
                return str(months) + " months ago"
        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"
            else:
                return str(years) + " years ago"

class events_view(models.Model):
    user_id=models.ForeignKey(chairman,on_delete=models.CASCADE)
    notice_id=models.ForeignKey(notice,on_delete=models.CASCADE)
    member_id=models.ForeignKey(member,on_delete=models.CASCADE)
    view_at=models.DateTimeField(auto_now_add=True,null=True)









    



