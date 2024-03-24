# asl for hours input, figure out time, and parking number

class parking_slot:


    def __init__(self, parking_num) -> None:
        self.discount = 0
        self.price_per_hour = 0
        self.parking_number = parking_num


    @staticmethod
    def isvalid_parking_number (parking_num) -> bool:
        weights = [2,3,4,5]
        parking_num = str(parking_num)
        num_digits = [int(digit) for digit in parking_num[:-1]]
        weighted_sum = [w*d for w,d in zip(weights,num_digits)]
        check_digit = 0 if (weighted_sum % 11 == 0) else (11 - (weighted_sum % 11))
        user_check_digit = int(parking_num[-1])

        return (check_digit==user_check_digit)

    # calculating discount, price_per_hour, max_stay 
    def calculate_parking_stuff(self, day, arrival_hour, frequent_parking_num) -> None:
        if arrival_hour >= 8 and arrival_hour <= 24:
            if self.isvalid_parking_number():
                self.discount = 0.1 if (arrival_hour >= 8 and arrival_hour < 16) else 0.5
            else:
                self.discount = 0
            if arrival_hour >= 8 and arrival_hour < 16:
                if day.lower() in ["monday","tuesday","wednesday","thursday","friday"]:
                    self.price_per_hour = 10
                    self.max_stay = 2
                elif day.lower() == "saturday" :
                    self.price_per_hour = 3
                    self.max_stay = 4
                elif day.lower() == "sunday" :
                    self.price_per_hour = 2
                    self.max_stay = 8
                else:
                    pass
            elif arrival_hour < 24 and arrival_hour >= 16 :
                self.max_stay = 24 - arrival_hour
                self.price_per_hour = 2
            else:
                pass
        else : 
            pass
        
    def display_parking_stuff(self) -> None:
        print(f"Parking slot - {self.parking_number} has a discount of ${self.discount}, 
              \nmax stay of {self.max_stay} hours, 
              \na parking rate of ${self.price_per_hour} per hour.")
    
    def park_car(self, amount_paid) -> None:
        total_cost = self.price_per_hour * self.max_stay * (1 - self.discount) 
        if amount_paid < total_cost:
            print("Insufficient payment. Please pay the required amount.")
            return

        parking_slot.daily_total_payments += amount_paid  # Add payment to daily total
        change = amount_paid - total_cost  # Calculate change (if any)

        print(f"Thank you for parking! Your total cost is ${total_cost:.2f}")
        if change > 0:
            print(f"Change: ${change:.2f}")

    @classmethod
    def display_daily_total(cls) -> None:
        print(f"Daily Total Payments: ${cls.daily_total_payments:.2f}")

def main() -> None:
    print("Task 1")
    day = input("Enter day of the week: ")
    arrival_hour = int(input("Enter hour of arrival (0-23): "))
    hours_to_park = int(input("Enter hours to park: "))
    frequent_parking_num = input("Enter frequent parking number (if available): ")

    parking = parking_slot(day, arrival_hour, hours_to_park, frequent_parking_num)
    parking.calculate_parking_stuff()
    parking.display_parking_stuff()

    # Task 2 - Keeping a total of the payments
    print("\nTask 2")
    parking_slot.daily_total = 0  # Reset daily total

    ask = ""
    while ask != "exit":
        customer_day = input("Enter day of the week for this customer: ")
        customer_arrival_hour = int(input("Enter hour of arrival (0-23) for this customer: "))
        customer_hours_to_park = int(input("Enter hours to park for this customer: "))
        customer_frequent_parking_num = input("Enter frequent parking number for this customer (if available): ")

        customer_parking = parking_slot(customer_day, customer_arrival_hour, customer_hours_to_park, customer_frequent_parking_num)
        customer_parking.calculate_parking_stuff()
        customer_parking.display_parking_stuff()

        paid_amount = float(input("Enter amount paid: "))
        customer_parking.park_car()

        ask = input("Enter 'exit' to finish or press enter to continue: ")

    print(f"\nTotal daily payments: ${parking_slot.daily_total}")


    # Task 3 - Making payments fairer
    print("\nTask 3")
    print("Customer arriving at 14:45 on a Sunday and parking for five hours:")
    parking = parking_slot("Sunday", 14, 5, "12345")
    parking.calculate_parking_stuff()
    parking.display_parking_stuff()
    parking.park_car()

if __name__ == "__main__":
    main()