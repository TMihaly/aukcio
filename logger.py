import csv
import os
import asyncio

# greedszint konstans:
greedValueConst = 0.01

async def log_to_csv(filename, row):
    # CSV-hez
    file_exists = os.path.isfile(filename)
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
             #column név
            writer.writerow(["timestamp", "event_type", "client_id", "money", "greed", "pride", "current_price", "bid"])
        writer.writerow(row)

async def update_greed(client, auction_length, csv_file):
    # aukció greedszint változtatáshoz
    while auction_length:
        client.greed = min(client.greed + greedValueConst, 1.0) # 5. sor a konstanshoz, ki kell cserélni majd ezt is randomizáltra
        await log_to_csv(csv_file, [auction_length, "greed_update", client.client_id, client.money, client.greed, client.pride, None, None])
        await asyncio.sleep(1)
        auction_length -= 1
