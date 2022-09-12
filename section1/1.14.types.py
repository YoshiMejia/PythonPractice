# Simple types: Integers, String, Floats

from re import X


x = 10
y = "10"
z = 10.1
# these are implicit declarations because we didn't explicitly define what Type the two values are

sum1 = x + x
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))