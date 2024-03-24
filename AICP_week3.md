# AICP Week 3

## Understanding situation

- recording of mil prod of cow herd
- 3 id code for cow
- cow is milked twice daily
- volume of milk is measured upto 1 decimal accuracy
- total and avg yield is calculated weekly for each cow
- identification of cow that produces : max milks ; less than 12 litres on at least 4 days per week

## Understanding Tasks

1. record weekly milk yields
2. display calculated stuff
3. display indetified cows

## Any Extra Stuff u wanna add to complete program?

`Item` Class:

- The `Item` class represents an item up for auction.

- **Attributes:

 - `item_id`: A class variable to keep track of the unique ID for each item.

 - `item_number`: An instance variable to store the item's unique number.

 - `bids_num`: An instance variable to track the number of bids placed on the item.

 - `description`: A description of the item.

 - `reserve_price`: The minimum price at which the item can be sold.

 - `highest_bid`: The highest bid placed on the item.

- **Methods**:

 - `__init__()`: Initializes the item with a description and reserve price. Assigns a unique `item_number` to the item.

 - `__str__()`: Returns a string representation of the item with its details.



`Buyer` Class:

- The `Buyer` class represents a bidder in the auction.

- Attributes:

 - `buyer_id`: A class variable to keep track of the unique ID for each buyer.

 - `buyer_name`: The name of the buyer.

 - `items_bid`: A set to store the items on which the buyer has placed bids.

- **Methods**:

 - `__init__()`: Initializes the buyer with a name and an empty set of items bid.

 - `__str__()`: Returns a string representation of the buyer with their details.

 - `place_bid(item, amount)`: Places a bid on a specified item with a given amount. Checks if the bid is valid.



#### `Auction` Class:

- The `Auction` class manages the auction process.

- **Attributes**:

 - `items`: A list to store the items available for auction.

- **Methods**:

 - `__init__()`: Initializes the auction with an empty list of items.

 - `add_item(item)`: Adds an item to the list of items available for auction.

 - `display_items()`: Displays all items available for bidding.

 - `end_auction()`: Ends the auction, displays results, calculates fees, and marks items as sold or unsold.



#### `main()` Function:

- The `main()` function is the entry point of the program.

- **Task 1 - Auction Setup**:

 - Initializes the auction with a set of predefined items and their reserve prices.

- **Interactive Buyer Bidding**:

 - Takes input for the number of buyers participating.

 - Allows each buyer to place bids on items interactively.

 - Displays available items for bidding and asks for item numbers and bid amounts.

 - Checks if the bid amount is valid and updates the highest bid for the item.

- **Task 3 - End of Auction**:

 - Ends the auction, displays results, including items sold, unsold, and those with no bids.

 - Calculates the total fee earned from sold items.



#### Changes Made:

1. Added `item_number` to each `Item` instance for easier identification.

2. Updated `place_bid()` method in the `Buyer` class to handle bid placement, checking against reserve prices and current highest bids.

3. Improved `end_auction()` method in the `Auction` class to display detailed results and calculate total fees.

4. Implemented a more interactive `main()` function for setting up the auction, allowing bidding, and ending the auction.

