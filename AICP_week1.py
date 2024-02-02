import os

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

def input_weight(index, name='') :
    # for loop with limit is used to avoid an infinte loop
    for _ in range(5):
        weight = input(f"Input weight of pupil#{index+1}" +
                       ": " if name == "" else f"- {name} :")
        if weight_isvalid(weight):
            break
    if weight_isvalid(weight):
        return float(weight)
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

    for i, (name, weight) in enumerate(zip(names, weights), 1):
        print(f"Pupil #{i}: Name: {name}, Weight: {weight} kg")

    print("---------------------------------------")

def main():
    # task 1 
    print("TASK 1")
    pupils_num = 30
    pupils_names = []
    pupils_weights = []
    pupils_names, pupils_weights = input_pupilData(pupils_num, True)
    output_pupilsData(pupils_names, pupils_weights)

    print("\n-------------------------------------\n")

    # task 2
    input('Press any key to continue to TASK 2')
    os.system('cls')
    print("TASK 2")
    pupils_newWeights = input_pupilData(pupils_num)
    
    
    pupils_weightDifference = []
    for i in range(pupils_num):
        if pupils_newWeights[i] == -1 or pupils_weights[i] == -1 :
            pupils_weightDifference.append(-1)
        else:
            pupils_weightDifference.append(pupils_newWeights[i] - pupils_weights[i])
    
    # task 3 
    input('Press any key to continue to TASK 3')
    os.system('cls')
    print("TASK 3")
    for i in range(pupils_num):
        if abs(pupils_weightDifference[i]) >= 2.5 and pupils_weightDifference[i] != -1:
            print(f"Pupil#{i+1} - {pupils_names[i]} has", 
                  "gained" if pupils_weightDifference[i] > 0 else "lost", 
                  f"{abs(pupils_weightDifference[i])} kg.")
        elif pupils_weightDifference[i] != -1:
            print(f"Pupil#{i+1} - {pupils_names[i]} has not lost weight.") 
        else :
            print(f"Pupil#{i+1} - {pupils_names[i]} has entered invalid weights.")


if __name__ == "__main__":
    main()
