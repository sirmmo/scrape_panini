

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
		nowdate = datetime.datetime.now().isocalendar()
		from_week = nowdate[1]
		from_year = nowdate[0]

		for year in reversed(range(min_year, from_year+1)):
			final = from_week if year == from_year else 52
			for week in reversed(range(0,final+1)):
				for url in base_urls:
					the_url = url%(year, week)
					print ">> %s/%s" % (year, week)
					self.get_page(the_url, year, week)


	def get_page(self,the_url, y,w):
		page = requests.get(the_url)
		page = page.text
		page = BeautifulSoup(page)

		for details in page.find_all(class_="detail"):
			c = Comic()
			for di in details.find_all("div"):
				if "cover" in di["class"]:
					print di.img["src"]
					c.cover = domain+di.img["src"]
					if not c.ident:
						try:
							c.ident = di.img["src"].split("=")[1].split("&")[0]
						except:
							pass
				elif "logo_brand" in di["class"]:
					c.brand = di.img["alt"]
				elif "title" in di["class"]:
					print di.h3.string
					c.title = di.h3.string
					c.contains = di.find_all(class_="features")[0].string
				elif "price" in di["class"]:
					c.price = float(di.find_all("strong")[-1].string)
				elif "actions_comm" in di["class"]:
					if not c.ident:
						try:
							c.ident = di.a["href"].split("=")[1]
						except:
							pass
				elif "desc" in di["class"]:
					c.notes = di.p.string
							
			c.year = y
			c.week = w

			if Comic.objects.filter(ident=c.ident).count()>0:
				pass
			else:
				c.save()




