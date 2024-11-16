from django.db import models

# Create your models here.

class scraped_data(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100 ,null=True ,blank=True )
    address = models.CharField(max_length=200 ,null=True ,blank=True)
    title = models.CharField(max_length=250 ,null=True ,blank=True)
    published = models.CharField(max_length=50 ,null=True ,blank=True)
    article_img = models.CharField(max_length=150 ,null=True ,blank=True)
    body =models.CharField(max_length=20000 ,null=True ,blank=True)



    # 'url': url,
    #     'title': title,
    #     'author': author,
    #     'author_details': author_info,
    #     'published': published,
    #     'published_date': published_date,
    #     'body':article_body ,
    #     "image_url": image_url,

