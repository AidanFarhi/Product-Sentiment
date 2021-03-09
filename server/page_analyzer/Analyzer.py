import re

class Analyzer:
    
    # reviews will be an array of review strings to be analyzed
    def __init__(self, reviews):
        self.reviews = reviews
        # maintain a count of positive words found in reviews
        self.positive_phrases = {
            'really like': 0,
            'happy with this purchase': 0,
            'happy with the purchase': 0,
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
            'looks great': 0,
            'looks good': 0,
            'works perfectly': 0,
            'works great': 0,
            'works well': 0,
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
            'excellent book': 0,
            'great read': 0,
            'excellent read': 0,
            'beyond my expectations': 0,
            'exceeded my expectations': 0,
            'nicer than anticipated': 0,
            'better than anticipated': 0,
            'loves it': 0,
            'nicely made': 0,
            'amazing device': 0,
            'amazing product': 0,
            'amazing purchase': 0,
            'amazing item': 0,
            'great device': 0,
            'great product': 0,
            'great purchase': 0,
            'great item': 0,
            'excellent device': 0,
            'excellent product': 0,
            'excellent purchase': 0,
            'excellent item': 0,
            'well built': 0,
            'is in love with this': 0,
            'is in love with these': 0,
            'are in love with this': 0,
            'are in love with these': 0
        }
        self.total_positive_hits = 0
        # maintain a count of negagive words found in reviews
        self.negative_phrases = {
            'try another brand': 0,
            'wouldn’t buy again': 0,
            'would not buy again': 0,
            'would not recommend': 0,
            'don’t buy': 0,
            'bad purchase': 0,
            'don\'t waste your time': 0,
            'don\'t waste your money': 0,
            'don\'t be fooled': 0,
            'very dissatisfied': 0,
            'am dissatisfied': 0,
            'was dissatisfied': 0,
            'low quality': 0,
            'not satisfied': 0,
            'poorly designed': 0,
            'cheaply built': 0,
            'cheaply made': 0,
            'badly made': 0,
            'poorly made': 0,
            'poor quality': 0,
            'not made well': 0,
            'waste of cash': 0,
            'waste of money': 0,
            'won\'t by again': 0,
            'not worth the money': 0,
            'disappointing purchase': 0,
            'piece of junk': 0,
            'piece of crap': 0,
            'not happy': 0,
            'not a good choice': 0,
            'was a bad choice': 0,
            'will be returning': 0,
            'will return': 0,
            'will definetly return': 0,
            'will definetly be returning': 0,
            'annoying': 0,
            'not high quality': 0,
            'not sturdy': 0,
            'not reliable': 0,
            'is unreliable': 0,
            'was unreliable': 0,
            'are unreliable': 0,
            'was rotten': 0,
            'very disappointed': 0,
            'highly disappointed': 0,
            'extremely disappointed': 0,
            'so disappointed': 0,
            'was spoilt': 0,
            'was spoiled': 0,
            'bad smell': 0,
            'wasn\'t fresh': 0,
            'tasted horrible': 0,
            'tasted bad': 0,
            'tasted off': 0,
            'tasted rotten': 0,
            'was disappointed': 0,
            'am disappointed': 0,
            'has mold': 0,
            'had mold': 0,
            'is moldy': 0,
            'was moldy': 0,
            'inedible': 0,
            'intend to replace': 0,
            'going to return': 0,
            'plan on returning': 0,
            'i wish it can be more durable': 0,
            'i wish it was more durable': 0,
            'false advertizing': 0,
            'was faulty': 0,
            'is faulty': 0,
            'not durable': 0,
            'is flimsy': 0,
            'was flimsy': 0,
            'chipped easily': 0,
            'did not withstand': 0,
            'strong chemical smell': 0,
            'strong chemical odor': 0,
            'strong paint smell': 0,
            'bad chemical smell': 0,
            'bad paint smell': 0,
            'strong paint odor': 0,
            'bad chemical odor': 0,
            'bad paint odor': 0,
            'paint comes off': 0,
            'paint chips': 0,
            'paint came off': 0,
            'paint chipped': 0,
            'put splinter': 0,
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

    def calc_score(self):
        total_hits = self.total_positive_hits + self.total_negative_hits
        if total_hits == 0:  # set result to -1 if no results obtained
            self.score = -1
        else:
            score = (self.total_positive_hits / total_hits) * 100
            self.score = round(score, 2)

    def analyze_reviews(self):
        self.get_counts(self.reviews)
        self.calc_score()
        return True
