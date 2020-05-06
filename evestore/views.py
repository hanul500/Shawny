from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from .models import *
# Create your views here.
def evestore_main(request):
	
	context = {}
	return render(request, "evestore/evestore.html", context)