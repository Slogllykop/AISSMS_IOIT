# Write a python program to store first year percentage of students in array. Write function for
# sorting array of floating point numbers in ascending order using
# a) Selection Sort
# b) Bubble sort and display top five scores.

def selection_sort(array):

    length = len(array)

    for i in range(length):

        minI = i
        for j in range(i+1, length):

            if array[j] < array[minI]:
                minI = j

        else:
            array[i], array[minI] = array[minI], array[i]

    else:
        return array


def bubble_sort(array):

    for i in range(len(array)):

        for j in range(len(array)-i-1):

            if array[j] > array[j+1]:

                array[j], array[j + 1] = array[j+1], array[j]

    else:
        return array


def displayTop5(array):

    print('\nTop 5 scores: ')
    for i in range(-1, -6, -1):

        print(f"{abs(i)}] {array[i]} %")


students = list(map(int, input('Enter percentages of students: ').split()))

sort_choice = int(input("Which sorting algorithm would you like to use?\n1] Selection Sort\n2] Bubble Sort\n3] Both\nEnter your choice: "))

print('\n\nOriginal marks: ', students)

if sort_choice == 1:
    print('\nSelection sort: ', selection_sort(students))

elif sort_choice == 2:
    print('\nBubble sort: ', bubble_sort(students))

elif sort_choice == 3:
    print('\nSelection sort: ', selection_sort(students))
    print('Bubble sort: ', bubble_sort(students))

# display top 5
if len(students) > 4:
    displayTop5(students)
