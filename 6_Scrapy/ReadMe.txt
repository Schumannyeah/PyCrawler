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