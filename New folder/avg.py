def average(numbers):
    if len(numbers) == 0:
        return None
    else:
        return sum(numbers) / len(numbers)

list = [1, 2, 3, 6]
print ("The average of list is ", round(average(list), 2))
