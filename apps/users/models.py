# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


import re

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

# Create your models here.
class UsersManager(models.Manager):
	def createUser(self, postData):
		retmsg=[]
		if not ( postData['name'] and postData['user'] and
						 postData['pswd'] and postData['conf'] ):
			retmsg.append('Must fill all fields!')
		if(len(postData['name'])<3 or len(postData['user'])<3):
			retmsg.append('Name and Username must be at least 3 characters long!')
		if not NAME_REGEX.match(postData['name']):
			retmsg.append('Name cannot have numbers in it!')
		if len(postData['pswd'])<8:
			retmsg.append('Password must be at least 8 characters!')
		if not postData['pswd']==postData['conf']:
			retmsg.append('Passwords do not match!')

		if retmsg:
			return retmsg

		if not Users.objects.filter(username=postData['user']):
			Users.objects.create(name=postData['name'],
											 username=postData['user'],
											 password=postData['pswd'])
			retmsg.append('Success!')
		else:
			retmsg.append('User exists!')

		return retmsg	

	def getUser(self, postData):
		if not ( postData['user'] and postData['pswd']):
			return False
		if not Users.objects.filter(username=postData['user']):
			return False
		user=Users.objects.get(username=postData['user'])
		if not user.password==postData['pswd']:
			return False

		return user

class Users(models.Model):
	name=models.CharField(max_length=100)
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=200)
	salt=models.CharField(max_length=200)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	objects=UsersManager()
