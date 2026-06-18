butterflies = 10
beetles = 12
ladybugs = 20
v = "a"
r = "aman Kumar"

print('I caught ' + str(butterflies )+ ' 🦋 butterflies!')
print('I caught ' + str(beetles) + ' 🪲 beetles!')
print('I caught ' + str(ladybugs )+ ' 🐞 ladybugs!')
total = butterflies + beetles + ladybugs
print('I caught ' + str(total) + ' total bugs!')

print(type(ladybugs))
print(ord(v))

print(r[0],r[-4])
print(r[0:5:1])
print(r[::-1]) #reverse string

print(ladybugs/5)# explicit type conversion done by python itself output 4.0

ladybugs = str(ladybugs)
print(type(ladybugs))

#Falsy values :False, 0, 0.0, (empty tuple), [empty list], {empty dictionary}, "empty string"

print(f"I caught {ladybugs} ladybugs")# Formated string

age = int(input("What is your age?"))
print(age)