from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from markdown2 import Markdown
from django.urls import reverse

from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def result(request,title):
	page=util.get_entry(title)
	entries=util.list_entries()
	if title in entries:
		return HttpResponse(page)
	else:
		message="no such page exist."
		return render(request,"encyclopedia/error.html",{
			"message":message
			})	

def links(request,title):
	page=util.get_entry(title)
	markdownify=Markdown()
	return HttpResponse(markdownify.convert(page)+'<a href="edit_entries/'+title+'">EDIT</a>')

def search(request):
	if request.method=="POST":
		sub=request.POST.get("q")
		entries=util.list_entries()
		if sub in entries:
			return HttpResponseRedirect(reverse("links",args=[sub]))
		else:
			res=[i for i in entries if sub in i] 
			if res is not None:
				return render(request,"encyclopedia/sub.html",{
					"names":res
					})
			else:
				
				return render(request,"encyclopedia/subs.html")
			
def form(request):
	return render(request,"encyclopedia/add.html")
def add(request):
	if request.method=="POST":
		title=request.POST.get("title")	
		new_file=request.POST.get("data")
		entries=util.list_entries()
		if title in entries:
			message="This page already exist"
			return render(request,"encyclopedia/error.html",{
			"message":message
			})	
		else:
			util.save_entry(title,new_file)	
			return HttpResponseRedirect(reverse("links",args=[title]))
		
def randoms(request):
	list=util.list_entries()
	page=random.choice(list)
	return HttpResponseRedirect(reverse("links",args=[page]))

def edit_entries(request,title):
	data=util.get_entry(title)	
	return render(request,"encyclopedia/edit.html",{'title':title,'data':data})

def edit(request):
	if request.method=="POST":
		title=request.POST.get("title")	
		data=request.POST.get("data")
		util.save_entry(title,data)	
		return HttpResponseRedirect(reverse("links",args=[title]))
	else:
		return HttpResponse("METHOD NOT ALLOWED.")	



				 	 