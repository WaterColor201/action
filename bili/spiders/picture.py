import json
import scrapy
import time
import setting
from bili.items import BiliItem


class PictureSpider(scrapy.Spider):
    name = 'picture'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://h.bilibili.com/']

    def parse(self, response, **kwargs):
        for i in range(setting.PICTURE_MAX_PAGE):
            yield scrapy.Request(
                'https://api.vc.bilibili.com/link_draw/v2/Doc/list?page_size=20'
                '&type=' + setting.PICTURE_TYPE +
                '&category=' + setting.PICTURE_CATEGORY +
                '&page_num=' + str(i),
                callback=self.picture_info,
                dont_filter=True
            )

    def picture_info(self, response, **kwargs):
        data = json.loads(response.text)
        for item in data["data"]["items"]:
            img = BiliItem()
            img["url"] = item["item"]["pictures"][-1]["img_src"]
            img["title"] = item["item"]["title"]
            img["id"] = item["item"]["doc_id"]
            img["author"] = item["user"]["name"]
            img["uid"] = item["user"]["uid"]
            img["extension"] = img["url"].split('.')[-1]
            yield img
            time.sleep(setting.PICTURE_SLEEP_TIME)
