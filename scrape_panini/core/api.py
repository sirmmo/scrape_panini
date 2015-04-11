from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import SessionAuthentication, ApiKeyAuthentication, BasicAuthentication, MultiAuthentication
from django.conf.urls import patterns, include, url
from tastypie.utils import trailing_slash

from .models import *

from tastypie.api import Api


v1_api = Api(api_name='v1')

class ComicResource(ModelResource):
	class Meta:
		queryset = Comic.objects.all()
		resource_name = 'comic'
		allowed_methods=["get"]
		excludes=["id"]

	def prepend_urls(self):
		""" Add the following array of urls to the GameResource base urls """

		return [
			url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/add%s$" %
				(self._meta.resource_name, trailing_slash()),
				self.wrap_view('add'), name="api_comic_add"),
		]

	def add(self, request, **kwargs):
		""" proxy for the comic.add method """  

		# you can do a method check to avoid bad requests
		self.method_check(request, allowed=['get'])

		# create a basic bundle object for self.get_cached_obj_get.
		basic_bundle = self.build_bundle(request=request)

		# using the primary key defined in the url, obtain the game
		game = self.cached_obj_get(
			 bundle=basic_bundle,
			 **self.remove_api_resource_names(kwargs))

		# Return what the method output, tastypie will handle the serialization
		return self.create_response(request, "OK")

class CollectionResource(ModelResource):
	class Meta:
		queryset = Collection.objects.all()
		resource_name = "collection"
		#authentication = MultiAuthentication(BasicAuthentication(), SessionAuthentication(), ApiKeyAuthentication())
		#authorization = DjangoAuthorization()


v1_api.register(ComicResource())
v1_api.register(CollectionResource())
