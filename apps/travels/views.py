# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse

from models import Travels
from ..users.models import Users

# Create your views here.
def index(request):
	if not 'user' in request.session:
		return redirect('/')
	user = Users.objects.get(id=request.session['user'])
	context={
		'user':user,
		'owned':user.owned_travels.all(),
		'joined':user.travels.all(),
		'travels':Travels.objects.all().exclude(users=user)
	}
	return render(request, 'travels/index.html', context)

def destination(request, id):
	t = Travels.objects.get(id=id)
	context={
		'travel':t,
		'users':t.users.all()
	}
	return render(request, 'travels/destination.html', context)

def add(request):
	context = {}
	if 'msg' in request.session:
		context['messages']=request.session['msg']
		request.session.pop('msg')

	return render(request, 'travels/add.html', context)
def create_trip(request):
	if request.method == 'POST':
		msg = Travels.objects.createTravel(request.POST, request.session['user'])
		if msg:
			request.session['msg']=msg
			return redirect(reverse('travels:add'))
	return redirect(reverse('travels:index'))


def join(request, id):
	Travels.objects.addUser(id, request.session['user'])
	return redirect(reverse('travels:index'))
