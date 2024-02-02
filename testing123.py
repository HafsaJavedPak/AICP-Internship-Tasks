from AICP_week1 import output_pupilsData, input_pupilData

def output_test():
    hi = [2,2,2,2]
    bye = ['2','2','2','2']

    output_pupilsData(bye,hi)

def input_test() :
    testing_list = input_pupilData(2)
    print(testing_list)

if __name__ == "__main__" :
    output_test()
    input_test()