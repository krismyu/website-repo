#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

########################
#### BASIC SETTINGS #### 
########################


AUTHOR = u'Kristine M. Yu'
SITENAME = u'Kristine M. Yu'
SITESUBTITLE = u'Linguist at UMass Amherst'
SITEURL = ''

PATH = 'content'
DELETE_OUTPUT_DIRECTORY = True

DEFAULT_DATE_FORMAT = '%Y %B %d'
DEFAULT_DATE = 'fs'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Set theme
THEME = '../themes/pelican-bootstrap3'

# Set bootstrap theme
BOOTSTRAP_THEME = 'cosmo'
#BOOTSTRAP_NAVBAR_INVERSE = 'TRUE'

#ABOUT_ME = 'Hi there.'
#AVATAR = './content/img/emmy-sophie-sideways.jpg'


## Set templates 

# List of templates that are used directly to render content. Typically direct templates are used to generate index pages for collections of content (e.g. tags and category index pages).

#DIRECT_TEMPLATES = ['blog', 'tag', 'archives']
#PAGINATED_DIRECT_TEMPLATES = ['blog']
#DEFAULT_PAGINATION = 5

# Tag cloud setup
#TAG_CLOUD_STEPS = 4 # Count of different font sizes in the tag cloud.
#TAG_CLOUD_MAX_ITEMS = 100 # Max number of tags in cloud

######################
#### URL SETTINGS #### 
######################

# http://simblestudios.com/blog/development/pages-as-pelican-top-level.html

# put articles (posts) in blog/
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

DISPLAY_ARTICLE_INFO_ON_INDEX = True


# we need to change the main index page now though...
INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = 'blog/'
#now move all the category and tag stuff to that blog/ dir as well
CATEGORY_URL = 'blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
CATEGORIES_URL = 'blog/category/'
CATEGORIES_SAVE_AS = 'blog/category/index.html'
TAG_URL = 'blog/tag/{slug}.html'    
TAG_SAVE_AS = 'blog/tag/{slug}.html'    
TAGS_URL = 'blog/tag/'  
TAGS_SAVE_AS = 'blog/tag/index.html'
YEAR_ARCHIVE_SAVE_AS = 'blog/archives/{date:%Y}/archive.html'
ARCHIVES_SAVE_AS = 'blog/archives/archives.html'
ARCHIVES_URL = 'blog/archives/archives.html'
AUTHOR_SAVE_AS = 'blog/{slug}.html'
AUTHORS_SAVE_AS = 'blog/authors.html'

# Article settings
#ARTICLE_URL = "blog/posts/{date:%Y}/{date:%m}/{slug}/"
#ARTICLE_SAVE_AS = "blog/posts/{date:%Y}/{date:%m}/{slug}/index.html"

# Page settings
# put pages in the root directory
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Author and category settings
#AUTHOR_URL = ''
#AUTHOR_SAVE_AS = False # Don't create author file
#CATEGORY_URL = ''
#CATEGORY_SAVE_AS = False # Don't create category file

# Archive settings
# YEAR_ARCHIVE_SAVE_AS = 'blog/posts/{date:%Y}/index.html'
# ARCHIVES_SAVE_AS = "archives/index.html"
NEWEST_FIRST_ARCHIVES = True

# Direct template settings
#BLOG_SAVE_AS =  'blog/index.html'
#TAG_SAVE_AS =  'tag/index.html'


###################################################
#### THEMING SETTINGS: NAVIGATION AND SIDEBARS #### 
###################################################

# Navigation bar
# MENUITEMS = [('About', '/home'),             
#              ('Research', '/research'),
#              ('Teaching', '/teaching'),
#              ('Code', '/code'),
#              ('Blog', '/blog')]
MENUITEMS = [('Research', '/research'),
             ('Teaching', '/teaching'),
             ('Code', '/code'),
             ('Blog', '/blog')]
DISPLAY_PAGES_ON_MENU = False
# Below: this got rid of Articles appearing on the nav bar
DISPLAY_CATEGORIES_ON_MENU = False

# Search box
SEARCH_BOX = True





# Ignores emac lock files
IGNORE_FILES =  (['.#*']) 

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Plugins

PLUGIN_PATHS=['../plugins/',]
PLUGINS = [
    'neighbors',
    'render_math'
#    'pelican_fontawesome',
#    'pelican_gist',
#    'render_math',
#    'sitemap',
    ]

#LATEX = 'article' # Only use LaTeX for selected articles

# Set static paths
# STATIC_PATHS = ["blog/img", "blog/data", "blog/videos", "pages/home", "pages/output", "pages/resources", "pages/teaching", "pages/masspros"]


# Adapted from https://github.com/tylerhartley/beneathdata/blob/master/pelicanconf.py
################## Add custom css #########################
CUSTOM_CSS = 'static/custom.css'
# Set static paths
STATIC_PATHS = ["img", "pages/home", "pages/pdfs", "extra",]

EXTRA_PATH_METADATA = {'extra/custom.css':{'path':'static/custom.css'},
                       'extra/href_scroll.js':{'path':'theme/js/href_scroll.js'},
                       'extra/CNAME': {'path': 'CNAME'},
                       'extra/jquery.zoom.js':{'path':'theme/js/jquery.zoom.js'},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)


### Twitter
TWITTER_USERNAME = 'linguist_krisyu'
TWITTER_WIDGET_ID = '716655349130989568'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

########################################
#### COMMENTING AND SITE STATISTICS #### 
########################################

DISQUS_SITENAME = 'krisyu'

PIWIK_URL = 'www.piwik.krisyu.org'
#PIWIK_SSL_URL = ''
PIWIK_SITE_ID = '2'
