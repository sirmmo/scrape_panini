from __future__ import absolute_import
from core.models import *
import datetime
import requests
from bs4 import BeautifulSoup



from celery import shared_task

min_year = 1990

domain = "http://www.paninicomics.it"

base_urls = [
	"http://www.paninicomics.it/web/guest/paninicomics/checklist?year=%s&weekOfYear=%s",
	"http://www.paninicomics.it/web/guest/marvelitalia/checklist?year=%s&weekOfYear=%s",
	"http://www.paninicomics.it/web/guest/planetmanga/checklist?year=%s&weekOfYear=%s"
]

buy_url = "http://www.paninicomics.it/web/guest/carrello?addItemId=%s"

@shared_task
def refresh():
	nowdate = datetime.datetime.now().isocalendar()
	from_week = nowdate[1]
	from_year = nowdate[0]

	for year in reversed(range(min_year, from_year+1)):
		final = 52 if year == from_year else from_week
		for week in range(0,final):
			for url in base_urls:
				the_url = url%(year, week)
				
				get_page.delay(the_url)
@shared_task
def get_page(the_url):
	page = requests.get(the_url)
	page = page.response
	page = BeautifulSoup(page)

	for details in page.find_all(class_="detail"):
		c = Comic()
		for di in details.find_all("div"):
			if di["class"] == "cover":
				c.cover = domain+di.img["src"]
				c.ident = di.img["src"].split("img_id=")[1].split("&")[0]
			elif di["class"] == "logo_brand":
				c.brand = di.img["alt"]
			elif di["class"] == "title":
				c.title = di.h3.string
			elif di["class"] == "price":
				c.price = di.h3.strong.string
		c.save()




