import asyncio
from logger import log_to_csv

async def auction_timer(clients, auction_length, csv_file):
    #árváltoztatáshoz
    current_price = 50
    bids = []

# KÖRÖNKÉNTI LOG
    while auction_length:
        for client in clients:
            bid = client.place_bid(current_price)
            if bid:
                bids.append((client.client_id, bid))
                await log_to_csv(csv_file, [auction_length, "bid", client.client_id, client.money, client.greed, client.pride, current_price, bid])

        if bids:
            _, highest_bid = max(bids, key=lambda x: x[1])
            current_price = highest_bid

        await asyncio.sleep(1)
        auction_length -= 1

# VÉGEREDMÉNY
    if bids:
        winner = max(bids, key=lambda x: x[1])
        await log_to_csv(csv_file, [0, "auction_end", winner[0], None, None, None, current_price, winner[1]])
    else:
        await log_to_csv(csv_file, [0, "auction_end", None, None, None, None, current_price, None])
