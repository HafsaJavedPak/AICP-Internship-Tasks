from __future__ import annotations
from typing import Type



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

    def __init__(self, id, group, extra, num_days) -> None:
        self.id = id
        self.group = group
        self.per_attractions = extra
        self.num_days = num_days
        self.calculate_cost()        
    
    @staticmethod
    def ticket_options() -> None:
        for type, cost in Ticket.ticket_prices.items():
            print(f"Cost for one {type} is ${cost[1]} for one ticket and ${cost[2]} for two tickets")
        print("\nExtra attractions and prices:")
        for attraction, price in Ticket.extra_attractions.items():
            print(f"{attraction}: ${price}")
    

    def calculate_cost(self) -> None:
        self.cost = 0
        self.cost = self.ticket_prices[self.group][self.num_days]
        if isinstance(self.per_attractions, list):
            for attraction in self.per_attractions:
                self.cost += self.extra_attractions[attraction.strip()]

    def display(self) -> None:
        print(f"Ticket ID: {self.id}")
        print(f"Group: {self.group}")
        print(f"Extra attractions:", 
              f"{', '.join(self.per_attractions) if isinstance(self.per_attractions, list) else self.per_attractions}")
        print(f"Cost: ${self.cost}")


class Bookings():

    def __init__(self, num_people = 0) -> None:
        Bookings.bookings_num = 0
        self.bookings = [] 
        self.num_people = num_people
    
    def book(self) -> None:
        Bookings.bookings_num += 1
        Ticket.ticket_options()
        days = int(input("For how many days do you  want to book a ticket? (1/2)"))
        group = input("Which group are you a part of?").lower()
        choice = True if (input("Do you want extra attractions? (y/n)").lower() == "y") else False
        if choice:
            attractions = input("Which attractions do you want to add?").split(",")
        else:
            attractions = None
        temp = Ticket(id=Bookings.bookings_num, group=group, num_days=days, extra=attractions)
        
        if self.pay(temp):
            print(f"Ticket - {Bookings.bookings_num} has been booked.")
            self.bookings.append(temp)
        else:
            print(f"Ticket - {Bookings.bookings_num} wasn't paid sufficient amount, Ticket removed.")
            Bookings.bookings_num -= 1



    def pay(self, temp: Type[Ticket]) -> bool:
        temp.calculate_cost()
        temp.display()
        return (True if ( float(input(f"\nKindly pay ${temp.cost}")) >= temp.cost) else False)
        
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

            elif booking.group == "family":
                num_people = len(booking.extra_attractions) + 1  # Include the person booking
                num_families_needed = num_people // 5
                if num_people % 5 != 0:
                    num_families_needed += 1
                single_family_cost = Ticket.ticket_prices["family"][booking.num_days]
                total_family_cost = single_family_cost * num_families_needed
                alternatives.append(("Multiple Family Tickets", total_family_cost))

            best_alternative, best_cost = min(alternatives, key=lambda x: x[1])

            if best_cost < booking.cost:
                print(f"Better Option: {best_alternative} for ${best_cost} of Ticket - {booking.id}")
                switch = input(f"Do you want to switch to {best_alternative}? (y/n): ").lower()
                if switch == 'y':
                    self.switch_ticket(booking.id, new_ticket=booking)
            else:
                print(f"Current Cost of Ticket - {booking.id} is the Best Value!")


    def switch_ticket(self, booking_id: int, new_ticket: Ticket) -> None:
        for booking in self.bookings:
            if booking.id == booking_id:
                old_cost = booking.cost
                new_cost = new_ticket.cost
                refund_amount = old_cost - new_cost
                if refund_amount > 0:
                    print(f"Refunding ${refund_amount} for Booking ID: {booking_id}")
                    print("Switching to the new ticket...")
                    booking.cost = new_cost
                    booking.group = new_ticket.group
                    booking.extra_attractions = new_ticket.extra_attractions
                    return
                else:
                    print("The new ticket is not cheaper. No refund needed.")
                    return
        print(f"Booking ID {booking_id} not found.")

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