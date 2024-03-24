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

class Buyer:
    buyer_id = 0

    def __init__(self, buyer_name) -> None:
        self.buyer_id = Buyer.buyer_id
        self.buyer_name = buyer_name
        Buyer.buyer_id += 1
        self.items_bid = set()

    def __str__(self) -> str:
        return f"Buyer ID: {self.buyer_id}, Buyer Name: {self.buyer_name}, Items Bid: {', '.join(str(item.item_number) for item in self.items_bid)}"

    def place_bid(self, item, amount):
        if amount > item.highest_bid:
            if amount >= item.reserve_price:
                item.highest_bid = amount
                item.bids_num += 1
                self.items_bid.add(item)
                print(f"{self.buyer_name} placed a bid of {amount} on {item.description}.")
            else:
                print(f"Sorry, {self.buyer_name}, your bid of {amount} on {item.description} is less than the reserve price of {item.reserve_price}.")
        else:
            print(f"Sorry, {self.buyer_name}, your bid of {amount} on {item.description} is not higher than the current highest bid of {item.highest_bid}.")

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

def main() -> None:
    auction = Auction()

    # Task 1 - Auction set up
    descriptions = ["Antique Vase", "Vintage Watch", "Rare Painting", "Diamond Necklace",
                    "Signed Baseball", "Classic Car", "Ancient Coin", "Limited Edition Print",
                    "Vintage Wine", "Rare Book"]
    
    reserve_prices = [500, 1000, 2000, 1500, 300, 5000, 100, 800, 200, 400]

    for desc, price in zip(descriptions, reserve_prices):
        item = Item(desc, price)
        auction.add_item(item)

    # Interactive Buyer Bidding
    num_buyers = int(input("Enter the number of buyers: "))
    buyers = []
    for i in range(num_buyers):
        buyer_name = input(f"Enter name for Buyer {i + 1}: ")
        buyers.append(Buyer(buyer_name))

        while True:
            print("\nAvailable Items for Bidding:")
            auction.display_items()
            print()

            while True:
                try:
                    item_number = int(input(f"{buyer_name}, enter the item number you want to bid on: "))
                    if not (0 <= item_number < len(auction.items)):
                        raise ValueError("Invalid item number.")
                    break
                except ValueError as e:
                    print(e)

            selected_item = auction.items[item_number]

            while True:
                try:
                    bid_amount = float(input(f"{buyer_name}, enter your bid for '{selected_item.description}': "))
                    if bid_amount <= 0:
                        raise ValueError("Bid amount must be greater than 0.")
                    break
                except ValueError as e:
                    print(e)

            buyers[-1].place_bid(selected_item, bid_amount)

            another_bid = input(f"\n{buyer_name}, do you want to bid on another item? (yes/no): ").lower()
            if another_bid != 'yes':
                break

    # Task 3 - End of Auction
    auction.end_auction()

    # Additional Testing
    print("\nDisplaying Items:")
    auction.display_items()

    print("\nBuyers Information:")
    for buyer in buyers:
        print(buyer)


if __name__ == "__main__":
    main()
