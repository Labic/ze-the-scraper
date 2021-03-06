# -*- coding: utf-8 -*-
from . import ZeSpider


class ExameSpider(ZeSpider):

    name = 'exame'
    allowed_domains = ['exame.abril.com.br']
    items_refs = [{
        "item": "ze.items.creativework.ArticleItem",
        "fields": { 
            "name": {
                "selectors": {
                    "css": [
                        "meta[property='og:title']::attr(content)",
                        "meta[name=title]::attr(content)",
                        "[itemprop=name]::text", 
                        ".content-head__title::text" 
                    ]
                }
            },
            "image": {
                "selectors": {
                    "css": [
                        'meta[property="og:image"]::attr(content)',
                        "[itemprop=image]::attr(content)", 
                        "[property='og:image']::attr(content)" 
                    ]
                }
            }, 
            "description": {
                "selectors": {
                    "css": [
                        "meta[property='og:description']::attr(content)",
                        "meta[name=description]::attr(content)",
                        "[itemprop=description]::text", 
                        "[itemprop=alternativeHeadline]::text", 
                        ".content-head__subtitle::text" 
                    ]
                }
            }, 
            "author": {
                "selectors": {
                    "css": [
                        "[itemprop=author]::text", 
                        "[itemprop=creator]::text",
                        ".article-author span::text"
                    ]
                }
            }, 
            "datePublished": {
                "selectors": {
                    "css": [
                        "[itemprop=datePublished]::attr(datetime)", 
                        "[itemprop=datePublished]::text", 
                        "meta[property='bt:pubDate']::attr(content)",
                        # head > meta:nth-child(44)
                    ]
                }
            }, 
            "dateModified": {
                "selectors": {
                    "css": [
                        "[itemprop=dateModified]::attr(datetime)" , 
                        "[itemprop=dateModified]::text", 
                        "meta[name='article:modified_time']::attr(content)",
                        "updated::text",
                    ]
                }
            }, 
            "articleBody": {
                "selectors": {
                    "css": [
                        "[itemprop=articleBody]",
                        ".mc-body",
                        ".materia-conteudo",
                        ".entry-content",
                        ".conteudo",
                        ".article-content"
                    ]
                }
            }, 
            "keywords": {
                "selectors": {
                    "css": [
                        "meta[name=keywords]::attr(content)",
                        "[itemprop=keywords]::text", 
                        ".entities__list-itemLink::text"
                    ]
                }
            }
        }
    }]
