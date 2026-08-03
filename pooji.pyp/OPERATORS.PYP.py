# B1.1

a = 23
b = 6

print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)
print("Floor Division (//):", a // b)
print("Modulus (%):", a % b)
print("Exponent (**):", a ** b)

#OUTPUT:
#Addition (+): 29
#Subtraction (-): 17
#Multiplication (*): 138
#Division (/): 3.8333333333333335
#Floor Division (//): 3
#Modulus (%): 5
#Exponent (**): 148035889



# B2.1

m = int(input("Enter m: "))
n = int(input("Enter n: "))

print("m == n :", m == n)
print("m != n :", m != n)
print("m > n  :", m > n)
print("m < n  :", m < n)
print("m >= n :", m >= n)
print("m <= n :", m <= n)

#OUTPUT:
#Enter m: 10
#Enter n: 20
#m == n : False
#m != n : True
#m > n  : False
#m < n  : True
#m >= n : False
#m <= n : True

# B3.1

score = 50
print("Initial score =", score)

score += 10
print("After += 10 :", score)

score -= 5
print("After -= 5 :", score)

score *= 2
print("After *= 2 :", score)

score /= 5
print("After /= 5 :", score)

score //= 2
print("After //= 2 :", score)

score %= 4
print("After %= 4 :", score)

score **= 3
print("After **= 3 :", score)

#OUTPUT:
#Initial score = 50
#After += 10 : 60
#After -= 5 : 55
#After *= 2 : 110
#After /= 5 : 22.0
#After //= 2 : 11.0
#After %= 4 : 3.0
#After **= 3 : 27.0


# B4.1

percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance (%): "))

eligible = percentage > 75 and attendance > 90

print("Eligible for scholarship:", eligible)

#OUTPUT:
#Enter percentage: 85
#Enter attendance (%): 92
#Eligible for scholarship: True


# B5.1 

p = 12
q = 10

print("Binary of p:", bin(p))
print("Binary of q:", bin(q))

print("p & q =", p & q)
print("p | q =", p | q)
print("p ^ q =", p ^ q)
print("~p =", ~p)
print("p << 2 =", p << 2)
print("p >> 2 =", p >> 2)

#OUTPUT:
#Binary of p: 0b1100
#Binary of q: 0b1010
#p & q = 8
#p | q = 14
#p ^ q = 6
#~p = -13
#p << 2 = 48
#p >> 2 = 3


# B6.1 

fruits = ["apple", "banana", "mango", "grape", "kiwi"]

item = input("Enter a fruit: ")

print(item, "is in the list:", item in fruits)
print(item, "is not in the list:", item not in fruits)

#OUTPUT:
#Enter a fruit: mango
#mango is in the list: True
#mango is not in the list: False


# B7.1 

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2 :", list1 == list2)
print("list1 is list2 :", list1 is list2)
print("list1 is list3 :", list1 is list3)
print("list1 is not list2 :", list1 is not list2)

print("ID of list1:", id(list1))
print("ID of list2:", id(list2))
print("ID of list3:", id(list3))

#OUTPUT:
#list1 == list2 : True
#list1 is list2 : False
#list1 is list3 : True
#list1 is not list2 : True
#ID of list1: 140236579862080
#ID of list2: 140236579860864
#ID of list3: 140236579862080






