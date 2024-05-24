import requests
import re
from bs4 import BeautifulSoup


# object for torrent site scraper
class TorrentFinder:
    # constructor
    def __init__(self):
        pass

    # method to search for torrents on pirate bay
    def search_hd_movies(self, query):
        url = 'https://prbay.top/search/' + query + '/1/99/207'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        results = []
        for trs in soup.find_all('tr'):
            tds = trs.find_all('td')

            if len(tds) > 1:
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

                result = { 'title': title, 'magnet': magnet, 'size': size, 'seeders': seeders, 'leechers': leechers }
                result = { key: value.replace('\xa0', ' ') if value else value for key, value in result.items() }
                results.append(result)

        return results

    def search_movies(self, query):
        url = 'https://prbay.top/search/' + query + '/1/99/201'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        results = []
        for trs in soup.find_all('tr'):
            tds = trs.find_all('td')

            if len(tds) > 1:
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

                result = { 'title': title, 'magnet': magnet, 'size': size, 'seeders': seeders, 'leechers': leechers }
                result = { key: value.replace('\xa0', ' ') if value else value for key, value in result.items() }
                results.append(result)

        return results

    def search_hd_tv_shows(self, query):
        url = 'https://prbay.top/search/' + query + '/1/99/208'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        results = []
        for trs in soup.find_all('tr'):
            tds = trs.find_all('td')

            if len(tds) > 1:
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

                result = { 'title': title, 'magnet': magnet, 'size': size, 'seeders': seeders, 'leechers': leechers }
                result = { key: value.replace('\xa0', ' ') if value else value for key, value in result.items() }
                results.append(result)

        return results

    def search_tv_shows(self, query):
        url = 'https://prbay.top/search/' + query + '/1/99/205'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        results = []
        for trs in soup.find_all('tr'):
            tds = trs.find_all('td')

            if len(tds) > 1:
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

                result = { 'title': title, 'magnet': magnet, 'size': size, 'seeders': seeders, 'leechers': leechers }
                result = { key: value.replace('\xa0', ' ') if value else value for key, value in result.items() }
                results.append(result)

        return results
        

if __name__ == '__main__':
    pass
