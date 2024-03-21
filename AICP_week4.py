class Item:
    item_id = 0

    def __init__(self, description, reserve_price) -> None:
        self.item_number = Item.item_id
        Item.item_id += 1
        self.bids_num = 0
        self.description = description
        self.reserve_price = reserve_price
        self.highest_bid = 0

    def __str__(self) -> str:
        return f"Item Number: {self.item_number}, Description: {self.description}, Reserve Price: {self.reserve_price}, Number of Bids: {self.bids_num}, Highest Bid: {self.highest_bid}"

class Buyer :
    buyer_id = 0
    
    def __init__(self, buyer_name) -> None:
        self.buyer_id = Buyer.buyer_id
        self.buyer_name = buyer_name
        Buyer.buyer_id += 1
        # CHECK
        self.items_bid = set()
    
    def __str__(self) -> str:
        return f"Buyer ID: {self.buyer_id}, Buyer Name: {self.buyer_name}, Items Bid: {', '.join(str(item.item_number) for item in self.items_bid)}"

class Auction:
    def __init__(self) -> None:
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        for item in self.items:
            print(item)

    def end_auction(self):
        total_fee = 0
        items_sold = 0
        items_not_sold = 0
        items_no_bids = 0

        print("\nResults of the Auction:\n")

        for item in self.items:
            if item.bids_num > 0:
                if item.highest_bid >= item.reserve_price:
                    total_fee += 0.1 * item.highest_bid
                    items_sold += 1
                    print(f"Item {item.item_number} sold for {item.highest_bid} with reserve price met.")
                else:
                    items_not_sold += 1
                    print(f"Item {item.item_number} did not meet reserve price.")
            else:
                items_no_bids += 1
                print(f"Item {item.item_number} received no bids.")

        print(f"\nTotal Fee from Sold Items: {total_fee}")
        print(f"Number of Items Sold: {items_sold}")
        print(f"Number of Items Not Sold: {items_not_sold}")
        print(f"Number of Items with No Bids: {items_no_bids}")


# Test the Auction System
if __name__ == "__main__":
    auction = Auction()

    # Task 1 - Auction set up
    descriptions = ["Antique Vase", "Vintage Watch", "Rare Painting", "Diamond Necklace",
                    "Signed Baseball", "Classic Car", "Ancient Coin", "Limited Edition Print",
                    "Vintage Wine", "Rare Book"]
    reserve_prices = [500, 1000, 2000, 1500, 300, 5000, 100, 800, 200, 400]

    for desc, price in zip(descriptions, reserve_prices):
        item = Item(desc, price)
        auction.add_item(item)

    # Task 2 - Buyer bids
    buyer1 = Buyer("Alice")
    buyer2 = Buyer("Bob")
    buyer3 = Buyer("Charlie")

    buyer1.place_bid(auction.items[0], 600)
    buyer2.place_bid(auction.items[0], 700)
    buyer3.place_bid(auction.items[0], 750)

    buyer1.place_bid(auction.items[1], 1100)
    buyer2.place_bid(auction.items[1], 1200)

    buyer1.place_bid(auction.items[4], 400)
    buyer2.place_bid(auction.items[4], 450)

    # Task 3 - End of Auction
    auction.end_auction()

    # Additional Testing
    print("\nDisplaying Items:")
    auction.display_items()

    print("\nBuyers Information:")
    print(buyer1)
    print(buyer2)
    print(buyer3)
