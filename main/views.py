from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect

def logo_page(request):
	context = {}
	return render(request, "main/logo_page.html", context)