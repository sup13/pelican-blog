#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Supriti'
SITENAME = u'MyFirstBlog'
SITEURL = 'https://testblog.com'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DISPLAY_PAGES_ON_MENU= False
DEFAULT_LANG = u'en'

#THEME = 'pelican-themes/blueidea/'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('Instagram', 'https://www.instagram.com/supritichourasia/?hl=en'),
	 ('LinkedIn', 'https://www.linkedin.com/in/supriti-chourasia-766245106/'),
         ('Facebook', 'https://www.facebook.com/supriti.chourasia'),
         ('GitHub', 'https://github.com/sup13'),
        )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
 #         ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
