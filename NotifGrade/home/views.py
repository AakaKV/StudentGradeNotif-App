from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse
from .forms import CreateNewAssignment
# Create your views here.
# #Telling compiler to search for templates in the templates folder
# TEMPLATE_DIRS = (
#     'os.path.join(BASE_DIR, templates),'
# )
def index(request):
    return render(request,"index.html")

def assignments(response):
    form = CreateNewAssignment()
    return render(response,"assignments.html", {"form":form})