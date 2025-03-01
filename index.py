# # def calculate_factorial(n):
# #     if n < 0:
# #         return "Factorial cannot be calculated for negative numbers"
    
# #     elif n == 0 or n == 1:
# #         return 1
# #     else:
# #         result = 1
# #         for i in range(2, n + 1):
# #             result *= i
# #         return result

# # print(calculate_factorial(5))


# # matrix = [
# #     [0, 1, 2],
# #     [3, 4, 5],
# #     [6, 7, 8]
# # ]

# # total_sum = 0

# # for row in range(len(matrix)):
# #     for col in range(len(matrix[row])):
# #         total_sum += matrix[row][col]

# # print("Sum of all elements:", total_sum)


# # print("\n\n")
# # for i in range(1, 6):
# #     for j in range(i):
# #         print('*', end='')
# #     print()




# # newMatrix = [
# #     [1, 2, 3],
# #     [4, 5, 6],
# # ]

# # num = 0

# # for row in range(len(newMatrix)):
# #     for col in range(len(newMatrix[row])):
# #         print(newMatrix[row])
# #         if newMatrix[row][col] < 5:
# #             num += newMatrix[row][col]

# #             print(newMatrix[row][col])
# #             break

# # print(num)


# # for i in range(1, 11):  
# #     result = 5 * i
# #     print(f"5 x {i} = {result}") 


# import tkinter as tk
# import random

# mywin = tk.Tk()
# mywin.title("Guessing game")
# mywin.geometry("450x300")

# target_number = random.randint(1, 30)
# print(target_number)

# entry = tk.Entry(mywin)
# entry.pack(pady=20)

# result_label = tk.Label(mywin, text="Guess a number between 1 and 30!")
# result_label.pack(pady=10)

# def check_guess():
#     user_guess = int(entry.get())
#     if user_guess < 1 or user_guess > 30:
#         result_label.config(text="Please enter a number between 1 and 30!")
#     elif user_guess == target_number:
#         result_label.config(text="Congratulations! You guessed correctly!")
#     elif user_guess != target_number:
#         result_label.config(text="Wrong number")
#     else:
#         result_label.config(text="Wrong number")

# submit_button = tk.Button(mywin, text="Submit Guess", command=check_guess)
# submit_button.pack(pady=10)

# mywin.mainloop()



