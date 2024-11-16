import requests
from datetime import datetime
from bs4 import BeautifulSoup
import json

def convert_date_format(date_str):
    date_obj = datetime.strptime(date_str, "%B %d, %Y")
    formatted_date = date_obj.strftime("%Y-%m-%d")
    return formatted_date

def macworld_author_details(author_url):
    response = requests.get(author_url)
    # print(response.status_code)
    soup = BeautifulSoup(response.text , 'html.parser')
    author_linkedin=author_twitter=author_img=''

    # author name
    author_name_meta= soup.find('h1' , class_='archive-title')
    author_name = author_name_meta.text.strip() if author_name_meta else ""
    # author image
    author_image_meta = soup.find('meta' ,{'property':'og:image'})
    author_img = author_image_meta['content'] if author_image_meta else ""

        
    author_details = {"author_name": author_name, "author_img" : author_img, "author_linkedin" : author_linkedin, "author_twitter" : author_twitter}
    return author_details


def macworld_article_list(url = "https://www.macworld.com/"):
    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.6',
        'cookie': 'wbdFch=368a482c867f2186221f0aeb56e1ec749e2ef90b; countryCode=IN; FastAB=0=5189,1=9107,2=2878,3=7743,4=7276,5=6772,6=1589,7=3841,8=0805,9=4969,10=8584,11=0685,12=3549,13=6687,14=6276,15=6662,16=7091,17=7832,18=8650,19=2326; usprivacy=1---; FastAB_Zion=5.1; s_ecid=MCMID%7C07480088709520616564237507128275873012; AMCVS_7FF852E2556756057F000101%40AdobeOrg=1; s_cc=true; stateCode=KA; _sp_ses.f5fb=*; sato=1; umto=1; nexus-web-application-identifier=fdc15c95-006c-4f02-a819-7db7e74d901c|1722311063110; SecGpc=1; geoData=bagalkot|KA|587314|IN|AS|530|broadband|16.480|75.100|356004; cnprevpage_pn=%2Fbusiness%2F; _dd_s=logs=1&id=740207b1-0cca-406f-abe6-b01c4b736113&created=1722310663321&expire=1722312121015; _sp_id.f5fb=459eb680-9fee-49d9-88b7-9a98b43be2f1.1722084009.4.1722311221.1722104477.8d17cf80-9349-4027-bf4e-b358e068ed21; s_sq=cnn-adbp-domestic%3D%2526c.%2526a.%2526activitymap.%2526page%253D%25252Fbusiness%25252F%2526link%253DTech%2526region%253DpageHeader%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c; AMCV_7FF852E2556756057F000101%40AdobeOrg=179643557%7CMCIDTS%7C19935%7CMCMID%7C07480088709520616564237507128275873012%7CMCAID%7CNONE%7CMCOPTOUT-1722318421s%7CNONE%7CvVersion%7C5.5.0; wbdFch=6e3372d1f0b30a1c132db0f7aefe3dc3e7d2c4c2; SecGpc=1; countryCode=IN; geoData=davangere|KA|577006|IN|AS|530|broadband|14.460|75.910|356004; stateCode=KA',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    }
    # response = requests.get(url, headers=headers, proxies=residential_proxies, verify=ca_cert_path)
    response = requests.get(url, headers=headers)
    
    article_data = set()
    soup = BeautifulSoup(response.text, 'html.parser')
    article_tags = soup.find_all('article')
    for article in article_tags:
        link = article.find('a')['href']
        article_data.add(link)
             
    return article_data

        
        


def  macworld_article_details(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.6',
        'cookie': 'wbdFch=368a482c867f2186221f0aeb56e1ec749e2ef90b; countryCode=IN; FastAB=0=5189,1=9107,2=2878,3=7743,4=7276,5=6772,6=1589,7=3841,8=0805,9=4969,10=8584,11=0685,12=3549,13=6687,14=6276,15=6662,16=7091,17=7832,18=8650,19=2326; usprivacy=1---; FastAB_Zion=5.1; s_ecid=MCMID%7C07480088709520616564237507128275873012; AMCVS_7FF852E2556756057F000101%40AdobeOrg=1; s_cc=true; stateCode=KA; _sp_ses.f5fb=*; sato=1; umto=1; nexus-web-application-identifier=fdc15c95-006c-4f02-a819-7db7e74d901c|1722311063110; SecGpc=1; geoData=bagalkot|KA|587314|IN|AS|530|broadband|16.480|75.100|356004; cnprevpage_pn=%2Fbusiness%2F; _dd_s=logs=1&id=740207b1-0cca-406f-abe6-b01c4b736113&created=1722310663321&expire=1722312121015; _sp_id.f5fb=459eb680-9fee-49d9-88b7-9a98b43be2f1.1722084009.4.1722311221.1722104477.8d17cf80-9349-4027-bf4e-b358e068ed21; s_sq=cnn-adbp-domestic%3D%2526c.%2526a.%2526activitymap.%2526page%253D%25252Fbusiness%25252F%2526link%253DTech%2526region%253DpageHeader%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c; AMCV_7FF852E2556756057F000101%40AdobeOrg=179643557%7CMCIDTS%7C19935%7CMCMID%7C07480088709520616564237507128275873012%7CMCAID%7CNONE%7CMCOPTOUT-1722318421s%7CNONE%7CvVersion%7C5.5.0; wbdFch=6e3372d1f0b30a1c132db0f7aefe3dc3e7d2c4c2; SecGpc=1; countryCode=IN; geoData=davangere|KA|577006|IN|AS|530|broadband|14.460|75.910|356004; stateCode=KA',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # headline
    title = soup.find('meta', {'property': 'og:title'})
    title = title['content'] if title else ''
    print(title)

    # published
    published = soup.find('meta', {'name': 'date'})
    published = published['content'] if published else 'not found'

    # published_date = convert_date_format(published)


    # author
    author_tag = soup.find('span' ,class_='author vcard')
    author= author_tag.text
    author_link = author_tag.find('a')
    
# author details
    author_url =author_link['href']
    author_info = macworld_author_details(author_url)


# body
    paragraph_texts=[]
    # link_wrapped_content
    body_content = soup.find('div', id='link_wrapped_content').find_all('p')
    for para in body_content:
        paragraph_texts.append(para.text)
    article_body = ' '.join(paragraph_texts)
    # print(body_content)

    # article image
    image_url_meta = soup.find("meta", {"property": "og:image"})
    image_url = image_url_meta['content'] if image_url_meta else "" 
    # print(image_url)

    return {
        'url': url,
        'title': title,
        'author': author,
        'author_details': author_info,
        'published': published,
        # 'published_date': published_date,
        'body':article_body ,
        "image_url": image_url,

    }


# result =macworld_article_details()

if __name__ == "__main__":

    total_article_links = macworld_article_list()

    articles_data = []
   
    for url in total_article_links:        
        article_details = macworld_article_details(url)
        if article_details:
            articles_data.append(article_details)
    
    # Save scraped data to a JSON file  scraped_websites\zzsample outputs
    with open("macworld_articles.json", "w") as json_file:
        json.dump(articles_data, json_file, indent=4)

    print("Data fetched and stored in macworld_articles.json")


