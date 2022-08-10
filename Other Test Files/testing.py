def isPrime(n):
    for i in range(2,n):
        if (n%i) == 0:
            return False
    return True



input_array=    [   [215, 0,     0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0],
                            [193, 124,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0],
                            [117, 237, 442,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0],
                            [218, 935, 347, 235,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0],
                            [320, 804, 522, 417, 345,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0],
                            [229, 601, 723, 835, 133, 124,   0,   0,   0,   0,   0,   0,   0,   0,  0],
                            [248, 202, 277, 433, 207, 263, 257,   0,   0,   0,   0,   0,   0,   0,  0],
                            [359, 464, 504, 528, 516, 716, 871, 182,   0,   0,   0,   0,   0,   0,  0],
                            [461, 441, 426, 656, 863, 560, 380, 171, 923,   0,   0,   0,   0,   0,  0],
                            [381, 348, 573, 533, 447, 632, 387, 176, 975, 449,   0,   0,   0,   0,  0],
                            [223, 711, 445, 645, 245, 543, 931, 532, 937, 541, 444,   0,   0,   0,  0],
                            [330, 131, 333, 928, 377, 733,  17, 778, 839, 168, 197, 197,   0,   0,  0],
                            [131, 171, 522, 137, 217, 224, 291, 413, 528, 520, 227, 229, 928,   0,  0],
                            [223, 626,  34, 683, 839,  53, 627, 310, 713, 999, 629, 817, 410, 121,  0],
                            [924, 622, 911, 233, 325, 139, 721, 218, 253, 223, 107, 233, 230, 124, 233]  ]

# max_depth = len(input_array)
path_array = []
diver = 1
totalSum = 0
header_x = 0
header_y = 0
if input_array[0][0] == 0 or  isPrime(input_array[0][0]) == False:
    totalSum = input_array[0][0]
    path_array.append(input_array[0][0])
    for diver in input_array:
        #magic
        print("#######################################################################################################################################")
        print("Current diving level: " + str(diver))
        print("Total Sum before process: " + str(totalSum))
        bottomN = input_array[header_y+1][header_x] 
        rightN1 = input_array[header_y+1][header_x+1]

        primeChecker1 =  isPrime(bottomN)
        primeChecker2 =  isPrime(rightN1)
        print("Prime checker for " + str(bottomN) + " is ->"+ str(primeChecker1))
        print("Prime checker for " + str(rightN1) + " is ->"+ str(primeChecker2))
        #you reversed true@s and false@s from here
        if primeChecker1 == False and primeChecker2 == False:
            if bottomN > rightN1:
                totalSum += bottomN
                path_array.append(bottomN)
                header_x = (header_x)
                header_y = (header_y+1)
            elif rightN1 > bottomN:
                totalSum += rightN1
                path_array.append(rightN1)
                header_x = (header_x+1)
                header_y = (header_y+1)
        elif primeChecker1 == False and primeChecker2 == True:
                totalSum += bottomN
                path_array.append(bottomN)
                header_x = (header_x)
                header_y = (header_y+1)
        elif primeChecker1 == True and primeChecker2 == False:
                totalSum += rightN1
                path_array.append(rightN1)
                header_x = (header_x+1)
                header_y = (header_y+1)
        print("Total Sum after process: " + str(totalSum))
        print("path array")
        print(path_array)
    total_path = 0
    i = 0
    for i in range(0,len(path_array)):
        total_path = total_path + path_array[i]
    print(total_path)
