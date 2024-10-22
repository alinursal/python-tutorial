def calculate_average(numbers):
    # Get the sum of the list
    total_sum = sum(numbers)
    # Divide it by the length of the list to get the average
    average = total_sum / len(numbers) if numbers else 0  # Handle empty list case
    return average

numbers_list = [10, 20, 30, 40, 50]
result = calculate_average(numbers_list)
print("The average is:", result)