from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from .models import *
# Create your views here.
def games_main(request):
	obj = Game.objects.all()
	context = {'obj':obj}
	return render(request, "games/app.html", context)