import sys, csv, math

knn_instances = list()
k_value = 0
total_number_of_instances = 0
number_of_correct_dedutions = 0

def check_arguments():

    if(len(sys.argv) != 4):
        print('\n\tCall python3 knn.py k_value training_file test_file\n')
        exit()

    if(not sys.argv[1].isnumeric()):
        print('\n\tInvalid value of K. It must be a number.\n')
        exit()

    if((int(sys.argv[1]) % 2) == 0):
        print('\n\tInvalid value of K. It must be a odd number.\n')
        exit()

def insert_nearest_instance(value, target):

    global knn_instances
    new_instance = list([value, target])
    knn_instances.append(new_instance)

def sort_nearest_instances():

    global knn_instances
    knn_instances.sort(key=lambda x:x[0])

def remove_less_close_instance(): 

    global knn_instances, k_value
    if(len(knn_instances) > k_value):
        knn_instances.pop(k_value)

def add_nearest_instance(value, target):
    
    insert_nearest_instance(value, target)
    sort_nearest_instances()
    remove_less_close_instance()
   
def calculate_distancy(test_instance, training_instance):

    summation = 0
    target = training_instance[len(training_instance)-1]

    for i in range(0, len(training_instance) - 1):
        summation += pow((float(test_instance[i]) - float(training_instance[i])), 2)

    add_nearest_instance(math.sqrt(summation), target)

def check_result(test_instance):

    global knn_instances, k_value, number_of_correct_dedutions
    
    aux = 0
    for i in knn_instances:
        if(i[1] == '1.0'):
            aux += 1

    result = 1 if (aux > k_value / 2) else 0
        
    if(result == int(float(test_instance[len(test_instance) - 1]))):
        number_of_correct_dedutions += 1

def analyze_instance(test_instance):

    global knn_instances
    knn_instances.clear()

    with open(sys.argv[2]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        firstRow = True
        for training_instance in csv_reader:
            if(firstRow):
                firstRow = False                
            else:
                calculate_distancy(test_instance, training_instance)
        check_result(test_instance)        

check_arguments()

k_value = int(sys.argv[1])

print('\n\t*** KNN Algotithm ***')
print('\n\tChosen K value: ' + sys.argv[1])
print('\tPath to training file: ' + sys.argv[2])
print('\tPath to test file: ' + sys.argv[3])
print('\n\t********************')
print('\n\tRunning KNN Algotithm...')

try:
    with open(sys.argv[3]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        firstRow = True
        for test_instance in csv_reader:
            if(firstRow):
                firstRow = False                
            else:
                total_number_of_instances += 1
                analyze_instance(test_instance)

        print('\n\tAccuracy(%): ' + str(((100*number_of_correct_dedutions)/total_number_of_instances)))
        print('\n\tExecution complete successfully.\n')

except: 
    print('\n\tAn except occurred. Check the path of the input files.')
    print('\n\tExecution failed.\n')

