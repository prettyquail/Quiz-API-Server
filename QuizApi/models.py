from django.db import models

# Create your models here.
class Admin(models.Model):
	id=models.IntegerField(primary_key=True)
	fullname=models.CharField(max_length=55)

	def __str__(self):
		return self.fullname

class User(models.Model):
	id=models.IntegerField(primary_key=True)
	username=models.CharField(max_length=66)

class Quiz(models.Model):
	id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=55)
	admin_id=models.ForeignKey(Admin,on_delete=models.CASCADE)
	status=models.DateTimeField()

	def __str__(self):
		return self.name

class Question(models.Model):
	id=models.IntegerField(primary_key=True)
	quiz_id=models.ForeignKey(Quiz,on_delete=models.CASCADE)
	question=models.TextField()
	image_url=models.CharField(max_length=66,blank=True)
	option1=models.CharField(max_length=166,blank=True)
	option2=models.CharField(max_length=166,blank=True)
	option3=models.CharField(max_length=166,blank=True)
	option4=models.CharField(max_length=166,blank=True)
	answer=models.CharField(max_length=166)

class Attempt(models.Model):
	id=models.IntegerField(primary_key=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	qid=models.ForeignKey(Question,on_delete=models.CASCADE)
	ans=models.CharField(max_length=166,blank=True)


