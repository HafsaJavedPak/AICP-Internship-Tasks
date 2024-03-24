class Ticket:
    ticket_types = {
        "adult": {"one_day": 20.00, "two_days": 30.00},
        "child": {"one_day": 12.00, "two_days": 18.00},
        "senior": {"one_day": 16.00, "two_days": 24.00},
        "family": {"one_day": 60.00, "two_days": 90.00},
        "group": {"one_day": 15.00, "two_days": 22.50}
    }

    extra_attractions = {
        "lion feeding": 2.50,
        "penguin feeding": 2.00,
        "evening barbecue": 5.00
    }

    days_available = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def __init__(self, booking_date, ticket_type, num_tickets, duration, attractions=None):
        self.booking_date = booking_date
        self.ticket_type = ticket_type
        self.num_tickets = num_tickets
        self.duration = duration
        self.attractions = attractions if attractions else []
        self.booking_number = self.generate_booking_number()

    def generate_booking_number(self):
        # Generate a unique booking number (simplified for demonstration)
        return f"WPB{len(Booking.bookings) + 1}"

    def calculate_cost(self):
        ticket_cost = self.ticket_types[self.ticket_type][self.duration] * self.num_tickets
        attraction_cost = sum([self.extra_attractions[attraction] for attraction in self.attractions])
        total_cost = ticket_cost + attraction_cost
        return total_cost

    def display_booking_details(self):
        print("------ Booking Details ------")
        print(f"Booking Number: {self.booking_number}")
        print(f"Booking Date: {self.booking_date}")
        print(f"Ticket Type: {self.ticket_type}")
        print(f"Number of Tickets: {self.num_tickets}")
        print(f"Duration: {self.duration} day(s)")
        print("Extra Attractions:")
        for attraction in self.attractions:
            print(f"- {attraction}")
        print(f"Total Cost: ${self.calculate_cost()}")
        print("-----------------------------")


class Booking:
    bookings = []

    @staticmethod
    def display_options():
        print("------ Ticket Options ------")
        for ticket_type, prices in Ticket.ticket_types.items():
            print(f"{ticket_type.capitalize()}:")
            print(f"  One-Day Ticket: ${prices['one_day']}")
            print(f"  Two-Day Ticket: ${prices['two_days']}")
            print("---------------------------")
        print("\n------ Extra Attractions ------")
        for attraction, cost in Ticket.extra_attractions.items():
            print(f"{attraction.capitalize()}: ${cost}")
        print("------------------------------")
        print("\nDays Available for Booking:")
        print(", ".join(Ticket.days_available))

    @classmethod
    def process_booking(cls):
        cls.display_options()
        booking_date = input("\nEnter booking date (e.g., Monday): ")
        ticket_type = input("Enter ticket type (e.g., adult, child, senior, family, group): ")
        num_tickets = int(input("Enter number of tickets: "))
        duration = input("Enter duration (one_day or two_days): ")
        attractions = []
        while True:
            attraction = input("Enter extra attraction (or enter 'done' to finish): ")
            if attraction.lower() == "done":
                break
            attractions.append(attraction)

        new_booking = Ticket(booking_date, ticket_type, num_tickets, duration, attractions)
        new_booking.display_booking_details()
        cls.bookings.append(new_booking)

    @classmethod
    def check_best_value(cls):
        for booking in cls.bookings:
            if booking.ticket_type == "group" and booking.num_tickets >= 6:
                num_groups = booking.num_tickets // 6
                remainder_tickets = booking.num_tickets % 6
                group_cost = num_groups * Ticket.ticket_types["group"][booking.duration]
                if remainder_tickets > 0:
                    remainder_cost = remainder_tickets * Ticket.ticket_types["group"][booking.duration]
                    if remainder_cost < Ticket.ticket_types["family"][booking.duration]:
                        booking.ticket_type = "group"
                        booking.num_tickets = remainder_tickets
                        print(f"\nBooking {booking.booking_number} converted to Group Ticket for {remainder_tickets} people.")
                    else:
                        booking.ticket_type = "family"
                        booking.num_tickets -= remainder_tickets
                        print(f"\nBooking {booking.booking_number} converted to Family Ticket for {booking.num_tickets} people.")
                    print(f"Remaining {remainder_tickets} tickets added to a new booking.")
                else:
                    booking.ticket_type = "group"
                    print(f"\nBooking {booking.booking_number} remains as Group Ticket.")
            booking.display_booking_details()

if __name__ == "__main__":
    # Task 1
    print("Task 1")
    Booking.display_options()
    print("-------------------------------------\n")

    # Task 2
    print("\nTask 2 - Process a Booking")
    Booking.process_booking()
    Booking.process_booking() 
    print("-------------------------------------\n")

    # Task 3
    print("Task 3")
    Booking.check_best_value()
    print("-------------------------------------\n")