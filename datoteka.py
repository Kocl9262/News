import urllib2

stran = urllib2.urlopen("http://www.shortnews.com/start.cfm?id=100422")
tekst = stran.read().decode("utf-8")

nzac = tekst.find("<h1>April Fools")
nkon = nzac + 70
naslov = tekst[nzac:nkon]

print(naslov)

azac = tekst.find("edie")
akon = azac + 4
avtor = tekst[azac:akon]

print(avtor)

czac = tekst.find("<p>In spirit")
ckon = tekst.find("concludes.") + 14
clanek = tekst[czac:ckon]

print(clanek)
stran.close()

html = open("index.html", "w")
html.write("<!DOCTYPE html>")
html.write("<html><head></head><body>")
html.write(naslov + " " + "<p>Avtor:" + " " + avtor + "</p>" + " " + clanek)
html.write("</body>")
html.close()
