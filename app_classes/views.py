from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout as dj_logout
from django.contrib.auth.decorators import login_required
