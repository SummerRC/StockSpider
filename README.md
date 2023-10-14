# README
纯 Scrapy 爬虫项目代码，用于快速开发并生成 egg 文件，以便于快速在服务器的 ScrapydWeb 网站部署爬虫。

之前的项目 [KPLSpider](https://github.com/SummerRC/KPLSpider) 整合了 Scrapy 爬虫项目的代码、scrapyd、scrapydweb 三者的内容和配置，并配置好了 Dockerfile 文件，可利用 docker 快速打包部署到远程云服务器。

特别注意，以下几个包含密码的配置文件不允许提交到代码仓库：
- 1、config.ini 包含了数据库地址、用户名、密码等项目相关的敏感信息
- 2、scrapy.cfg spider deploy时的敏感信息

## 本项目常用命令

- 1、生成 egg 文件但不上传：``` scrapyd-deploy --build-egg egg_name.egg```
- 2、上传指定 egg 文件到指定服务器：``` scrapyd-deploy -v version -L TARGET --egg egg_name.egg```