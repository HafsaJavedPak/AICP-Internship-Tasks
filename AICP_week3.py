from statistics import mean

class Cow:
    milking_time = 0
    yield_weekly = 0
    yield_average = 0
    def __init__ (self, cow_id) :
        try :
            if not 100 <= cow_id <= 999 :
                raise ValueError("Cow ID must be between 100 and 999.")
            else: 
                self.cow_id = cow_id
        except ValueError as e:
            print(e)

        self.yield_total = [0.0] * 14
    
    def milk_cow(self):
        self.milking_time += 1
        # week is finished
        if self.milking_time > 7 :
            self.milking_time = 0
            self.yield_average = mean(self.yield_total)
            self.yield_weekly = sum(self.yield_total)
        yield_amount = round(float(input(f"Enter the volume of milk milked from cow {self.cow_id}:\n")), 1)
        self.yield_total[int(self.milking_time/2)] = yield_amount

    def calculate_cow_stuff(self):
        if self.milking_time > 7 :  
            self.milking_time = 0
            self.yield_average = mean(self.yield_total)
            self.yield_weekly = sum(self.yield_total)           
        else:
            pass

class Herd:
    herd = {}
    num_cows = 0
    def __init__(self, num_cows):
        self.num_cows = num_cows
        self.create_cows()

    def create_cows(self):
        for i in range(self.num_cows):
            cow_id = int(input(f"Enter the ID for cow {i+1} (3-digit number between 100 and 999):\n"))
            self.herd[cow_id] = Cow(cow_id)

    def record_yield_week(self):
        for cow_id, cow in self.herd.items():
            for _ in range(14):  # Assuming 2 milkings per day for 7 days
                cow.milk_cow()

    def calculate_statistics(self):
        total_weekly_yield = sum(cow.yield_weekly for cow in self.herd.values())
        average_yield_per_cow = mean(cow.yield_average for cow in self.herd.values())

        print(f"Total Weekly Volume of Milk for the Herd: {total_weekly_yield} litres")
        print(f"Average Yield Per Cow in a Week: {average_yield_per_cow} litres")

    def identify_cows(self):
        most_productive_cow = max(self.herd.values(), key=lambda cow: cow.yield_weekly)
        low_volume_cows = [cow_id for cow_id, cow in self.herd.items() if sum(1 for yield_amount in cow.yield_total if yield_amount < 12) >= 4]

        print(f"Most Productive Cow (ID: {most_productive_cow.cow_id}): {most_productive_cow.yield_weekly} litres")
        print("Cows with Yield < 12 litres for 4 or more days:")
        for cow_id in low_volume_cows:
            print(f"Cow ID: {cow_id}")

# Main Program
if __name__ == "__main__":
    num_cows = int(input("Enter the number of cows in the herd: "))
    herd = Herd(num_cows)

    print("\nTask 1: Record the Yield")
    herd.record_yield_week()

    print("\nTask 2: Calculate the Statistics")
    herd.calculate_statistics()

    print("\nTask 3: Identify the Most Productive Cow and Low-Volume Producers")
    herd.identify_cows()
