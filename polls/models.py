from django.db import models

# Create your models here.

class clients(models.Model):
	username = models.CharField('username', max_length=50)
	phone = models.CharField('phone', max_length=10)
	email = models.EmailField('Email', unique = True)
	extra_contacts = models.CharField('extra_contacts', max_length=50)
	coment = models.CharField('coment', max_length=228)
