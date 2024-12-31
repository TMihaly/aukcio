import random

class Client:
    def __init__(self, client_id, money, greed, pride):
        self.client_id = client_id
        self.money = money
        self.greed = greed
        self.pride = pride

    def place_bid(self, current_price): #greed benne van a generálásban

        if self.money > current_price and random.random() < self.greed:
            # alapnövelő
            bid_increase = current_price + random.randint(1, 10)
            # greed szintje alapján szorzó
            bid = current_price + bid_increase + int(bid_increase*self.greed)
            return bid
        return None
