from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Profile,Rate,Comment
# Create your views here.
