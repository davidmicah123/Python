# 1. Find the sum and procuct of each number in "1234567"

number_string = "1234567"

digits = [int(digit) for digit in number_string]
sum_digits = sum(digits)

product_digits = 1
for digit in digits:
    product_digits *= digit

print(f"Sum of digits: {sum_digits}")
print(f"Product of digits: {product_digits}")


print("\n")


# 2. find the product of each element in [[1,2,3], [4, 5, 6], 7] 

input_list = [[1, 2, 3], [4, 5, 6], 7]

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

flat_list = flatten(input_list)

product = 1
for num in flat_list:
    product *= num 

print(f"\n\nFlattened list: {flat_list}")
print(f"Product of all elements: {product}")

print("\n")


# 3. using list comprehension printout even numbers between 1 to 20 
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
for num in even_numbers:
    print(num)