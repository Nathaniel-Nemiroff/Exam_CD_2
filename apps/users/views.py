# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse

from models import Users

# Create your views here.
def index(request):
	if 'user' in request.session:
		return redirect(reverse('travels:index'))

	context={}
	if 'msg' in request.session:
		context['messages']=request.session['msg']
		request.session.pop('msg')
	return render(request, 'users/index.html', context)
def register(request):
	if request.method=='POST':
		msg = Users.objects.createUser(request.POST)
		request.session['msg']=msg
		print request.session['msg']

	return redirect('/')

def login(request):
	if request.method=='POST':
		user = Users.objects.getUser(request.POST)
		if user:
			print 'LOGIN SUCCESS'
			request.session['user']=user.id
			print request.session['user']
			return redirect(reverse('travels:index'))
		else:
			print 'LOGIN FAILURE'
			request.session['msg']=[]
			request.session['msg'].append('Login Failed!')
		
	return redirect('/')

def logout(request):
	if 'user' in request.session:
		request.session.pop('user')
	return redirect('/')
