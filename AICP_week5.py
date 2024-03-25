class parking_slot:
    daily_total_payments = 0
    def __init__(self, day, arrival_hour, hours_to_park, frequent_parking_num) -> None:
        self.discount = 0
        self.price_per_hour = 0
        self.max_stay = 0
        self.parking_number = frequent_parking_num
        self.arrival_hour = arrival_hour
        self.calculate_parking_stuff(day, arrival_hour, frequent_parking_num)


    @staticmethod
    def isvalid_parking_number(parking_num) -> bool:
        weights = [2, 3, 4, 5]
        parking_num = str(parking_num)
        num_digits = [int(digit) for digit in parking_num[:-1]]
        weighted_sum = sum(w * d for w, d in zip(weights, num_digits))
        check_digit = 0 if (weighted_sum % 11 == 0) else (11 - (weighted_sum % 11))
        user_check_digit = int(parking_num[-1])

        return check_digit == user_check_digit

    # calculating discount, price_per_hour, max_stay
    def calculate_parking_stuff(self, day, arrival_hour, frequent_parking_num) -> None:
        if arrival_hour >= 8 and arrival_hour <= 24:
            if self.isvalid_parking_number(frequent_parking_num):
                self.discount = 0.1 if (arrival_hour >= 8 and arrival_hour < 16) else 0.5
            else:
                self.discount = 0
            if arrival_hour >= 8 and arrival_hour < 16:
                if day.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
                    self.price_per_hour = 10
                    self.max_stay = 2
                elif day.lower() == "saturday":
                    self.price_per_hour = 3
                    self.max_stay = 4
                elif day.lower() == "sunday":
                    self.price_per_hour = 2
                    self.max_stay = 8
                else:
                    pass
            elif arrival_hour < 24 and arrival_hour >= 16:
                self.max_stay = 24 - arrival_hour
                self.price_per_hour = 2
            else:
                pass
            self.total_cost = self.price_per_hour * self.max_stay * (1 - self.discount)
        else:
            self.arrival_hour = -1  # Indicate invalid arrival hour
            print("Invalid arrival hour. Parking is only allowed between 8 and 24 hours.")
            # Reset values if invalid
            self.discount = 0
            self.price_per_hour = 0
            self.max_stay = 0

    def display_parking_stuff(self) -> None:
        print(f"Parking slot - {self.parking_number} has a discount of ${self.discount}, "
                f"\nmax stay of {self.max_stay} hours, "
                f"\na parking rate of ${self.price_per_hour} per hour.",
                f"\nand you must pay ${self.total_cost}")

    def park_car(self, amount_paid) -> None:
        if self.arrival_hour != -1:
            if amount_paid < self.total_cost:
                print("Insufficient payment. Please pay the required amount.")
                for _ in range(5):
                    amount_paid = int(input("Enter payment: "))
                    if amount_paid < self.total_cost and _ != 5:
                        print("Insufficient payment. Please pay the required amount.")  
                    elif amount_paid < self.total_cost and _ == 5:
                        return
                    else:
                        break

            parking_slot.daily_total_payments += amount_paid  # Add payment to daily total
            change = amount_paid - self.total_cost  # Calculate change (if any)

            print(f"Thank you for parking! Your total cost is ${self.total_cost:.2f}")
            if change > 0:
                print(f"Change: ${change:.2f}")
        else:
            print("This is an invalid parking spot. No payment needed.")

    @classmethod
    def display_daily_total(cls) -> None:
        print(f"Daily Total Payments: ${cls.daily_total_payments:.2f}")

    def input_attributes(self) -> None:
        self.day = input("Enter day of the week: ")
        self.arrival_hour = int(input("Enter hour of arrival (0-23): "))
        if self.arrival_hour < 8 or self.arrival_hour > 24:
            self.arrival_hour = -1  # Indicate invalid arrival hour
            print("Invalid arrival hour. Parking is only allowed between 8 and 24 hours.")
            return

        self.hours_to_park = int(input("Enter hours to park: "))
        self.frequent_parking_num = input("Enter frequent parking number (if available): ")

        self.calculate_parking_stuff(self.day, self.arrival_hour, self.frequent_parking_num)


def main() -> None:
    parking_spots = []  # List to hold parking spots

    print("WELCOME TO THE PARKING LOTS!\n")

    print("Welcome to the Parking Lot!")
    for i in ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]:
        print(f"For day {i.capitalize()}")
        print("Enter 'park' to park your car and 'exit' to exit the day.")
        while True:
            choice = input("Enter choice : ").lower()

            if choice == "exit" and len(parking_spots) != 0:
                print()
                for spot in parking_spots:
                    print(f"Parking Slot - {spot.parking_number}")
                    spot.display_parking_stuff()
                    paid_amount = float(input("Enter amount to pay: "))
                    spot.park_car(paid_amount)
                parking_slot.display_daily_total()
                print("Thank you for using the Parking Lot!")
                parking_spots = []
                break
            elif choice == "exit" and len(parking_spots) == 0:
                break

            day = i
            arrival_hour = int(input("Enter hour of arrival (0-23): "))
            if arrival_hour < 8 or arrival_hour > 24:
                arrival_hour = -1  # Indicate invalid arrival hour
                print("Invalid arrival hour. Parking is only allowed between 8 and 24 hours.")
                continue

            hours_to_park = int(input("Enter hours to park: "))
            frequent_parking_num = input("Enter frequent parking number (if available): ")
            if parking_slot.isvalid_parking_number(frequent_parking_num):
                print("You have entered a valid parking number.")
            else:
                print("You have entered an invalid parking number.")

            parking_spots.append(parking_slot(i,arrival_hour,hours_to_park,frequent_parking_num))
            
if __name__ == "__main__":
    main()
