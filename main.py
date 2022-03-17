def bubbleSort(array):
    print("Array before 'bubbleSort(array)':")
    print("\n")
    print(arraybefore) # <- Sorting process is being "visualised"
    for j in range(len(array)):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                print(arraybefore)

# bubbleSort Function is getting defined ^^


#arraybefore = [1023, 2354, 4233, 11, 496, 235423, 2, 8, 3746738, 234]
array_input = input("Enter different numbers with spaces between them: ") # <- Input ('array_input') gets "defined" by user
arraybefore = [float(x) for x in array_input.split()] # <- Decimal number can be used due to float() function
bubbleSort(arraybefore) #  <- Input ('array_input') gets passed through bubbleSort()

print("\n")

print("Result of 'bubbleSort(array)' function:")
print("\n")
print(arraybefore) # <- Result of bubbleSort is getting printed out
