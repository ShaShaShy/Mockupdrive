from django.db import models

# Create your models here.
class Files(models.Model):

	fileName = models.CharField(max_length=200, null=True)
	fileType = models.CharField(max_length=200, null=True)
	fileSize = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.name



class UserUpload(models.Model):

	fileName = models.CharField(max_length=200, null=True)
	fileUp = models.FileField()
	fileType = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.name