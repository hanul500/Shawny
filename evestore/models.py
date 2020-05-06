
from django.db import models

# Create your models here.
class Evestore(models.Model):
	name = models.CharField(max_length=300)
	upload_date = models.DateField()
	main_image = models.ImageField(upload_to='main_images/')
	heart = models.IntegerField(default=0)