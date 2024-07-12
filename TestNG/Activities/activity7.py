numbers = input("Enter elements of the list separated by space: ")
list = numbers.split()
list = [int(num) for num in list]
print("Elements in list",list)
total=0
for ele in range(0, len(list)):
    total += list[ele]
print("Sum of elements in list",total)