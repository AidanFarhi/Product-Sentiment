import asyncio
import requests
import aiohttp
import re
import time

url = 'https://www.amazon.com/Headphones-Microphone-Lightweight-Comfortable-Foldable/dp/B07J5X68B2/ref=sr_1_1_sspa?crid=1LU42U7ZS8LUD&dchild=1&keywords=headphones&qid=1611168382&sprefix=headpho%2Caps%2C201&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUDBIUzdZRURKUEdBJmVuY3J5cHRlZElkPUEwNDgwODk0TjlOM0lFMEZHVUE2JmVuY3J5cHRlZEFkSWQ9QTAyNDEzMzgyRlYwNDIzMk5aVTNMJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
headers = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}
reviews = []
pages = 0

def open_product_link(url):
    review_link_reg = r'"see-all-reviews-link-foot.*a>'
    href_reg = r'href=".*"'
    page = requests.get(url, headers=headers)
    review_link_raw = re.search(review_link_reg, page.text).group()
    see_all_reviews_link = re.search(href_reg, review_link_raw).group()[6:-1]
    return see_all_reviews_link

def open_see_all_reviews_link(see_all_reviews_link):  
    page = requests.get('https://amazon.com' + see_all_reviews_link, headers=headers)
    raw_all_reviews_page_string = str(page.content)
    first_page_raw_reviews = get_raw_reviews_from_page(raw_all_reviews_page_string)
    clean_raw_review_data(first_page_raw_reviews)
    return raw_all_reviews_page_string

# This method extracts the link to the 'Next page' of reviews
def get_original_next_review_page(raw_page):
    next_review_page_reg = r'<li class="a-last".*?Next page'
    return re.search(next_review_page_reg, raw_page).group()[28:-11]

def get_raw_reviews_from_page(raw_review_page_string):
    raw_reviews_arr = []
    review_body_reg = r'<span data-hook="review-body" class="a-size-base review-text review-text-content">.*?/span>'
    raw_reviews = re.findall(review_body_reg, raw_review_page_string)
    for rev in raw_reviews:
        raw_reviews_arr.append(rev)
    return raw_reviews_arr

def get_next_ten_pages(original_next_page_link):
    start_index = str.find(original_next_page_link, 'Number=')
    replace_index = start_index + 7
    ten_page_links = []
    for i in range (2, 16):
        new_link = original_next_page_link[:replace_index] + str(i) + original_next_page_link[replace_index + 1:]
        ten_page_links.append('https://amazon.com' + new_link)
    return ten_page_links

async def get_cleaned_review_from_link(session, link):
    async with session.get(link) as response:
        html = await response.read()
        raw_reviews = get_raw_reviews_from_page(str(html))
        clean_raw_review_data(raw_reviews)

async def send_out_async_requests(ten_page_links):
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = []
        for link in ten_page_links:
            task = asyncio.ensure_future(get_cleaned_review_from_link(session, link))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


# This method cleans the raw review data and stores all the cleaned reviews in self.reviews in state
def clean_raw_review_data(raw_reviews):
    reg = r'<span data-hook="review-body" class="a-size-base review-text review-text-content">|<span>|\\n|<br />|<br>|</span>|xe2|x80|x99dF|\\|&#34'
    for review in raw_reviews:
        res = re.sub(reg, '', review)
        reviews.append(res)

def driver_function():
    print('Opening product page...')
    link_to_all_reviews = open_product_link(url)
    print('Going to review page...')
    raw_all_reviews_page = open_see_all_reviews_link(link_to_all_reviews)
    original_next_review_page_link = get_original_next_review_page(raw_all_reviews_page)
    print('Generating links...')
    ten_page_links = get_next_ten_pages(original_next_review_page_link)
    print('Extracting reviews...')
    asyncio.get_event_loop().run_until_complete(send_out_async_requests(ten_page_links))

def main():
    start = time.time()
    driver_function()
    print(f'Reviews extracted: {len(reviews)}')
    print(f'Time taken: {time.time() - start} seconds')


main()