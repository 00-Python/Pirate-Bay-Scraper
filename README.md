# OOP-Pirate-Bay-Scraper
An Object Oriented scrapper that searches piratebay.live for torrents and returns dictionary with Filenames, Sizes, magnets, seeds, leeches

## Modules required:
1. requests
1. re
1. bs4

## How to use?
First, clone this repository, then install the required modules with pip.       
    `git clone https://github.com/00-Python/OOP-Pirate-Bay-Scraper.git`   
    `cd OOP-Pirate-Bay-Scrapper`  
    `pip install requests re beautifulsoup4`

Once you have installed the modules you can create a blank python file i.e. torrents.py 
```
# Inside your python file import the the scrapper
from pb_scrapper import TorrentFinder

# then create an instance of the object
scrape = TorrentFinder()

# and then you can use the search_pirate_bay method to scrape the data
data = scrape.search_pirate_bay('batman') # Replace batman for desired SEARCH TERM

# the raw data is a list of dictionaries with the following keys: title, magnet, size, seeders, leechers

# view data pretty
for result in data:
    print('Title: ' + result['title'])
    print('Magnet: ' + result['magnet'])
    print('Size: ' + result['size'])
    print('Seeders: ' + result['seeders'])
    print('Leechers: ' + result['leechers'])
    print()
    print('____________________________________________________')

# view data raw
print(data)

```

An example output searching for 'batman' would be:
```
Title: The Batman (2022) [1080p] [WEBRip] [5.1]
Magnet: magnet:?xt=urn:vsjdkbjlk;nvbksbdjacsjcldvbjldpnklmb
Size: 3.25 GiB
Seeders: 995
Leechers: 150

____________________________________________________
Title: Batman.The.Doom.That.Came.to.Gotham.2023.720p.WEBRip.800MB.x264-
Magnet: magnet:?xt=usnkdsbn,sdbvklsnvfb
Size: 796.92 MiB
Seeders: 811
Leechers: 37

____________________________________________________
Title: The Batman (2022) 1080p HDRip x264 - ProLover
Magnet: magnet:?xt=urn:btvhkdjblvksn;svbjlkn;cm'dvn;kbsdnk;
Size: 1.19 GiB
Seeders: 691
Leechers: 87

____________________________________________________


[{'title': 'The Batman (2022) [1080p] [WEBRip] [5.1]', 'magnet': 'magnet:?xt=urn:vsjdkbjlk;nvbksbdjacsjcldvbjldpnklmb', 'size': '3.25 GiB', 'seeders': '936', 'leechers': '158'}, {'title': 'Batman.The.Doom.That.Came.to.Gotham.2023.720p.WEBRip.800MB.x264-', 'magnet': 'magnet:?xt=usnkdsbn,sdbvklsnvfb', 'size': '796.92 MiB', 'seeders': '721', 'leechers': '32'}, {'title': 'The Batman (2022) 1080p HDRip x264 - ProLover', 'magnet': 'agnet:?xt=urn:btvhkdjblvksn;svbjlkn;cm'dvn;kbsdnk;', 'size': '1.19 GiB', 'seeders': '640', 'leechers': '83'}]
```
