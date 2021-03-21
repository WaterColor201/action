import requests
from os import path


class BiliPipeline:
    def process_item(self, item, spider):
        name = item["title"] + '-' + str(item["id"]) + '.' + item["extension"]
        res = requests.get(item["url"])
        with open(path.join(path.join(path.abspath('.'), 'image'), name), 'wb') as file:
            file.write(res.content)
            print(name)
        return item
