pip install Scrapy
and then
Before you start scraping, you will have to set up a new Scrapy project.
Enter a directory where you’d like to store your code and run:
scrapy startproject tutorial

This is giving you the structures as below:
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py

Details refers to https://docs.scrapy.org/en/latest/intro/tutorial.html

Main Steps:
First to compile the py module file like quotes_spider_default_two.py;

Then to run "scrapy crawl quotesDefaultTwo", the "quotesDefaultTwo" here comes from the defined name below:
class QuotesSpiderDefaultTwo(scrapy.Spider):
    name = "quotesDefaultTwo"
Be noted that the name as well as the class shall be unique and different from other names & classes
If running "scrapy crawl quotes", as defined in the py codes, it will generate 2 html files

Then the best way to learn how to extract data with Scrapy is trying selectors using the Scrapy shell.
scrapy shell "https://quotes.toscrape.com/page/1/"
then following functions could be run in cmd like
response.css("title")
[<Selector query='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]
response.css("title::text").getall()
['Quotes to Scrape']
response.css("title").getall()
['<title>Quotes to Scrape</title>']
response.css("title::text").get()
'Quotes to Scrape'
response.css("title::text")[0].get()
'Quotes to Scrape'
response.css("noelement")[0].get()
Traceback (most recent call last):
...
IndexError: list index out of range
Or using RegEx as bellow:
response.css("title::text").re(r"Quotes.*")
['Quotes to Scrape']
response.css("title::text").re(r"Q\w+")
['Quotes']
response.css("title::text").re(r"(\w+) to (\w+)")
['Quotes', 'Scrape']
Or Using XPath:
response.xpath("//title")
[<Selector query='//title' data='<title>Quotes to Scrape</title>'>]
response.xpath("//title/text()").get()
'Quotes to Scrape'
response.css("div.quote")
[<Selector query="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
<Selector query="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
...]
quote = response.css("div.quote")[0]
text = quote.css("span.text::text").get()
text
'“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'
author = quote.css("small.author::text").get()
author
'Albert Einstein'
tags = quote.css("div.tags a.tag::text").getall()
tags
['change', 'deep-thoughts', 'thinking', 'world']
for quote in response.css("div.quote"):
    text = quote.css("span.text::text").get()
    author = quote.css("small.author::text").get()
    tags = quote.css("div.tags a.tag::text").getall()
    print(dict(text=text, author=author, tags=tags))

{'text': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'author': 'Albert Einstein', 'tags': ['change', 'deep-thoughts', 'thinking', 'world']}
{'text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', 'author': 'J.K. Rowling', 'tags': ['abilities', 'choices']}
...

after running scrapy shell, you must use quit() first and you can re-run it.
quit()

Then to store the scraped data:
scrapy crawl quotes -O quotes.json
The -O command-line switch overwrites any existing file; use -o instead to append new content to any existing file.
However, appending to a JSON file makes the file contents invalid JSON.
When appending to a file, consider using a different serialization format, such as JSON Lines:

scrapy crawl quotes -o quotes.jsonl
The JSON Lines format is useful because it’s stream-like, you can easily append new records to it.

scrapy crawl quotes -o quotes-humor.json -a tag=humor
You can provide command line arguments to your spiders by using the -a option when running them:
These arguments are passed to the Spider’s __init__ method and become spider attributes by default.


Example:
As defined in "scrape_cssc_info.py", if we first run "scrapy crawl cssc-info-xpath -o cssc-company.json",
then run "load_json_into_db.py" to insert the company and website into sql database.

