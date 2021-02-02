import sys, csv, math

knn_instances = list()

def check_arguments():

    if(len(sys.argv) != 4):
        print('Call python3 knn.py k_value training_file test_file')
        exit()

    if(not sys.argv[1].isnumeric()):
        print('Invalid value of K. It must be a number.')
        exit()

    if((int(sys.argv[1]) % 2) == 0):
        print('Invalid value of K. It must be a odd number.')
        exit()

def compare_instances(instance, row):

    summation = 0
    
    for i in range(0, len(row) - 1):
        summation += pow((instance[i] - row[i]), 2)

    print(math.sqrt(summation))


def analyze_instance(instance):

    with open(sys.argv[2]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        firstRow = True
        for row in csv_reader:
            if(firstRow):
                firstRow = False                
            else:
                compare_instances(instance, row)


check_arguments()

print('\n*** KNN Algotithm ***')
print('\nChosen K value: ' + sys.argv[1])
print('Path to training file: ' + sys.argv[2])
print('Path to test file: ' + sys.argv[3])

try:
    with open(sys.argv[3]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        firstRow = True
        for row in csv_reader:
            if(firstRow):
                firstRow = False                
            else:
                analyze_instance(row)
except: 
    print('\nAn except occurred. Check the path of the input files.')
    
