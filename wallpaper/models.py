from django.db import models

# Create your models here.
class Wallpaper(models.Model):
	def __str__(self):
		return str(self.name)
	name = models.CharField(max_length=300)
	upload_date = models.DateField()
	main_image = models.ImageField(upload_to='main_images/')
	heart = models.IntegerField(default=0)
	Wallpaper = models.BooleanField(default = False)
	def get_images(self):
		return Wallpaper_images.objects.all().filter(original=self)


class Wallpaper_images(models.Model):
	def __str__(self):
		return str(self.original.name) +"  ---  "+ str(self.get_image_category_display())
	SCREEN_CHOICE=(
		("iph7","Iphone 7"),
		("iph8","Iphone 8"),
      ("iph11p","Iphone 11 Pro"),
      ("iph11","Iphone 11"),
      ("iphXS","Iphone X/XS"),
      ("iphXR","Iphone XR"),
      ("samZ","Samsung Z Flip"),
      ("sams20","Samsung S20"),
      ("sams20+","Samsung S20+"),
      ("ipadp10.5","iPad Pro 10.5-inch"),
      ("ipadp12.9","iPad Pro 12.9-inch"),
      ("no14","14"" Notebook"),
      ("no15.6","15.6"" Notebook"),
      ("nomacp13","Macbook Pro 13"),
      ("nomacp16","Macbook Pro 16"),
      ("3821","3840*2160"),
      ("2516","2560*1600"),
      ("2514","2560*1440"),
      ("2015","2048*1536"),
      ("1914","1920*1440"),
      ("1912","1920*1200"),
      ("1910","1920*1080"),
      ("1610","1680*1050"),
      ("1612","1600*1200"),
      ("1690","1600*900"),
      ("1490","1440*900"),
      ("6676","1366*768"),
      ("6076","1360*768"),
      ("1210","1280*1024"),
      ("1296","1280*960"),
      )
	image_category = models.CharField(choices=SCREEN_CHOICE,blank=True, max_length=120)
	image = models.ImageField(upload_to='images/')
	original = models.ForeignKey(Wallpaper, on_delete=models.CASCADE)
	def get_screen(self):
		if self.image_category == "iph7" or self.image_category == "iph8":
			return "screen_images/iphone_78.png"
		elif self.image_category[:3] == "iph":
			return "screen_images/iphone_not_78.png"
		elif self.image_category[:3] == "sam":
			return "screen_images/galaxy.png"
		elif self.image_category[:3] == "ipa":
			return "screen_images/ipad.png"
		elif self.image_category[:2] == "no":
			return "screen_images/laptop.png"
		else:
			return "screen_images/monitor.png"

	def get_device(self):
		if self.image_category == "iph7" or self.image_category == "iph8":
			return "iphone"
		elif self.image_category[:3] == "iph":
			return "iphone"
		elif self.image_category[:3] == "sam":
			return "android"
		elif self.image_category[:3] == "ipa":
			return "ipad"
		elif self.image_category[:2] == "no":
			return "pc"
		else:
			return "pc"