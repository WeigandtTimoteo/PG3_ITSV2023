import math

def calculate_statistics(numbers):
    n = len(numbers)
    mean = sum(numbers) / n

    deviation = [(x - mean) ** 2 for x in numbers]
    variance = sum(deviation) / n
    std_deviation = math.sqrt(variance)

    return mean, std_deviation