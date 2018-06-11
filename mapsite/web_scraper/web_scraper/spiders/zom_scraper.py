# -*- coding: utf-8 -*-
import scrapy
from web_scraper.items import WebScraperItem


class ZomScraperSpider(scrapy.Spider):
    name = 'zom_scraper'
    allowed_domains = ['zomato.com']
    start_urls = ['http://zomato.com/bangalore/restaurants']

    def parse(self, response):
        cards = response.css('.search-card')
        items = []
        for card in cards:
            item = WebScraperItem()
            item['name'] = card.css('.fontsize0::text').extract_first().strip()
            item['url'] = card.css('.fontsize0::attr(href)').extract_first().strip()
            item['location'] = card.css('.ln22::text').extract_first().strip()
            item['rating'] = card.css('.rating-popup::text').extract_first().strip()
            items.append(item)

        return items     
