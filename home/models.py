from django.db import models

# Create your models here.

class MenuItem(models.Model):
	itemName = models.CharField(max_length = 30)
	itemPrice = models.IntegerField(default = 0)

	def __str__(self):
		return self.itemName