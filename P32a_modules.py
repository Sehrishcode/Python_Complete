def lbs_to_kg(weight):
    return weight * 0.45
def kg_to_lbs(weight):
    return weight/0.45
print(".................Assingment Find a number....................")
def find_max(numbers):
    maximun = numbers[0]
    for number in numbers:
        if number> maximun:
            maximun = number
    return maximun