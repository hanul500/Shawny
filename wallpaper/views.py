from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
import json
from .models import *

# Create your views here.
def wall_main(request):
	qset = Wallpaper.objects.all().filter(Wallpaper=True)
	context = {'qset':qset}
	return render(request, "wallpaper/wall_main.html", context)

def wall_detail(request, wall_name):
	obj = get_object_or_404(Wallpaper, name=wall_name)
	obj_images = obj.get_images()
	if request.GET.get('like_num'):
		print('asdasd')
		obj.heart += 1
		obj.save()
	like_num = obj.heart
	context = {'obj':obj,'obj_images':obj_images,'like_num':like_num}
	return render(request,'wallpaper/blog-single.html',context)

def like(request):
	print('adsadsadsad')
	obj = get_object_or_404(Wallpaper, name=request.POST['obj_name'])
	obj.heart += 1
	obj.save()
	context = {'heart': obj.heart}
	return HttpResponse(json.dumps(context), "application/json")

def collection_main(request):
	qset = Wallpaper.objects.all()
	col_list = ['4','4','4','6','6','12']
	col_list = col_list * ((len(qset)//6)+1)
	context = {'qset':zip(qset,col_list)}
	return render(request, "collection/collection.html", context)