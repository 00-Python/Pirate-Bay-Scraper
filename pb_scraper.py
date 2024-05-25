import requests
import re
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# object for torrent site scraper
class TorrentFinder:
    # constructor
    def __init__(self):
        self.base_domain = 'tprbay.xyz'  # Update the base domain

    def fetch_html(self, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text

    # method to search for torrents on pirate bay
    def search_hd_movies(self, query):
        try:
            url = f'https://{self.base_domain}/search/{query}/1/99/207'
            logging.info(f'Searching HD movies with query: {query}')
            html = self.fetch_html(url)
            logging.debug(f'HTML content: {html[:500]}')  # Log the first 500 characters of the HTML content
            soup = BeautifulSoup(html, 'html.parser')

            results = []
            for trs in soup.find_all('tr'):
                tds = trs.find_all('td')

                if len(tds) > 1:
                    logging.debug(f'Table row content: {tds}')
                    # Find the link tag containing the magnet link
                    magnet_link_tag = tds[1].find('a', href=True, title="Download this torrent using magnet")

                    if magnet_link_tag:
                        magnet = magnet_link_tag['href']
                    else:
                        magnet = None

                    title_tag = tds[1].find('a', class_='detLink')
                    if title_tag:
                        title = title_tag.get('title', '').replace('Details for ', '')
                    else:
                        title = None

                    size_match = re.search(r'(?<=Size )(.*)(?=,)', str(tds[1]))
                    size = size_match.group(0) if size_match else None

                    seeders = tds[2].text if len(tds) > 2 else None
                    leechers = tds[3].text if len(tds) > 3 else None

                    result = {'title': title, 'magnet': magnet, 'size': size, 'seeders': seeders, 'leechers': leechers}
                    result = {key: value.replace('\xa0', ' ') if value else value for key, value in result.items()}
                    results.append(result)

            return results
        except requests.exceptions.RequestException as e:
            logging.error(f'Network error occurred: {e}', exc_info=True)
            return []
        except Exception as e:
            logging.error(f'Error occurred while searching HD movies: {e}', exc_info=True)
            return []

    def search_movies(self, query):
        try:
            url = f'https://{self.base_domain}/search/{query}/1/99/201'
            logging.info(f'Searching movies with query: {query}')
            html = self.fetch_html(url)
            logging.debug(f'HTML content: {html[:500]}')
            soup = BeautifulSoup(html, 'html.parser')

            results = []
            for trs in soup.find_all('tr'):
                tds = trs.find_all('td')

                if len(tds) > 1:
                    logging.debug(f'Table row content: {tds}')
                    # Find the link tag containing the magnet link
                    magnet_link_tag = tds[1].find('a', href=True, title="Download this torrent using magnet")

                    if magnet_link_tag:
                        magnet = magnet_link_tag['href']
                    else:
                        magnet = None

                    title_tag = tds[1].find('a', class_='detLink')
                    if title_tag:
                        title = title_tag.get('title', '').replace('Details for ', '')
                    else:
                        title = None

                    size_match = re.search(r'(?<=Size )(.*)(?=,)', str(tds[1]))
                    size = size_match.group(0) if size_match else None

                    seeders = tds[2].text if len(tds) > 2 else None
                    leechers = tds[3].text if len(tds) > 3 else None

                    result = {'title': title, 'magnet': magnet, 'size': size, 'seeders': seeders, 'leechers': leechers}
                    result = {key: value.replace('\xa0', ' ') if value else value for key, value in result.items()}
                    results.append(result)

            return results
        except requests.exceptions.RequestException as e:
            logging.error(f'Network error occurred: {e}', exc_info=True)
            return []
        except Exception as e:
            logging.error(f'Error occurred while searching movies: {e}', exc_info=True)
            return []

    def search_hd_tv_shows(self, query):
        try:
            url = f'https://{self.base_domain}/search/{query}/1/99/208'
            logging.info(f'Searching HD TV shows with query: {query}')
            html = self.fetch_html(url)
            logging.debug(f'HTML content: {html[:500]}')
            soup = BeautifulSoup(html, 'html.parser')

            results = []
            for trs in soup.find_all('tr'):
                tds = trs.find_all('td')

                if len(tds) > 1:
                    logging.debug(f'Table row content: {tds}')
                    # Find the link tag containing the magnet link
                    magnet_link_tag = tds[1].find('a', href=True, title="Download this torrent using magnet")

                    if magnet_link_tag:
                        magnet = magnet_link_tag['href']
                    else:
                        magnet = None

                    title_tag = tds[1].find('a', class_='detLink')
                    if title_tag:
                        title = title_tag.get('title', '').replace('Details for ', '')
                    else:
                        title = None

                    size_match = re.search(r'(?<=Size )(.*)(?=,)', str(tds[1]))
                    size = size_match.group(0) if size_match else None

                    seeders = tds[2].text if len(tds) > 2 else None
                    leechers = tds[3].text if len(tds) > 3 else None

                    result = {'title': title, 'magnet': magnet, 'size': size, 'seeders': seeders, 'leechers': leechers}
                    result = {key: value.replace('\xa0', ' ') if value else value for key, value in result.items()}
                    results.append(result)

            return results
        except requests.exceptions.RequestException as e:
            logging.error(f'Network error occurred: {e}', exc_info=True)
            return []
        except Exception as e:
            logging.error(f'Error occurred while searching HD TV shows: {e}', exc_info=True)
            return []

    def search_tv_shows(self, query):
        try:
            url = f'https://{self.base_domain}/search/{query}/1/99/205'
            logging.info(f'Searching TV shows with query: {query}')
            html = self.fetch_html(url)
            logging.debug(f'HTML content: {html[:500]}')
            soup = BeautifulSoup(html, 'html.parser')

            results = []
            for trs in soup.find_all('tr'):
                tds = trs.find_all('td')

                if len(tds) > 1:
                    logging.debug(f'Table row content: {tds}')
                    # Find the link tag containing the magnet link
                    magnet_link_tag = tds[1].find('a', href=True, title="Download this torrent using magnet")

                    if magnet_link_tag:
                        magnet = magnet_link_tag['href']
                    else:
                        magnet = None

                    title_tag = tds[1].find('a', class_='detLink')
                    if title_tag:
                        title = title_tag.get('title', '').replace('Details for ', '')
                    else:
                        title = None

                    size_match = re.search(r'(?<=Size )(.*)(?=,)', str(tds[1]))
                    size = size_match.group(0) if size_match else None

                    seeders = tds[2].text if len(tds) > 2 else None
                    leechers = tds[3].text if len(tds) > 3 else None

                    result = {'title': title, 'magnet': magnet, 'size': size, 'seeders': seeders, 'leechers': leechers}
                    result = {key: value.replace('\xa0', ' ') if value else value for key, value in result.items()}
                    results.append(result)

            return results
        except requests.exceptions.RequestException as e:
            logging.error(f'Network error occurred: {e}', exc_info=True)
            return []
        except Exception as e:
            logging.error(f'Error occurred while searching TV shows: {e}', exc_info=True)
            return []

if __name__ == '__main__':
    query = "Batman"

    scraper = TorrentFinder()
    res = scraper.search_hd_movies(query)

    print(res)
