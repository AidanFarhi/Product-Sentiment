from ReviewScraper import ReviewScraper


class Analyzer:
    
    # reviews will be an array of review strings to be analyzed
    def __init__(self, reviews):
        self.reviews = reviews
        # maintain a count of positive words found in reviews
        self.positive_phrases = {
            "best": 0,
            "love": 0,
            "happy": 0,
            "great": 0,
            "high-quality": 0,
            "excellent": 0,
        }
        self.total_positive_hits = 0
        # maintain a count of negagive words found in reviews
        self.negative_phrases = {
            "hate": 0,
            "disappointed": 0,
            "poor": 0,
            "bad": 0,
            "dislike": 0
        }
        self.total_negative_hits = 0

    def get_counts(self, reviews):
        for review in reviews:
            review = review.split(' ')
            for word in review:
                word = word.lower()
                if word in self.positive_phrases:
                    self.positive_phrases[word] += 1
                    self.total_positive_hits += 1
                if word in self.negative_phrases:
                    self.negative_phrases[word] += 1
                    self.total_negative_hits += 1
    
    def show_results(self):
        print(self.positive_phrases)
        print(self.negative_phrases)
        print("Positive Hits:", self.total_positive_hits)
        print("Negative Hits:", self.total_negative_hits)

    def analyze_reviews(self):
        self.get_counts(self.reviews)
        self.show_results()


def main():
    review_scraper = ReviewScraper()
    reviews = review_scraper.get_reviews()
    print(len(reviews))
    p_analyzer = Analyzer(reviews)
    p_analyzer.analyze_reviews()


main()