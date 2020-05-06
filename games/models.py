

# Create your models here.
from django.db import models

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length=300)
	category = models.CharField(max_length=300)
	content = models.CharField(max_length=500)
	upload_date = models.DateField()
	main_image = models.ImageField(upload_to='app_images/')
	link_android = models.CharField(max_length=300)
	link_ios = models.CharField(max_length=300)
	heart = models.IntegerField(default=0)