class Ticket:
    id = 0
    num_days = 0
    ticket_prices = {
        "adult": {1: 20.00, 2: 30.00},
        "child": {1: 12.00, 2: 18.00},
        "senior": {1: 16.00, 2: 24.00},
        "family": {1: 60.00, 2: 90.00},
        "group": {1: 15.00, 2: 22.50}
    }

    extra_attractions = {
        "lion feeding": 2.50,
        "penguin feeding": 2.00,
        "evening barbecue": 5.00
    }

    def __init__(self, id, group, extra) -> None:
        self.id = id
        self.group = group
        self.extra_attractions = extra
        self.calculate_cost()        

    @staticmethod
    def ticket_options(self) -> None:
        choice = int(choice)
        for type,cost in self.ticket_prices.items():
            print(f"Cost for one {type} is 
                  ${cost[1]} for one ticket and ${cost[2]} for two tickets")
        print("\nExtra attractions and prices:")
        for attraction, price in self.extra_attractions.items():
            print(f"{attraction}: ${price}") 

    def calculate_cost(self) -> None:
        self.cost = 0
        self.cost = self.ticket_prices[self.group][self.num_days]
        if self.extra_attractions:
            for attraction in self.extra_attractions:
                self.cost += self.extra_attractions[attraction]

    def display(self) -> None:
        print(f"Ticket ID: {self.id}")
        print(f"Group: {self.group}")
        print(f"Extra attractions: 
              {', '.join(self.extra_attractions) if isinstance(self.extra_attractions, list) else self.extra_attractions}")
        print(f"Cost: ${self.cost}")


class Bookings():

    def __init__(self, num_people = 0) -> None:
        Bookings.bookings_num = 0
        self.bookings = [] 
        self.num_people = num_people
    
    def book(self) -> None:
        Bookings.bookings += 1
        Ticket.ticket_options()
        days = int(input("For how many days do you  want to book a ticket? (1/2)"))
        group = input("Which group are you a part of?").lower()
        choice = True if (input("Do you want extra attractions? (y/n)").lower() == "y") else False
        if choice:
            attractions = input("Which attractions do you want to add?").split(",").strip()
        else:
            attractions = None
        self.bookings.append(Ticket(Bookings.bookings, group, attractions))

    def check_best_value(self) -> None:
        for booking in self.bookings:
            print(f"\nBooking ID: {booking.id}")
            print(f"Current Cost: ${booking.cost}")
            
            alternatives = []
            group_cost = Ticket.ticket_prices["group"][booking.num_days]
            alternatives.append(("Group Ticket", group_cost))

            if booking.group == "group":
                num_people = len(booking.extra_attractions) + 1  # Include the person booking
                num_families_needed = num_people // 5
                if num_people % 5 != 0:
                    num_families_needed += 1
                family_cost = Ticket.ticket_prices["family"][booking.num_days] * num_families_needed
                alternatives.append(("Family Tickets", family_cost))

            best_alternative, best_cost = min(alternatives, key=lambda x: x[1])

            if best_cost < booking.cost:
                print(f"Better Option: {best_alternative} for ${best_cost}")
            else:
                print("Current Cost is the Best Value!")

    def display_bookings(self) -> None:
        print("All bookings and their details:")
        for booking in self.bookings:
            booking.display()
            print()

def main():
    bookings = Bookings()

    while True:
        print("\nWelcome to the Wildlife Park Ticket Booking System!")
        print("1. Display Ticket Options and Attractions")
        print("2. Book a Ticket")
        print("3. Check Best Value for Bookings")
        print("4. Display All Bookings")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            Ticket.ticket_options()
        elif choice == "2":
            bookings.book()
        elif choice == "3":
            bookings.check_best_value()
        elif choice == "4":
            bookings.display_bookings()
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()