# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..users.models import Users

from datetime import datetime

# Create your models here.
class TravelsManager(models.Manager):
	def createTravel(self, postData, owner_param):
		retmsg=[]
		if not ( postData['dest'] and postData['desc'] and
						 postData['start'] and postData['end'] ):
			retmsg.append( 'Must fill all Fields!')
			return retmsg
		print '-----------------------------------'
		print postData['start']
		print '-----------------------------------'	
		date = datetime.strptime(postData['start'], '%Y-%m-%d')
		print '-----------------------------------'
		print postData['start']
		print '-----------------------------------'
		if date < datetime.now():
			retmsg.append('Plan must be in the future!')
		if postData['end'] < postData['start']:
			retmsg.append('Plan must happen in real time! (Travel Date To must be after Travel Date From)')

		if retmsg:
			return retmsg

		t = Travels.objects.create(destination=postData['dest'],
															 description=postData['desc'],
															 start_date=postData['start'],
																	 end_date=postData['end'],
										owner=Users.objects.get(id=owner_param))
		return False

	def addUser(self, travel_id, user_id):
		Travels.objects.get(id=travel_id).users.add(Users.objects.get(id=user_id))

class Travels(models.Model):
	destination=models.CharField(max_length=255)
	description=models.CharField(max_length=255)
	start_date=models.DateTimeField()
	end_date=models.DateTimeField()
	owner=models.ForeignKey(Users, related_name='owned_travels')
	users=models.ManyToManyField(Users, related_name='travels')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	objects = TravelsManager()
