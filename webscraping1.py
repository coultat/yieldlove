import requests
r = requests.get("http://example.webscraping.com")
country = " Afghanistan"
position = r.text.find(country)
#finding the closest <a href=" through rfind
afghanlink = r.text.rfind('href="',0,position)
afghanlink += 6

#finding the ending of the href bracket

afghanend = r.text.find('"',afghanlink)
web = "http://example.webscraping.com" + r.text[afghanlink:afghanend]
q = requests.get(web)
print(q.text)
