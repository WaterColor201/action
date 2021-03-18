import requests
from lxml import html

res = requests.get(
        r"https://www.bing.com/HPImageArchive.aspx",
        params={
            "n": 1,
            "format": "xml"
        }, )
sel = html.fromstring(res.content)
name = sel.xpath(r'//copyright/text()')[0].split(" ")[0].split("，")
name = name[0] + '-' + name[1] + ".jpg"
url = sel.xpath(r'//url/text()')[0].split("_")
url = "https://cn.bing.com" + url[0] + '_' + url[1] + "_1920x1200.jpg"
time = sel.xpath(r'//enddate/text()')[0]
res = requests.get(url)
with open(name, 'wb') as file:
    file.write(res.content)
