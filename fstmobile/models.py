from django.db import models

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=255);
	number = models.CharField(max_length=255);
	created = models.DateTimeField('auto_now_add=True');

