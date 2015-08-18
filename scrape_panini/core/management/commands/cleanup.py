

from django.core.management.base import BaseCommand, CommandError




from core.models import *
import datetime
import requests
from bs4 import BeautifulSoup




min_year = 1990

domain = "http://www.paninicomics.it"

base_urls = [
	"http://www.paninicomics.it/web/guest/paninicomics/checklist?year=%s&weekOfYear=%s",
	"http://www.paninicomics.it/web/guest/marvelitalia/checklist?year=%s&weekOfYear=%s",
	"http://www.paninicomics.it/web/guest/planetmanga/checklist?year=%s&weekOfYear=%s"
]

buy_url = "http://www.paninicomics.it/web/guest/carrello?addItemId=%s"


class Command(BaseCommand):

	def handle(self, *args, **options):
		self.refresh()

	def refresh(self):
		for c in Comic.objects.all():
			print c.id
			if c.notes:
				c.notes = c.notes.replace("\n", "")
			if c.contains:
				c.contains = c.contains.replace("\n", "")
			c.save()




