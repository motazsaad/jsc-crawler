import requests
import sys

from bs4 import BeautifulSoup

print_links = set()
crawled_links = set()

jsc_news_home_url = 'http://www.aljazeera.net/news/'


def crawl_links(web_url, stop=5000):
    #sys.stdout.write("\rprint_links: {0}\t crawled_links: {1}".format(len(print_links), len(crawled_links)))
    if len(print_links) > stop:
        return
    else:
        html_doc = requests.get(web_url).text
        soup = BeautifulSoup(html_doc, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            my_link = str(link.get('href'))
            if 'home/print/' in my_link:
                print_links.add(my_link)
            elif my_link.startswith('/news/') or my_link.startswith('http://www.aljazeera.net/news/'):
                if not my_link.startswith('http://www.aljazeera.net'):
                    target_link = 'http://www.aljazeera.net' + my_link
                    target_link = target_link.strip()
                else:
                    target_link = my_link
                if target_link not in crawled_links:
                    #print('\ncrawling {}'.format(target_link))
                    crawled_links.add(target_link)
                    crawl_links(target_link)


if __name__ == '__main__':
    try:
        crawl_links(jsc_news_home_url)
    except Exception as err:
        print('\nerror: {}'.format(err))
    finally:
        print('\nwriting urls')
        url_writer = open('jsc_urls.txt', mode='w')
        url_writer.write('\n'.join(print_links))
