from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from django.db import models
# Create your models here.
class Questionnaire(models.Model):
 question = models.CharField(max_length=256)



class Worker(models.Model):
			name = models.CharField(max_length=100)
			ph_number = models.IntegerField()
			email = models.CharField(max_length=100)
			address = models.CharField(max_length=250)
			age = models.IntegerField()
			skill_1 = models.CharField(max_length=50)
			skill_2= models.CharField(max_length=50)
			skill_3 = models.CharField(max_length=50)
			skill_4= models.CharField(max_length=50)
			Profile_pic = models.CharField(max_length=1000)
			gender = models.CharField(max_length=15)
			hire = models.CharField(max_length=20)

			def get_absolute_url(self):
				return reverse('profiles:index')

