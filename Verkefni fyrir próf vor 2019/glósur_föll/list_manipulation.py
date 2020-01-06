def addToList(li, elem):
    '''Adds elem to the back of the list li'''
    li.append(elem)

def removeFromList(li, i):
    '''Removes the element at index i in li'''
    li.pop(i)


def printList(li):
    '''Prints the list'''
    for x in li:
        print(x,"", end="")


def getListElement(li, i):
    '''Prints the lists element at index i in li'''
    print(li[i])


def printListBackwards(li):
    '''Prints the list li backwards'''
    for x in li[::-1]:
        print(x, "", end="")


def printListEveryOtherElement(li):
    '''Prints every other element of the list li'''
    for x in li[::2]:
        print(x, "", end="")


def printSlicedList(li, a, b):
    '''Prints elements from index a to index b in the list li'''
    for x in li[a:b]:
        print(x, "", end="")


def get_action():
    print()
    print('1: Add to the list')
    print('2: Remove from the list')
    print('3: Print the list')
    print('4: Print a single element from the list')
    print('5: Print the list backwards')
    print('6: Print every other element of the list')
    print('7: Print sliced list')
    print('Other: Quit')

    return input("Select an action: ")


def main():
    my_list = []

    while True:
        action = get_action()

        if action == '1':
            new_element = input("Enter new element: ")
            addToList(my_list, new_element)
        elif action == '2':
            index = int(input("Enter the index of the element you want to remove: "))
            removeFromList(my_list, index)
        elif action == '3':
            printList(my_list)
        elif action == '4':
            index = int(input("Enter the element's index: "))
            getListElement(my_list, index)
        elif action == '5':
            printListBackwards(my_list)
        elif action == '6':
            printListEveryOtherElement(my_list)
        elif action == '7':
            begin_index = int(input("Enter list index: "))
            end_index = int(input("Enter the latter index: "))
            printSlicedList(my_list, begin_index, end_index)
        else:
            break


main()