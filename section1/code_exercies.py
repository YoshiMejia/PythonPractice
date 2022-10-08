# Count Values (E)
# Below you can see a student_grades list. 
# Your task is to use Python to count how many items with a value of 10.0 are in the student_grades list. 
# Once you find the proper list method that counts items, then print out its output using a print() function.

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
occur = student_grades.count(10.0)
# when a value is passed into the count method, it counts the number of occurences of that value inside the list that it is called on
print(occur)


# Modify String (E)
# Like the previous exercise, find the proper function or method that converts the string in username into lowercase letters and prints out the output.
username = "Python3"
print(username.lower())

# Create Complex Dictionary (E)
# Assign a dictionary to variable day_temperatures.
#  The dictionary should contain three keys: 'morning', 'noon', and 'evening' and each key should contain a tuple as value.
#  Each tuple should contain three floats.
day_temperatures = { "morning": (1.2, 3.3, 4.4), "noon": (12.2, 12.34, 12.565), "evening": (12.3, 12.12, 14.3)}
