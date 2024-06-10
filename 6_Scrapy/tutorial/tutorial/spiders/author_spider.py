import scrapy


class AuthorSpider(scrapy.Spider):
    name = "author"

    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        # find all links that comes immediately after the elements with the
        # class "author"
        author_page_links = response.css(".author + a")
        # follow these links to call parse_author method to further process
        # the author's page
        yield from response.follow_all(author_page_links, self.parse_author)

        # select the all the links after the li element with class next
        pagination_links = response.css("li.next a")
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            # It uses CSS selectors to extract text from the HTML response,
            # with a default empty string return if no match is found.
            return response.css(query).get(default="").strip()

        yield {
            "name": extract_with_css("h3.author-title::text"),
            "birthdate": extract_with_css(".author-born-date::text"),
            "bio": extract_with_css(".author-description::text"),
        }