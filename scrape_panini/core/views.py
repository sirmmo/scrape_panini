from django.shortcuts import render

from core.models import *

from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
def collection(request, user=None, clist="collection"):
	f = {}
	ret = {}
	page = request.GET.get('page')
	q = request.REQUEST.get("q")

	if user:
		f["owned_by__owner"] = User.objects.get(username = user)
		f["owned_by__list"] = clist

	if q:
		f["title__contains"] = q
		ret["q"]=q
	
	s = Comic.objects.filter(**f)
	paginator = Paginator(s, 60)

	try:
		s = paginator.page(page)
	except PageNotAnInteger:
		s = paginator.page(1)
	except EmptyPage:
		s = paginator.page(paginator.num_pages)

	ret["collection"] = s

	if request.user.is_authenticated():
		ret["owneds"]= [c.ident for c in Comic.objects.filter(owned_by__owner = request.user)]
	return render(request, "list.html", ret)

@login_required
@csrf_exempt
def add(request):
	comic = Comic.objects.get(ident=request.REQUEST.get("comic"))
	c = Collection()
	c.owner = request.user
	c.comic = comic
	if request.REQUEST.get("list") == "wishlist":
		c.the_list = "wishlist"
	c.save()

	return HttpResponse("<div>added!</div>")

@login_required
@csrf_exempt
def rem(request):
	comic = Comic.objects.get(ident=request.REQUEST.get("comic"))
	Collection.objects.filter(comic = comic, owner = request.user).delete()

	return HttpResponse("<div>removed!</div>")


def profile(request):
	return HttpResponseRedirect("/collection/%s" % request.user.username)


from django.contrib.auth import logout as lo
def logout(request):
	lo(request)
	return HttpResponseRedirect("/")



