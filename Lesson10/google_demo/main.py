pip install beautifulsoup4



from dataclasses import dataclass
from typing import List
import requests
from bs4 import BeautifulSoup

#---------------------------------------------------------------
## verkar inte funka
## det är en web sida som pajar, kan inte läsas
#------------------------------------------------------------

@dataclass
class Contact:
    email: str
    phone: str


@dataclass
class TopSite:
    rank: int
    url: str
    google_text: str
    contact: Contact | None = None


# Cookie för att komma förbi cookie bannern, acceptera cookies i incognito och kolla efter en cookie som hete SOCS
cookies = {"SOCS": "CAESHAgCEhJnd3NfMjAyMjEyMDUtMF9SQzMaAnN2IAEaBgiAvI6dBg"}

# Urlen är bara att kopiera från google.
url = "https://www.google.com/search?q=webbbyr%C3%A5+stockholm"

page = requests.get(url, headers={"USer-Agent": "Mozilla/5.0"}, cookies=cookies)


soup = BeautifulSoup(page.text, "html.parser")
tags = soup.find_all("a")
# print(soup.find("a"))
# print(tags)

# # Rank är för att visa var den ligger i google sökningen
rank = 1

# # Vi sparar alla i en lista med våra top sites
top_sites: List[TopSite] = []

for tag in tags:
    # Rensar bort alla som pekar til lsidan vi är
    if tag["href"] == "#":
        continue

    # Rensar alla google länkar
    elif "google" in tag["href"]:
        continue

    # Rensar alla google search länkar
    elif "search" in tag["href"]:
        continue

    # Rensar alla länkar som är suggestions
    elif tag["href"].startswith("/?"):
        # print(tag)
        continue

    # Hämtar url till sidan
    site_rank = rank

    # Rensar upp URLEN för att bara behålla själva länken
    url = tag["href"].split("=")[1].split("&")[0]
    # print(url)
    
#     # Alternativt sätt att göra ovan
#     # url = url.split("=")[1]
#     # url = url.split("&")[0]

    # Sparar texten
    text = tag.text
    # print(text)

    # Skapar en site och lägger till i våran lista
    site = TopSite(site_rank, url, text)
    top_sites.append(site)

    # Ökar rank för att nästa ska vara nästa i rank
    rank += 1
    # print(top_sites)


for site in top_sites:
    # print(site.url)
    # Special case  för att wasabi strular
    if site.rank ==  3 and 2 and 4 and 5 and 6 and 7 and 9 :
        # print("Wasabi web sucks")
        # print(site.url)
        continue

    # Ny request för varje url vi sparat
    site_page_res = requests.get(site.url)
    print(site_page_res)
    if site_page_res.status_code == 403:
        print()
        print("Innaccessible page")
        continue
    else:
        site_page = site_page_res.text
        site_soup = BeautifulSoup(site_page, "html.parser")

    #     # Hämtar alla a taggar
    #     site_a_tags = site_soup.find_all("a")
    #     # print(site_a_tags)
#----------------------------------------------------------
        # Initierar variabler för att spara m,ail och tel_nummer
        # site_mail = ""
        # site_phone = ""
        # for site_a_tag in site_a_tags:
        #     print(site_a_tag)            
            # Kolla att a taggen har en href
            # if site_a_tag.has_attr("href"):
                # Om det är en mail href Spara i den variabeln
                # if "mailto" in site_a_tag["href"]:
                #     if site_mail:
                        # print(site_a_tag["href"])
                        # continue
#                     site_mail = site_a_tag.text.strip()
#                 # Om det är en telefon href Spara i den variabeln
#                 elif "tel" in site_a_tag["href"]:
#                     if site_phone:
#                         continue
#                     site_phone = site_a_tag.text.strip()

#             # När vi har en av varje breaka loopen
#             if site_phone and site_mail:
#                 site.contact = Contact(site_mail, site_phone)
#                 break


# for site in top_sites:
#     print(site)


