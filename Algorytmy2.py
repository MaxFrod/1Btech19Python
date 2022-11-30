# a = int(input())
# b = int(input())
# iloczyn = a * b
# while a != b:
#   if a > b : a = a - b
#   if b > a : b = b - a
#   print(iloczyn // a)


a = int(input())
b = int(input())
iloczyn = a * b
while b > 0:
    a, b = b, a%b
nwd = a
print(iloczyn // nwd)