from django.db import models

# Create your models here.

class Album(models.Model):
	owner = models.CharField(max_length=20)

class Picture(models.Model):
	album = models.ForeignKey(Album, on_delete = models.CASCADE)
	image = models.ImageField(null=True)
	is_deleted = models.BooleanField(default = False)
	is_shared = models.BooleanField(default = False)




		