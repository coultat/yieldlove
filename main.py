import requests
import functions

def hreffind(divtext, country):
    hrefbegin = divtext.rfind('href="', 0 , divtext.find(country)) + 6
    hrefend = divtext.find('"', hrefbegin )
    url = divtext[hrefbegin :hrefend]
    webdestination = "http://example.webscraping.com"+url
    return webdestination


def gettingthemaincity(urladdress):
    maincityurl = requests.get(urladdress)
    pag = maincityurl.text.find("Capital: ")
    pag = maincityurl.text.find('w">', pag) +3
    pagend = maincityurl.text.find("<", pag)
    capital = maincityurl.text[pag :pagend]
    return capital






r = requests.get("http://example.webscraping.com")

paginator = r.text.find('<div id="results">')
divend = r.text.find('<div id="pagination">')
wholediv = r.text[paginator :divend]
landnamen = []
hauptstadtnamen = []
count = y = 0
while True:
    paginator = r.text.find('</a>', paginator)
    prepaginator = r.text.rfind(">", 0, paginator) + 2

    #if paginator < divend: BORRAR Y SI FUNCIONA
    if y < 2:
        landnamen.append(r.text[prepaginator :paginator])
        urlmaincity = hreffind(wholediv, r.text[prepaginator :paginator])
        hauptstadtnamen.append(gettingthemaincity(urlmaincity))
        paginator = paginator + 1
        y = y + 1
    else:
        finallist = zip(landnamen, hauptstadtnamen)
        for garbage, trash in finallist:
            print (garbage+" which capital is: "+trash)
        x = input("\nDo you want to look the next page? ")
        if x=='y' or x=='Y':
            print("Eso es que quieres")
            count = count + 1
            nexturl = "http://example.webscraping.com/places/default/index/" + str(count)
            r = requests.get(nexturl)
            paginator = r.text.find('<div id="results">')
            wholediv = r.text[paginator :divend]
            y = 0
            continue
        else:
            break
