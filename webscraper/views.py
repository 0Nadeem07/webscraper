from django.shortcuts import render ,get_object_or_404
from .models import scraped_data
from .script import macworld_article_list,macworld_article_details
from .techmeme2 import techmeme_article_list ,techmeme_article_details

from django.http import HttpResponseRedirect

import requests
from bs4 import BeautifulSoup

# Create your views here.

def scrape(request):

    if request.method == 'POST':

        site  = request.POST.get('site','')
        if site!='' and site!= None:
            # response = requests.get(site)
            article_links = macworld_article_list(site)
            if article_links:
                for article in article_links:
                    art = macworld_article_details(article)
                    if art:
                        name = art.get('author', 'Unknown Author')
                        address = art.get('url', 'No URL')
                        title = art.get('title', 'No Title')
                        published = art.get('published', 'No Date')
                        body = art.get('body', 'No Content')
                        article_img = art.get('article_img','no image')
                        
                        scraped_data.objects.create(
                            name=name,
                            address=address,
                            title=title,
                            published=published,
                            article_img=article_img,
                            body=body
                        )
                    else:
                        print(f"Skipping article: {article} (No details found)")

            return HttpResponseRedirect('/')
        else:
            data  = scraped_data.objects.all()
    else:
        data  = scraped_data.objects.only('name', 'address')

    return render(request,'webscraper/scraper.html',{'data':data})

def load_details(request, id):

    details = scraped_data.objects.get(pk=id)
    return render(request ,'webscraper/details.html',{'details':details})


def clear(request):
    scraped_data.objects.all().delete()

    return render(request,'webscraper/scraper.html')

