# Task 1
def task1(numbers):
    return sum(numbers)

# Task 2
def task2(data):
    return len(data)

# Task 3
def task3(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[0]

# Task 4
def task4(data):
    dictionary = data[0]
    return dictionary.get("name")

# Task 5
def task5(data):
    sorted_tuples = sorted(data, key=lambda x: len(x[0]) if isinstance(x[0], str) else x[0])
    return sorted_tuples[-1][-1]

# Task 6
def task6(data):
    filtered_numbers = [number for sublist in data for number in sublist if isinstance(number, int) and number % 2 != 0]
    product = 1
    for num in filtered_numbers:
        product *= num
    return product

# Task 7
def task7(data):
    return sum(second for first, second in data)

# Example usage:
tuple1 = (3, 5)
tuple2 = (1, 2, 'a', 'b', 'c')
tuple3 = (10, 5, 8, 3)
tuple4 = ({'name': 'John', 'age': 30},)
tuple5 = ([(1, 2, 3), (4, 5), (6, 7, 8, 9)])
tuple6 = ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15])
tuple7 = ((1, 2), (3, 4), (5, 6), (7, 8))

print(task1(tuple1)) 
print(task2(tuple2))  
print(task3(tuple3))  
print(task4(tuple4)) 
print(task5(tuple5)) 
print(task6(tuple6))  
print(task7(tuple7))  
