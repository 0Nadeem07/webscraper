import requests
from datetime import datetime
from bs4 import BeautifulSoup
import json
import re

def techmeme_article_list(base_url="https://www.techmeme.com/"):

    # base_url = "https://www.techmeme.com/"

    # residential_proxies = {'http': 'http://brd-customer-hl_5f7bc336-zone-nad_webunlocker:nlevo8vx0tsw@brd.superproxy.io:22225',
    #         'https': 'http://brd-customer-hl_5f7bc336-zone-nad_webunlocker:nlevo8vx0tsw@brd.superproxy.io:22225'}
    
    # ca_cert_path = 'ca.crt'

    payload = {}
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,en-IN;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': '_vwo_uuid_v2=DCD1E05F115A9A945941D2C2F5D0DC2ED|d761ac1c16c696026f5937e7ec240c83; pushly.user_puuid_GvbR9fxg=Ahfglpx1RxK9CzIcOueNyyf0T1YTenAT; _pnss_GvbR9fxg=none; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAEzIEYOBmAVgCZ%2B3ABwB2cQDYB40fwAMIAL5A; _pcid=%7B%22browserId%22%3A%22lz9wrshm3h03ewbz%22%7D; __pid=.fortune.com; __pat=-14400000; _pbjs_userid_consent_data=3524755945110770; _li_dcdm_c=.fortune.com; _lc2_fpi=00366f952340--01j44h4axmzwd4593sgrxwv7sq; _pubcid=dab487b4-4f6f-4644-8e1c-50fe4d49f6f7; cX_G=cx%3A1gs1g24nstwp51ms3ujd003qer%3A39sx8lloxbbqs; permutive-id=45ee7083-b9f3-4ca2-abda-d60e025d3e4b; _pnlspid_GvbR9fxg=29459; ajs_anonymous_id=a54a6391-e327-46b4-9902-b927cc5cb80d; _ga=GA1.1.1936473159.1722434075; _gcl_au=1.1.93871804.1722434075; _lr_retry_request=true; _lr_env_src_ats=false; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://fortune.com/%22%2C%22sref%22:%22%22%2C%22sts%22:1722434076660%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=3db77d5f-a737-4eef-8ea9-f5d7e9d69a71%22%2C%22session_count%22:1%2C%22last_session_ts%22:1722434076660}; _ce.irv=new; cebs=1; _ce.clock_event=1; pbjs-unifiedid=%7B%22TDID%22%3A%22db70ec1e-7260-4161-b586-dfacdfd438bf%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222024-07-31T13%3A54%3A37%22%7D; panoramaId_expiry=1722520477310; _cc_id=d3ea27bf2c58f0b63af6cb4266d081a; panoramaId=d71fdea5f489bfd90eee42d092dda9fb927a132323e7291c64e7f96cff70f69c; __li_idex_cache_e30=%7B%7D; pbjs_li_nonid=%7B%7D; _ce.clock_data=505%2C152.58.16.203%2C1%2Cc28c178f7fc01e92a5161b6c80153add%2CEdge%2CIN; _CEFT=Q%3D%3D%3D; bounceClientVisit6717v=N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgGYD2ATggK4B2ApgHQDGpAtkSADQjkwhcgAligD6Ac1IiUdFCkGkaMYgEMw07sPEQpMuQqWrpAXyA; __pnahc=0; __pvi=eyJpZCI6InYtbHo5d3JzaXJobmtqZ3U1dyIsImRvbWFpbiI6Ii5mb3J0dW5lLmNvbSIsInRpbWUiOjE3MjI0MzQxMTkxMjh9; __tbc=%7Bkpex%7DfXfGjj5poN4GJhijJ-LSb-OfhPYOwqyObQhWQKNQf29gXV-1yL6pUGiO6fHiK9w0; xbc=%7Bkpex%7Dy-v5j-NmbMgnRKQvRGNIRHLBsxr4b55HfwBSbzR7oio; _pcus=eyJ1c2VyU2VnbWVudHMiOnsiQ09NUE9TRVIxWCI6eyJzZWdtZW50cyI6WyJMVHM6MDVjNTVjYTVmODM1ZDk0N2YxNjBjYjRkZDJmZTg3ZmFlZDE2N2IyMTo5IiwiTFRjOjE2NmIxNDEzMzViYWJlODJjMmRiMWFhNTM1NGIzZTkwNjUzMmY5ODk6bm9fc2NvcmUiLCJDU2NvcmU6NjE0NzMxN2NmZjEzYjRhNTljMzBlOWJhNGQwMTdjODBlNTRkMmRjMjpub19zY29yZSIsIkxUcmVnOmQ1NzUxODQ4NzU1ZmU2MDUwYzk0OWJhY2M3Y2YxMDY2NGEwOWE0MWE6NSIsIkxUcmV0dXJuOmUwNmFhMTFlNmNlMmNlNzcxMDFlZDg2ZTRhYmMwNGFhZTNmZDNhN2Q6NiJdfX19; cebsp_=3; _ga_T498R2CHRG=GS1.1.1722434075.1.1.1722434221.0.0.0; cX_P=lz9wrshm3h03ewbz; __gads=ID=6b7c692932b2cb48:T=1722434074:RT=1722435635:S=ALNI_MbWVEG-VhNCsGDomMWdkGRXRlDNWw; __gpi=UID=00000eaf67503499:T=1722434074:RT=1722435635:S=ALNI_MZDBFbd61beXdMQUqD-evW7h0Q12A; __eoi=ID=9ca5d673baf11f5c:T=1722434074:RT=1722435635:S=AA-AfjYMUJHcje8xz_lHbiaZ4UoS; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Jul+31+2024+19%3A51%3A12+GMT%2B0530+(India+Standard+Time)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=1311a5dd-98eb-4ce6-8b6a-f7ec507128c3&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Ffortune.com%2F&groups=C0001%3A1%2CC0003%3A1%2CSSPD_BG%3A1%2CC0005%3A1%2CC0004%3A1%2CC0002%3A1; _ce.s=v~f79cabb6d3df54c30783b5c1c6929e3c2bd50837~lcw~1722435668810~lva~1722434077746~vpv~0~v11.cs~388300~v11.s~6dec5530-4f44-11ef-b947-6df8f7a7e84b~v11.sla~1722435668807~gtrk.la~lz9xq0vy~v11.send~1722435672722~lcw~1722435672722; bounceClientVisit6717=N4IgJglmIFwgjAJkQThQBhQdgCzoBwBsAzMTvouuiADQgBuUs8WyOZBArIp8YvljoAzegBdmrROxxJBIAIYB7WOjoAbAA6wQAC1GiNAZwCkxAILHEAMUtWhigE6iArgDsApgDoAxooC2trQKhip09Br0sIh00HDQdA7aQd5iEmwc+Jx0hkww8MR0AObeiTDIdH6hIGqpeZLSsjGFVhAOhqIAMorysaIOzu4AvkA',
    'if-none-match': '"gfnjc31pizb917"',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }
    response = requests.get(base_url, data=payload, headers=headers )
    print(response.status_code)
    if response.status_code == 200:
        article_links =set()
        soup = BeautifulSoup(response.text ,'html.parser')

        article_div = soup.find_all('div', class_ = 'ii')
        if article_div:
            for article in article_div:
                link = article.find('a')
                url = link['href']
                if not ('mediagazer.com' in url  or url.startswith('/r2/')):
                    # print(url)
                    article_links.add(url)
                
        else:
            print("Article section was not found")            
        return article_links
    
    else:
        print({'error': 'Failed to retrieve the page', 'status_code': response.status_code})

