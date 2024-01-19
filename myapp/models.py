from django.db import models

# Create your models here.


class info(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)


class note(models.Model):
    title=models.CharField(max_length=100)
    cate=models.CharField(max_length=100)
    myfile=models.FileField(upload_to='Media')
    comments=models.TextField()


class feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    sub=models.CharField(max_length=100)
    msg=models.CharField(max_length=100)