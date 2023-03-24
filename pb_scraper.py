import requests
import re
from bs4 import BeautifulSoup


# object for torrent site scraper
class TorrentFinder:
    # constructor
    def __init__(self):
        pass

    # method to search for torrents on pirate bay
    def search_pirate_bay(self, query):
        url = 'https://piratebay.live/search/' + query + '/1/99/0'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        results = []
        x = 0
        for trs in soup.find_all('tr'):
            tds = trs.find_all('td')
            # use re to get title from element with detLink class
            title = re.search(r'(?<=title=")(.*)(?=">)', str(tds[1])).group(0) if len(tds) > 1 else None

            if title is None:
                continue

            # if Details for sting is in title, remove it
            if 'Details for ' in title:
                title = title.replace('Details for ', '')

            # get magnet link
            magnet = re.search(r'(?<=href=")(.*)(?=" title="Download this torrent using magnet")', str(tds[1])).group(0) if len(tds) > 1 else None

            # get size
            size = re.search(r'(?<=Size )(.*)(?=,)', str(tds[1])).group(0) if len(tds) > 1 else None

            # get seeders
            seeders = re.search(r'(?<=<td align="right">)(.*)(?=</td>)', str(tds[2])).group(0) if len(tds) > 2 else None

            # get leechers
            leechers = re.search(r'(?<=<td align="right">)(.*)(?=</td>)', str(tds[3])).group(0) if len(tds) > 3 else None

            dict = { 'title': title, 'magnet': magnet, 'size': size, 'seeders': seeders, 'leechers': leechers }
            # replace any  \xa0 with a space
            dict = { key: value.replace('\xa0', ' ') for key, value in dict.items() }

            results.append(dict)

        return results


if __name__ == '__main__':
    pass
