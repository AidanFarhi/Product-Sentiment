#from ReviewScraper import ReviewScraper
import re

test_urls = [
    'https://www.amazon.com/ExcelSteel-Stainless-Steel-Colanders-Set/dp/B00FEDLBII/ref=cm_cr_arp_d_product_top?ie=UTF8&th=1',
    'https://www.amazon.com/Headphones-Microphone-Lightweight-Comfortable-Foldable/dp/B07J5X68B2/ref=sr_1_1_sspa?crid=1LU42U7ZS8LUD&dchild=1&keywords=headphones&qid=1611168382&sprefix=headpho%2Caps%2C201&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUDBIUzdZRURKUEdBJmVuY3J5cHRlZElkPUEwNDgwODk0TjlOM0lFMEZHVUE2JmVuY3J5cHRlZEFkSWQ9QTAyNDEzMzgyRlYwNDIzMk5aVTNMJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==',
    'https://www.amazon.com/produce-aisle-Cantaloupe-One-Medium/dp/B000NSGULC?ref=US_TRF_DSK_UFG_RTL_ONSIT_0425559&fpw=fresh&pf_rd_r=DM5MK0RMDAHW6WNC5ZE7&pf_rd_p=a2fbb221-3d31-4621-bc2b-527067383c0e&pd_rd_r=a5320fa6-3922-4bd0-b37e-a246075cb449&pd_rd_w=Ur09B&pd_rd_wg=SedKi&ref_=pd_gw_unk',
    'https://www.amazon.com/dp/B00LXWGWNI/ref=s9_acsd_al_bw_c2_x_3_t?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-14&pf_rd_r=PQ9FBQYMCK1WWFAYRHAX&pf_rd_t=101&pf_rd_p=50ea4b60-758f-466c-a69c-7c069294dd24&pf_rd_i=165793011'
]

class Analyzer:
    
    # reviews will be an array of review strings to be analyzed
    def __init__(self, reviews):
        self.reviews = reviews
        # maintain a count of positive words found in reviews
        self.positive_phrases = {
            'really like': 0,
            'happy with this purchase': 0,
            'happy with purchase': 0,
            'love it': 0,
            'love them': 0,
            'love this': 0,
            'good quality': 0,
            'great quality': 0,
            'glad I bought': 0,
            'look great': 0,
            'look good': 0,
            'work perfectly': 0,
            'work great': 0,
            'work well': 0,
            'glad I made': 0,
            'good value': 0,
            'great value': 0,
            'sturdy': 0,
            'well made': 0,
            'good price': 0,
            'great price': 0,
            'excellent price': 0,
            'perfect': 0,
            'beautiful': 0,
            'easy to use': 0,
            'highly recommend': 0,
            'would recommend': 0,
            'great for the price': 0,
            'good for price': 0,
            'would highly recommend': 0,
            'best tasting': 0,
            'good size': 0,
            'arrived fresh': 0,
            'was fresh': 0,
            'were perfect': 0,
            'was perfect': 0,
            'was awesome': 0,
            'were awesome': 0,
            'is tasty': 0,
            'very tasty': 0,
            'was tasty': 0,
            'tasted great': 0,
            'best tasting': 0,
            'tasted amazing': 0,
            'decent flavor': 0,
            'good flavor': 0,
            'great flavor': 0,
            'amazing flavor': 0,
            'perfect condition': 0,
            'great condition': 0,
            'good condition': 0,
            'was delicious': 0,
            'is delicious': 0,
        }
        self.total_positive_hits = 0
        # maintain a count of negagive words found in reviews
        self.negative_phrases = {
            'try another brand': 0,
            'returned': 0,
            'wouldn’t buy again': 0,
            'would not recommend': 0,
            'don’t buy': 0,
            'bad purchase': 0,
            'don\'t waste your time': 0,
            'don\'t waste your money': 0,
            'don\'t be fooled': 0,
            'dissatisfied': 0,
            'low quality': 0,
            'not satisfied': 0,
            'poorly designed': 0,
            'cheaply built': 0,
            'cheaply made': 0,
            'poor quality': 0,
            'not made well': 0,
            'waste of cash': 0,
            'waste of money': 0,
            'won\'t by again': 0,
            'not worth the money': 0,
            'disappointing purchase': 0,
            'Junk': 0,
            'not happy': 0,
            'not a good choice': 0,
            'returning': 0,
            'will return': 0,
            'annoying': 0,
            'not high quality': 0,
            'not sturdy': 0,
            'not reliable': 0,
            'unreliable': 0,
            'rotten': 0,
            'very disappointed': 0,
            'was spoilt': 0,
            'was spoiled': 0,
            'bad smell': 0,
            'molds': 0,
            'moldy': 0,
            'wasn\'t fresh': 0,
            'tasted horrible': 0,
            'tasted bad': 0,
            'tasted off': 0,
            'tasted rotten': 0,
            'was disappointed': 0,
            'am disappointed': 0,
            'mold': 0,
            'inedible': 0,
        }
        self.total_negative_hits = 0
        self.score = 0

    def get_counts(self, reviews):
        for review in reviews:
            review = review.lower()
            for key in self.positive_phrases.keys():
                reg = r'{key}'.format(key=key)
                if re.search(reg, review) is not None:
                    self.positive_phrases[key] += 1
                    self.total_positive_hits += 1
            for key in self.negative_phrases.keys():
                reg = r'{key}'.format(key=key)
                if re.search(reg, review) is not None:
                    self.negative_phrases[key] += 1
                    self.total_negative_hits += 1
    
    def show_results(self):
        print(self.positive_phrases)
        print(self.negative_phrases)
        print("Positive Hits:", self.total_positive_hits)
        print("Negative Hits:", self.total_negative_hits)

    def calc_score(self):
        total_hits = self.total_positive_hits + self.total_negative_hits
        score = (self.total_positive_hits / total_hits) * 100
        self.score = score

    def analyze_reviews(self):
        self.get_counts(self.reviews)
        self.calc_score()
        self.show_results()
        return True


# def main():
#     review_scraper = ReviewScraper(test_urls[3])
#     reviews = review_scraper.get_reviews()
#     print(len(reviews))
#     p_analyzer = Analyzer(reviews)
#     p_analyzer.analyze_reviews()


# main()