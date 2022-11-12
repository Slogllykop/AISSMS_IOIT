# Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N
# students in the class. Write functions to compute following:
# a) The average score of class
# b) Highest score and lowest score of class
# c) Count of students who were absent for the test
# d) Display mark with highest frequency


# length of the students arary
def length(mainList):
    count = 0

    for i in mainList:
        count += 1

    else:
        return count

# count of a specific element in the array


def count(mainList, r):
    count = 0

    for i in mainList:

        if i == r:
            count += 1

    else:
        return count


# avg of the array
def avg(mainList):
    sum = 0

    for i in mainList:

        if i != -1:
            sum += i

    else:
        return sum/length(mainList)


# max element in the array
def max(mainList):
    max = 0

    for i in mainList:

        if i != -1:
            max = i
            break

    for j in mainList:

        if j > max:
            max = j

    else:
        return max

# min element in the array


def min(mainList):
    min = 0

    for i in mainList:

        if i != -1:
            min = i
            break

    for j in mainList:

        if j != -1:
            if j < min:
                min = j

    else:
        return min

# mode of the array


def mode(mainList):
    tempL = []

    for i in mainList:
        tempL.append(count(mainList, i))

    mode = mainList[tempL.index((max(tempL)))]

    return mode

# absent students in the array


def abs(mainList):
    count = 0

    for i in mainList:

        if i == -1:
            count += 1

    else:
        return count


# main list of the students stored in an array
mainList = list(map(int, input('Enter marks of students: ').split()))

# menu for the code
choice = input(
    '\nChoose one operation index:\n[1] Average\n[2] Highest and Lowest\n[3] Mode\n[4] Absent students\n[5] All\n\nYour choice: ')

if choice == '1':
    print(f'\nAverage: {avg(mainList)}')

elif choice == '2':
    print(f'\nHighest score: {max(mainList)}\nLowest score: {min(mainList)}')

elif choice == '3':
    print(f'\nMode: {mode(mainList)}')

elif choice == '4':
    print(f'\nAbsent students: {abs(mainList)}')

elif choice == '5':
    print(f'\nAverage: {avg(mainList)}\nHighest score: {max(mainList)}\nLowest score: {min(mainList)}\nMode: {mode(mainList)}\nAbsent students: {abs(mainList)}\n')

else:
    print("Invalid choice, try again!")
