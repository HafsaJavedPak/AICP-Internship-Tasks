# To determine whether inputed value is int or not
def isInt(temp_val, custom_info = "inputted value", positive_only = False):
    try :
        temp_val = int(temp_val)
    except ValueError:
        print(f"The {custom_info} should be a number.")
        return False
    
    if positive_only:
        try :
            if temp_val < 0:
                raise ValueError(f"The {custom_info} should be a positive number.")
        except ValueError as e:
            print(e)
            return False
 
    return True


class senior_citizens_outing:

    outing_id = 0
    total_grps = 0
    def __init__(self):
        self.data_snrs = {} 
        self.cost_coach = 0
        self.cost_meal = 0
        self.cost_theature = 0
        self.total_snrs = 0
        self.total_carers = 0
        self.amount_paid = 0
        self.amount_total = 0
        self.notPaid_people = set()
        self.outing_id = senior_citizens_outing.total_grps
        senior_citizens_outing.total_grps += 1
    
    def input_data(self):
        for _ in range(5):
            self.input_total_snrs()
            if self.total_snrs > 0:
                break
        self.carers = 3 if self.total_snrs > 24 else 2
        
        if self.total_snrs != -1 :
            self.determine_cost()
            self.input_names()
        else:
            print("This group won't go to the outing, the total number of people entered does not satisfy criteria.")

    # To input total number of snr citizens
    def input_total_snrs (self) :
        self.total_snrs = input(f'Input the total number of senior citizens of Group - {self.outing_id}: ')
        if not isInt(self.total_snrs, 'total number of senior citizens'):
            self.total_snrs = -1
        else:
            try:
                self.total_snrs = abs(int(self.total_snrs))
                if 10 > self.total_snrs or self.total_snrs > 36:
                    raise ValueError("The total number of serior citizens should be a number between 10 and 36.")
            except ValueError as e:
                print(e)
                self.total_snrs = -1
    
    def input_names (self, add_more= False , add_more_number = 0):
        for i in range( 0 if (not add_more) else self.total_snrs, self.total_snrs + add_more_number):
            self.data_snrs[i] = [input(f"{i+1} - Name of citizen : ")]
            self.data_snrs[i].append(False)

    # determining cost and there's SOME ERROR HANDLING
    def determine_cost(self):
        if self.total_snrs != -1 :
            if self.total_snrs < 17:
                self.cost_coach = 150
                self.cost_meal = 14.00
                self.cost_theature = 21.00
            elif self.total_snrs < 27:
                self.cost_coach = 190
                self.cost_meal = 13.50
                self.cost_theature = 20.00
            elif self.total_snrs < 40:
                self.cost_coach = 225
                self.cost_meal = 13.00
                self.cost_theature = 19.00
            
            self.cost_total = round(self.cost_coach + self.cost_meal + self.cost_theature, 3)
            self.cost_perPerson = round(self.cost_total/self.total_snrs,3)
        else:
            pass

    # is there room for more people in the coach
    def extra_space(self):
        if self.total_snrs != -1 :
            for i in [16,26,39]:
                if i > self.total_snrs:
                    return (i - self.total_snrs)
            return 0
        else :
            return 0
    
    # final step
    def lets_go(self):
        if self.total_snrs != -1 :
            print("-------------------------------------------------")
            print(f"Outing ID : {self.outing_id}.\n Total amount of seniors are {self.total_snrs}")
            if self.extra_space():
                if input('Anyone else wants to go? : y/n\n') == 'y':
                    extras = abs(int(input('How many?\n')))
                    for i in [16, 26, 39]:
                        if (self.total_snrs + extras) > i:
                            print(f'Total of {i - self.total_snrs} people added. Enter their names')
                            self.input_names(True, i - self.total_snrs)
                            self.total_snrs = i
                            break
                        else:
                            print(f"Total of {extras} people added. Enter their names.")
                            self.input_names(True, extras)
                            self.total_snrs += extras 
                            break  
            
            print(f"Please pay your share.{self.cost_perPerson}$")
            for i in range(self.total_snrs):
                for _ in range(5):
                    pay = float(input(f"Citizen - {i}: Please pay your share."))
                    if pay < self.cost_perPerson:
                        print("You have paid less")
                        self.notPaid_people.add(i)
                    elif round(pay,1) == round(self.cost_perPerson,1):
                        self.data_snrs[i][1] = True
                        # not using set.remove() because I dont want to raise esxpcetion when element is not in set
                        self.notPaid_people.discard(i)
                        break
                    else :
                        self.notPaid_people.discard(i)
                        self.data_snrs[i][1] = True
                        print(f"Returning {pay - self.cost_perPerson}$ to {self.data_snrs[i][0]}")
                        break
            
            for id in self.notPaid_people:
                print(f"Citizen {id}: {self.data_snrs[id][0]} has not paid their share.")
                self.data_snrs[id].pop()
            
            if self.notPaid_people:
                print(f"Removing these people from Outing # {self.outing_id}.")

        else :
            print(f"Group {self.outing_id} does not exist as invalid data was entered.")
    
    # outputing data
    def output(self):
        print("------------------------------")
        if self.total_snrs != -1 :
            print(f"The following people are going on Outing # {self.outing_id}")
            for id, data in self.data_snrs.items():
                print(f"ID : {id}, Name : {data[0]}")
        else :
            print(f"Group {self.outing_id} does not exist as invalid data was entered.")
    
def main():
    num_outing = abs(int(input("How many groups do you want to go on an outing?: ")))
    outings = [senior_citizens_outing() for _ in range(num_outing)]

    for i in range(num_outing):
        outings[i].input_data()
        outings[i].lets_go()
        outings[i].output()
    
if __name__ == "__main__":
    main()