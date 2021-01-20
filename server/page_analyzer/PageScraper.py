import requests
import re


# This class parses a page for reviews and returns a list of reviews for analysis
class PageScraper:

    # Get url and store in state for later use
    def __init__(self, url):
        self.url = url
        self.reviews = []
        self.headers = {
            'authority': 'www.amazon.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
    
    def get_reviews(self):
        link_to_reviews = self.open_product_link()
        raw_review_data = self.open_reviews_link(link_to_reviews)
        self.clean_raw_review_data(raw_review_data)
        print('Successfully fetched and cleaned {} reviews.'.format(len(self.reviews)))

    # This method opens the provided product link and extracts the reviews link
    def open_product_link(self):
        print('Going to product page...')
        review_link_reg = r'"see-all-reviews-link-foot.*a>'
        href_reg = r'href=".*"'
        page = requests.get(self.url, headers=self.headers)
        review_link_raw = re.search(review_link_reg, page.text).group()
        review_link_final = re.search(href_reg, review_link_raw).group()[6:-1]
        return review_link_final

    # This method opens the review
    def open_reviews_link(self, review_url):
        raw_review_data = []
        review_body_reg = r'<span data-hook="review-body" class="a-size-base review-text review-text-content">.*?/span>'
        page = requests.get('https://amazon.com' + review_url, headers=self.headers)
        raw_page_string = str(page.content)
        print('Scraping Review pages...')
        for i in range(1, 11):
            print(f'Pages scraped: {i}')
            raw_reviews = re.findall(review_body_reg, raw_page_string)
            for rev in raw_reviews:
                raw_review_data.append(rev)
            next_page_url = self.get_next_review_page(raw_page_string)
            page = requests.get('https://amazon.com' + next_page_url, headers=self.headers)
            raw_page_string = str(page.content)
        return raw_review_data

    def get_next_review_page(self, raw_page):
        next_review_page_reg = r'<li class="a-last".*?Next page'
        return re.search(next_review_page_reg, raw_page).group()[28:-11]

    def clean_raw_review_data(self, raw_review_data):
        reg = r'<span data-hook="review-body" class="a-size-base review-text review-text-content">|<span>|\\n|<br />|<br>|</span>|xe2|x80|x99dF|\\|&#34'
        for review in raw_review_data:
            res = re.sub(reg, '', review)
            self.reviews.append(res)
            

def main():

    page_scraper = PageScraper("https://www.amazon.com/Sennheiser-RS120-Wireless-Headphones-Charging/dp/B0001FTVEK/ref=sr_1_2_sspa?crid=1LU42U7ZS8LUD&dchild=1&keywords=headphones&qid=1611167687&sprefix=headpho%2Caps%2C201&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTDhQODhFTERJOEk5JmVuY3J5cHRlZElkPUEwMzk1MjY1MTdZU01KRU0zWk9UNyZlbmNyeXB0ZWRBZElkPUEwNDUyMzEzMVI0UEFISVc1Nk5LRSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
    page_scraper.get_reviews()


main()