# techmeme_article_list()


def techmeme_article_details(url):
    # residential_proxies = {'http': 'http://brd-customer-hl_5f7bc336-zone-nad_webunlocker:nlevo8vx0tsw@brd.superproxy.io:22225',
    #         'https': 'http://brd-customer-hl_5f7bc336-zone-nad_webunlocker:nlevo8vx0tsw@brd.superproxy.io:22225'}
    
    # ca_cert_path = 'ca.crt'

    payload = {}
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,en-IN;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': '_vwo_uuid_v2=DCD1E05F115A9A945941D2C2F5D0DC2ED|d761ac1c16c696026f5937e7ec240c83; pushly.user_puuid_GvbR9fxg=Ahfglpx1RxK9CzIcOueNyyf0T1YTenAT; _pnss_GvbR9fxg=none; _pctx=%7Bu%7DN4IgrgzgpgThIC4B2YA2qA05owMoBcBDfSREQpAeyRCwgEt8oBJAEzIEYOBmAVgCZ%2B3ABwB2cQDYB40fwAMIAL5A; _pcid=%7B%22browserId%22%3A%22lz9wrshm3h03ewbz%22%7D; __pid=.fortune.com; __pat=-14400000; _pbjs_userid_consent_data=3524755945110770; _li_dcdm_c=.fortune.com; _lc2_fpi=00366f952340--01j44h4axmzwd4593sgrxwv7sq; _pubcid=dab487b4-4f6f-4644-8e1c-50fe4d49f6f7; cX_G=cx%3A1gs1g24nstwp51ms3ujd003qer%3A39sx8lloxbbqs; permutive-id=45ee7083-b9f3-4ca2-abda-d60e025d3e4b; _pnlspid_GvbR9fxg=29459; ajs_anonymous_id=a54a6391-e327-46b4-9902-b927cc5cb80d; _ga=GA1.1.1936473159.1722434075; _gcl_au=1.1.93871804.1722434075; _lr_retry_request=true; _lr_env_src_ats=false; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://fortune.com/%22%2C%22sref%22:%22%22%2C%22sts%22:1722434076660%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=3db77d5f-a737-4eef-8ea9-f5d7e9d69a71%22%2C%22session_count%22:1%2C%22last_session_ts%22:1722434076660}; _ce.irv=new; cebs=1; _ce.clock_event=1; pbjs-unifiedid=%7B%22TDID%22%3A%22db70ec1e-7260-4161-b586-dfacdfd438bf%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREATED_AT%22%3A%222024-07-31T13%3A54%3A37%22%7D; panoramaId_expiry=1722520477310; _cc_id=d3ea27bf2c58f0b63af6cb4266d081a; panoramaId=d71fdea5f489bfd90eee42d092dda9fb927a132323e7291c64e7f96cff70f69c; __li_idex_cache_e30=%7B%7D; pbjs_li_nonid=%7B%7D; _ce.clock_data=505%2C152.58.16.203%2C1%2Cc28c178f7fc01e92a5161b6c80153add%2CEdge%2CIN; _CEFT=Q%3D%3D%3D; bounceClientVisit6717v=N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgGYD2ATggK4B2ApgHQDGpAtkSADQjkwhcgAligD6Ac1IiUdFCkGkaMYgEMw07sPEQpMuQqWrpAXyA; __pnahc=0; __pvi=eyJpZCI6InYtbHo5d3JzaXJobmtqZ3U1dyIsImRvbWFpbiI6Ii5mb3J0dW5lLmNvbSIsInRpbWUiOjE3MjI0MzQxMTkxMjh9; __tbc=%7Bkpex%7DfXfGjj5poN4GJhijJ-LSb-OfhPYOwqyObQhWQKNQf29gXV-1yL6pUGiO6fHiK9w0; xbc=%7Bkpex%7Dy-v5j-NmbMgnRKQvRGNIRHLBsxr4b55HfwBSbzR7oio; _pcus=eyJ1c2VyU2VnbWVudHMiOnsiQ09NUE9TRVIxWCI6eyJzZWdtZW50cyI6WyJMVHM6MDVjNTVjYTVmODM1ZDk0N2YxNjBjYjRkZDJmZTg3ZmFlZDE2N2IyMTo5IiwiTFRjOjE2NmIxNDEzMzViYWJlODJjMmRiMWFhNTM1NGIzZTkwNjUzMmY5ODk6bm9fc2NvcmUiLCJDU2NvcmU6NjE0NzMxN2NmZjEzYjRhNTljMzBlOWJhNGQwMTdjODBlNTRkMmRjMjpub19zY29yZSIsIkxUcmVnOmQ1NzUxODQ4NzU1ZmU2MDUwYzk0OWJhY2M3Y2YxMDY2NGEwOWE0MWE6NSIsIkxUcmV0dXJuOmUwNmFhMTFlNmNlMmNlNzcxMDFlZDg2ZTRhYmMwNGFhZTNmZDNhN2Q6NiJdfX19; cebsp_=3; _ga_T498R2CHRG=GS1.1.1722434075.1.1.1722434221.0.0.0; cX_P=lz9wrshm3h03ewbz; __gads=ID=6b7c692932b2cb48:T=1722434074:RT=1722435635:S=ALNI_MbWVEG-VhNCsGDomMWdkGRXRlDNWw; __gpi=UID=00000eaf67503499:T=1722434074:RT=1722435635:S=ALNI_MZDBFbd61beXdMQUqD-evW7h0Q12A; __eoi=ID=9ca5d673baf11f5c:T=1722434074:RT=1722435635:S=AA-AfjYMUJHcje8xz_lHbiaZ4UoS; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Jul+31+2024+19%3A51%3A12+GMT%2B0530+(India+Standard+Time)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=1311a5dd-98eb-4ce6-8b6a-f7ec507128c3&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Ffortune.com%2F&groups=C0001%3A1%2CC0003%3A1%2CSSPD_BG%3A1%2CC0005%3A1%2CC0004%3A1%2CC0002%3A1; _ce.s=v~f79cabb6d3df54c30783b5c1c6929e3c2bd50837~lcw~1722435668810~lva~1722434077746~vpv~0~v11.cs~388300~v11.s~6dec5530-4f44-11ef-b947-6df8f7a7e84b~v11.sla~1722435668807~gtrk.la~lz9xq0vy~v11.send~1722435672722~lcw~1722435672722; bounceClientVisit6717=N4IgJglmIFwgjAJkQThQBhQdgCzoBwBsAzMTvouuiADQgBuUs8WyOZBArIp8YvljoAzegBdmrROxxJBIAIYB7WOjoAbAA6wQAC1GiNAZwCkxAILHEAMUtWhigE6iArgDsApgDoAxooC2trQKhip09Br0sIh00HDQdA7aQd5iEmwc+Jx0hkww8MR0AObeiTDIdH6hIGqpeZLSsjGFVhAOhqIAMorysaIOzu4AvkA',
    'if-none-match': '"gfnjc31pizb917"',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }
    print('*****************************')
    # print(url)
    response = requests.get(url, data=payload, headers=headers )

    if response.status_code == 200:
        title = published = published_date = author = body_content = ""

        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find('meta', {'property': 'og:title'})
        title = title['content'] if title else ''

        desc = soup.find('meta', {'property': 'og:description'})
        desc = desc['content'][:100] if desc else ''

        body_content = []
        json_ld_pattern = re.compile(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', re.DOTALL)
        match = json_ld_pattern.search(response.text)

        if match:
            json_ld_data = match.group(1)

            # Regex to find the datePublished and author
            date_published_pattern = re.compile(r'"datePublished"\s*:\s*"([^"]+)"')
            author_pattern = re.compile(r'"@type"\s*:\s*"Person".*?"name"\s*:\s*"([^"]+)"', re.DOTALL)

            # Find datePublished
            date_published_match = date_published_pattern.search(json_ld_data)
            published = date_published_match.group(1) if date_published_match else ''
            published_date = published[:10] if published else ''

            # Find author
            author_match = author_pattern.search(json_ld_data)
            author = author_match.group(1) if author_match else ''

            # Find articleBody using a slightly more robust pattern
            article_body_pattern = r'"articleBody"\s*:\s*"([^"]*?)"'
            article_body = re.search(article_body_pattern, json_ld_data)
            body = article_body.group(1) if article_body else ''

            # If articleBody is found, append it to body_content
            if body:
                # print('article body found')
                body_content.append(body)
            else:
                # print('article body not found, extracting main body content')

                # Fallback to finding <main> or <body> content
                main_body = soup.find('main')
                if not main_body:
                    main_body = soup.find('body')

                # total_para = []
                filtered_text = None

                if main_body:
                    paras = main_body.find_all('p')
                    main_p = ''.join(para.text for para in paras) if paras else main_body.text

                    # Attempt to filter content based on description (desc)
                    start_index = main_p.find(desc) if 'desc' in locals() else -1
                    filtered_text = main_p[start_index:] if start_index != -1 else main_p

                if filtered_text:
                    body_content.append(filtered_text)
                else:
                    print("No content found in main or body tag.")

            # Omit result if body_content is empty
            if not body_content:
                # print("***********Omitting this URL***********")
                return None

        else:
            print("No JSON-LD found.")

            # Fallback logic if no JSON-LD data found  article:published_time
            pub_attrs = [{'property':'article:published_time'}, {'itemprop': 'datePublished'}, {'name': 'parsely-pub-date'}, {'name': 'article:published_time'},{'name':'article.published'}]
            published = ''
            for attrs in pub_attrs:
                meta_published = soup.find('meta', attrs)
                if meta_published:
                    published = meta_published['content']
                    published_date = meta_published['content'].split('T')[0]
            # print(published)
# article:author  property
            auth_attrs = [{'property':'article:author'}, {'name': 'article:author'}, {'name': 'parsely-author'} ,{'name':'author'}]
            author = ''
            for attr in auth_attrs:
                meta_author = soup.find('meta', attr)
                if meta_author:
                    author = meta_author['content']
                    break
            # print(author)

            # Fallback extraction of body content from <main> or <body>
            main_body = soup.find('main')
            if not main_body:
                main_body = soup.find('body')

            # total_para = []
            filtered_text = None

            if main_body:
                paras = main_body.find_all('p')
                main_p = ''.join(para.text for para in paras) if paras else main_body.text

                # Attempt to filter content based on description (desc)
                start_index = main_p.find(desc) if 'desc' in locals() else -1
                filtered_text = main_p[start_index:] if start_index != -1 else main_p

            if filtered_text:
                body_content.append(filtered_text)
            else:
                print("No content found in main or body tag.")

            # Omit result if body_content is empty
            if not body_content:
                print("***********Omitting this URL***********")
                return None

        # Return the final data if body_content exists
        return {
            'url': url,
            'title': title,
            'published': published,
            'publish_date': published_date,
            'author': author,
            'body': body_content,
        }




if __name__ == "__main__":

    total_article_links = techmeme_article_list()
    print(f"{len(total_article_links)} article links collected ")
    print(total_article_links)

    articles_data = []
    for url in total_article_links:        
        article_details = techmeme_article_details(url)
        print(f"scraping {url}")
        if article_details:
            articles_data.append(article_details)
    print('/n')
    print(len(articles_data) , 'out of', len(total_article_links) , 'were scraped')
    # Save scraped data to a JSON file
    with open("zzsample_outputs/thememe_articles00.json", "w") as json_file:
        json.dump(articles_data, json_file, indent=4)

    print("Data fetched and stored in theblock_articles.json")
