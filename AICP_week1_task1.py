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

def input_weights(total_pupils) :
    weights = []
    names = []

    for i in range(total_pupils):
        name = input(f"Input name of pupil#{i+1} : ")
        
        # for loop with limit is used to avoid an infinte loop
        for _ in range(5):
            weight = input(f"Input weight of pupil#{i+1} : ")
            if weight_isvalid(weight):
                break
        
        if weight_isvalid(weight):
            names.append(name)
            weights.append(weight)

    return names, weights

def output_weights(weights, names):
    print("---------------------------------------")
    print("Printing the names and weights of pupils.")
    print("---------------------------------------")

    for i, (name, weight) in enumerate(zip(names, weights), 1):
        print(f"Pupil #{i}: Name: {name}, Weight: {weight} kg")

    print("---------------------------------------")


def main():
    weight_isvalid('qe')

if __name__ == "__main__":
    main()