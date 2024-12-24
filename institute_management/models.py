from django.db import models

# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	password=models.CharField(max_length=100)
	profile_picture=models.ImageField(upload_to="profile_picture/",default="")
		

	def __str__(self):
		return self.fname+" - "+self.lname





class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    hire_date = models.DateField()

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    president = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title


