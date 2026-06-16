# if, else, elif
a = int(input("provide a value for a"))
if a < 10:
    print("If executed")

elif a >10 and a < 50 :
    print("elif executed")
else:
    print("else executed")


gen = input(" please tell your gender as character ( M or F)")
 
if gen == "M" or gen == "m":
    print( "Good morning sir")
    
elif gen == "F" or gen == "f":
     print( "Good morning maam")
else:
   print( " invalid input")
