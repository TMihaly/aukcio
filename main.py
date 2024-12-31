import os
import asyncio
from logger import log_to_csv, update_greed
from auction import auction_timer
from client import Client

async def main():
    csv_file = "auction_log.csv"

    # előző csv törlése, élesnél ki kell venni
    if os.path.exists(csv_file):
        os.remove(csv_file)

    clients = [
        Client(client_id=1, money=100, greed=0.5, pride=0.3),
        Client(client_id=2, money=150, greed=0.4, pride=0.5),
        Client(client_id=3, money=80, greed=0.6, pride=0.2),
    ]

    auction_length = 20

    greed_tasks = [update_greed(client, auction_length, csv_file) for client in clients]
    await asyncio.gather(auction_timer(clients, auction_length, csv_file), *greed_tasks)

# Futtatás
if __name__ == "__main__":
    asyncio.run(main())
