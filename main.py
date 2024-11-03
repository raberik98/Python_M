number_1 = 123
number_2 = 456


def sum_two_numbers(a, b):
    return a + b

array = [ 5,5,5,5,5,5,5,5,75,5,5 ]
for next_number in array:
    if next_number is 5:
        print("---")
    else:
        print(f"Lol I found: {next_number}")

number_3 = sum_two_numbers(number_1, number_2)
print(number_3)