# to auto-generate lists with a certain order, you can use a Range. It's another type of object.
student_grades = list(range(0,11))
# by encapsulating range(0,11) inside of list() we are converting that range(0,11) to an array/list which would output like so:
#Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(student_grades)

#note that the range goes up to the number before the 2nd arg, so (0,11) goes up to 10. 
