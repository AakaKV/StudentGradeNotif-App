from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Testing Response')