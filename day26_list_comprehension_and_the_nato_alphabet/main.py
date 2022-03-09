# List Comprehension
# exercise 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n * n for n in numbers]

print(squared_numbers)

# exercise 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [even for even in numbers if even % 2 == 0]

print(result)


# exercise3
with open("file1.txt") as file1:
    num1 = file1.readlines()
    nums1 = []
    for num in num1:
        nums1.append(int(num.strip()))

with open("file2.txt") as file2:
    num2 = file2.readlines()
    nums2 = []
    for num in num2:
        nums2.append(int(num.strip()))

answer = [n1 for n1 in nums1 for n2 in nums2 if n1 == n2]
print(answer)

# exercise3 solution
with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(num) for num in file_1_data if num in file_2_data]

# write your code above
print(result)

########## Dictionary comprehension

# exercise1

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_list = sentence[:-1].split()

result = {word:len(word) for word in words_list}

print(result)

# exercise2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items() }


print(weather_f)

# exercise final
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
for (key, value) in student_data_frame.items():
    print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row)
    print(row.student)