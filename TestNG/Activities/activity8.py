#numList = [10, 20, 30, 40, 10]
numbers = input("Enter elements of the list separated by space: ")
list = numbers.split()
list = [int(num) for num in list]
print("Given list is ", list)

firstElement = list[0]
lastElement = list[-1]

if (firstElement == lastElement):
    print(True)
else:
    print(False)