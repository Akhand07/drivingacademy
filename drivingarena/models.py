from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.
class CustomUser(AbstractUser):
    is_SchoolAdmin = models.BooleanField(default=False)
    is_Trainer = models.BooleanField(default=False)
    is_Trainee = models.BooleanField(default=False)


class SchoolAdmin(models.Model):
    schooladminid = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    city = models.CharField(max_length=20)
    phone = models.IntegerField(null=False)
    address = models.TextField(max_length=40)
    gender = models.CharField(max_length=6)
    experience = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="drivingarena/schooladminpic",max_length=100, null=True)

class SchoolDetails(models.Model):
    school_name = models.CharField(max_length=100, null=False, primary_key=True)
    owner_name = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=45, null=False)
    address = models.TextField(null=False)
    phone = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=100, null=True)
    about = models.TextField(null=False)
    opening_days = models.CharField(max_length=20, null=False)
    time = models.CharField(max_length=20, null=False)

class Trainer(models.Model):
    trainer_id = models.OneToOneField(CustomUser,on_delete=models.CASCADE,primary_key=True)
    phone = models.CharField(max_length=10,null=False)
    address = models.TextField(max_length=30,null=False)
    city = models.CharField(max_length=20,null=False)
    gender= models.CharField(max_length=10,null=False)
    dateofjoin = models.DateTimeField(default=timezone.now,editable=False, )
    experience = models.CharField(max_length=50,null=False)
    photo = models.FileField(max_length=100,upload_to="drivingarena/trainerpic",null=True)

class Trainee(models.Model):
    trainee = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name=models.CharField(max_length=10,default="")
    last_name=models.CharField(max_length=10,default="")
    City = models.CharField(max_length=100)
    Address = models.TextField()
    Phone = models.CharField(max_length=10)
    Gender = models.CharField(max_length=6)
    DateOfAdmission = models.DateField()
    # Photo= models.FileField(max_length=100, upload_to="school/traineepic", default="")
    Admissionmode = models.CharField(max_length=10)
    Transactionnumber = models.CharField(max_length=100)
    Fees = models.CharField(max_length=10)
    Status = models.CharField(max_length=15)
    trainer_id = models.IntegerField(null=True)


class ridedetail(models.Model):
    ride_id = models.AutoField(primary_key=True)
    # trainer_id_id = models.IntegerField(null=True)
    trainee = models.IntegerField(null=False)
    getdate = models.DateField(default=timezone.now,editable=False, )
    from_to = models.CharField(max_length=50,null=False)
    timeduration = models.CharField(max_length=20,null=False)
    traineeperformance = models.TextField(max_length=100,null=False)


class Tips(models.Model):
    tipsid = models.AutoField(primary_key=True)
    tipstext = models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=15, null=False)
    postdate = models.DateField(default=timezone.now,null=False)

class Feedback(models.Model):
    id= models.AutoField(primary_key=True)
    username=models.CharField(max_length=45,null=False)
    feedback_text=models.CharField(max_length=45,null=False)
    rating=models.IntegerField(null=False)
    date=models.DateField(default=timezone.now,editable=False, )

class ContactUs(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    yourQuery = models.TextField()
    date = models.DateField(default=timezone.now)

class TrainerAssignment(models.Model):
    Assign_id=models.AutoField(primary_key=True)
    trainer_id=models.IntegerField()
    trainee_id=models.IntegerField()
    Date=models.DateField(default=timezone.now)

