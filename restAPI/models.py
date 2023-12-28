import uuid
from django.db import models
from enum import Enum
from django.contrib.auth import authenticate

class UserType(Enum):
    ADMIN = 'admin'
    EXPERT = 'expert'
    PARENT = 'parent'
    SPECIAL_PERSON = 'special_person'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class CustomUser(models.Model):
    U_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userType = models.CharField(max_length=20, choices=[(tag, tag.value) for tag in UserType], default=UserType.ADMIN.value)
    fullName = models.CharField(max_length=255, null=False)
    userName = models.CharField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    age = models.IntegerField( null=False)
    gender = models.CharField(max_length=10, null=False)
    address = models.TextField(max_length=500, null=False)
    mobileNo = models.CharField(max_length=10, null=False)
    country = models.CharField(max_length=255, null=False)
    avatar = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.fullName





class Special_Person(models.Model):
    sp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    U_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    disability_type = models.CharField(max_length=255, null=False)
    disability_cert =  models.ImageField(upload_to='media/', null=False)
    education = models.CharField(max_length=255, null=False)
    hobbies = models.CharField(max_length=255, null=False)





class expert(models.Model):
    expert_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    U_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255, null=False)
    proof_of_designation = models.ImageField(upload_to='media/', null=True, blank=True)
    




class Question(models.Model):
    Q_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    U_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # ForeignKey to link with the User model
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  # Automatically updated on each save
    like_count = models.PositiveIntegerField(default=0)
    dislike_count = models.PositiveIntegerField(default=0)
    # liked_by = models.ManyToManyField(CustomUser, related_name='liked_questions')
    # dis_liked_by = models.ManyToManyField(CustomUser, related_name='dis_liked_questions')
  

    def __str__(self):
        return self.title
    




class Answers(models.Model):
    A_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    U_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # ForeignKey to link with the User model
    Q_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    Answer = models.CharField(null=False)
    # description = models.TextField()
    # question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  # Automatically updated on each save 
    like_count = models.PositiveIntegerField(default=0)
    dislike_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.Answer








