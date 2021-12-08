import os
import urllib.request


data_dir = "d:/Python Nauka/Strony"

pages = [

    {'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},

    {'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'}]


for item in pages:

    try:
        fileName = (item["name"]+".html")
        print(fileName)
        path = os.path.join(data_dir, fileName)

        urllib.request.urlretrieve(item["url"], path)

    except:
        print("Failure processing web page: " + item["name"])
        break
else:
    ("Pages are download succesfully")
