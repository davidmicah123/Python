# import random

# numberguess = random.randint(1, 20)


# atempts = 3

# for i in range (3): 
#     userguess = int(input("Guess the number: "))

#     if userguess == numberguess:
#         print("You got it")
#         break
#     else:
#         atempts-=1
#         print("wrong guess")

#         if atempts > 1:
#             print(f"{atempts} atempts left")
#         elif atempts == 1:
#             print(f"{atempts} atempts left")
#         else:
#             print("You have no more atempts")





# dictionary
# course_result = {
#     "puthon": 95,
#     "JavaScript": 85,
#     "Golang": 65,
#     "passed": True
# }

# print(course_result)
# print(course_result["Golang"])
# print(course_result.keys())
# print(course_result.values())
# print(course_result.items())

# def sayHello():
#     print("hello")


# sayHello()
# sayHello()
# sayHello()
# sayHello()
# sayHello()
# sayHello()
# sayHello()



# def numba():
#     for i in range(10):
#         i+=1
#         print(i)

# numba()

# def numb(num):
#     for val in num:
#         print(val)

# numba()
# numb([1, 8, 8, 19, 24, 4])


# def 





# name = str(input("enter your name: "))
# age = str(input("\nenter your age: "))
# sex = str(input("\nenter your sex: "))

# def getUserDetails(name, age, sex):

    
#     userdetails = {
#         "name": name,
#         "age": age,
#         "sex": sex
#     }

#     print(userdetails.keys())

#     for value in userdetails.keys():
#         print(f"\n{value}")

#     print(f"\nYour name is: {name}, you are {age} years old and you are a {sex} person")

# getUserDetails(name, age, sex)



class Human:
    def __init__(self, name, height, gender):
        self.name = name
        self.height = height
        self.gender = gender

    def talk(self):
        print(f"my name is {self.name}, height is {self.height} and gender is {self.gender}")
    


David = Human("David", 5.8, "male")

# David.talk()




# class Fish:
#     def __init__(self, name, height, gender):
#         self.name = name
#         self.height = height
#         self.gender = gender

    
#     def swim(self):
#         print(f"my name is {self.name} I'm a {self.gender} fish, I'm {self.height} inches in height, I can swim")


# myFish = Fish("Tylapia", 2, "female")

# myFish.swim()


file = open("./file.py", "r")

print(file.read())