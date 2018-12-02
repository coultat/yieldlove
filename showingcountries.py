import requests
r = requests.get("http://example.webscraping.com")

#Die Länder fangen bei dem div id=results an, und beenden bei div id=pagination
divbegin = r.text.find('<div id="results">')
divend = r.text.find('<div id="pagination">')
count = 0
paginador = divbegin
#Alle Länder stehen zwischen ein " " und "</a>"
while paginador < divend:
    paginador = r.text.find("</a>",paginador+1)
    count = r.text.rfind(" ",0,paginador)
    print(r.text[count+1 :paginador])
    if (paginador > divend):
        break
