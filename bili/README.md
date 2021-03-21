# 哔哩哔哩爬虫

想要自定义请先Fork（派生）该项目

目前已完成：

* 哔哩哔哩相簿爬虫

  使用方法：
  
  ```shell
  # 项目根目录下
  scrapy crawl picture
  # 图片将保存到image文件夹下
  ```
  
  可以在根目录下的 `setting.py` 设置：
    
  * `PICTURE_MAX_PAGE`
    
    爬的页数，每页20个
  
  * `PICTURE_SELLP_TIME`
    
    每爬一张图间隔的时间
  
  * `PICTURE_CATEGORY`
      
    要爬的图片的类型，选项如下
  
    * `all`：所有类型
    
    * `illustration`：插画
  
    * `comic`：漫画
  
    * `draw`：其他
  
  * `PICTURE_TYPE`
  
    排名规则。选项如下：
  
    * `hot`：按热度排序
  
    * `new`：按时间排序