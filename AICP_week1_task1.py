""""A school keeps records of the weights of each pupil. 
The weight, in kilograms, of each pupil isrecorded on the first day of term. 
Input and store the weights and names recorded for a class of30 pupils. 
You must store the weights in a one-dimensional array and the names in another one-dimensional array. 
All the weights must be validated on entry and any invalid weights rejected. 
Youmust decide your own validation rules. You may assume that the pupils’ names are unique. 
Outputthe names and weights of the pupils in the class"""

def weight_isvalid (weight):
    try :
        weight = float(weight)
    except ValueError:
        print("Weight should be a number.")
        return False

    try:
        weight = float(weight)
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        # min and max human weights in kg.
        if not (15 <= weight <= 650):
            raise ValueError("Weight should be between 15 and 650 kg.")
        return True
    except ValueError as e:
        print(f"Invalid weight: {e}")
        return False

def input_weight(index) :
    # for loop with limit is used to avoid an infinte loop
    for _ in range(5):
        weight = input(f"Input weight of pupil#{index+1} : ")
        if weight_isvalid(weight):
            break
    if weight_isvalid(weight):
        return weight
    else : 
        return -1

def input_pupilData(total_pupils, returnNames = False) :
    weights = []
    if returnNames :
        names = []

    for i in range(total_pupils):
        if returnNames :
            name = input(f"Input name of pupil#{i+1} : ")
        
        weight = input_weight(i)
        # if user has still not entered valid weight
        if weight == -1 :
            if returnNames :
                names.append(name)
            weights.append(weight)

    if returnNames :
        return names, weights
    else :  
        return weights

def output_pupilsData(names, weights):
    print("---------------------------------------")
    print("Printing the names and weights of pupils.")
    print("---------------------------------------")

    for i, (name, weight) in enumerate(zip(names, weights), 1):
        print(f"Pupil #{i}: Name: {name}, Weight: {weight} kg")

    print("---------------------------------------")

def main():
    # task 1 
    print("TASK 1")
    pupils_num = 2
    pupils_names = []
    pupils_weights = []
    pupils_names , pupils_weights = input_pupilData(pupils_num , True)
    output_pupilsData(pupils_names, pupils_weights)

    print("\n-------------------------------------\n")

    # task 2
    print("TASK 2")
    pupils_newWeights = input_pupilData(pupils_num)
    pupils_weightDifference = []
    for i in range(pupils_num):
        pupils_weightDifference.append(pupils_newWeights[i] - pupils_weights[i])
    output_pupilsData(pupils_names, pupils_newWeights)

    print("\n-------------------------------------\n")

    # task 3 
    print("TASK 3")
    for i in range(pupils_num) :
        if abs(pupils_weightDifference[i]) >= 2.5 :
            print(f"{pupils_names[i]} has ", "gained" if pupils_weightDifference[i] > 0 else "lost", f"{abs(pupils_weightDifference[i])} kg.")


if __name__ == "__main__":
    main()