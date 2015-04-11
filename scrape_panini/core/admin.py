from django.contrib import admin

# Register your models here.

from .models import * 

admin.site.register(Comic)
admin.site.register(Collection)
admin.site.register(Tag)
admin.site.register(ComicTag)
