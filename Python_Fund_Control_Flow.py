#2.Data types 
#Exercise Snackin

'''
favorite_snack = "Popcorn";
print("MY favorite snack is " + favorite_snack)

a = "I could eat";
b = 100;
c = favorite_snack;

print (a + str(b) + c)

for i in range(77):
    print("My fav snack is "+ favorite_snack)

'''

#2.Data types 
#Exercise Grocery Shopping

'''
#1
print('milk','eggs','salmon','chicken','butter')

#2
print (5.63+13.40+3.99+4.57+2.47)

#3
print("salmon \n" * 100)

#4
print("salmon " * 100)

#5
print('milk','eggs','salmon','chicken','butter')

'''


#2.Data types 
#Exercise String Flings

'''

#1
season = "Spring"

#2
anything = (season + "Fling")

#3
print(season)

#4
temp = season
season = "Summer"
print(temp)

#5
print(temp + " " + season )

'''

#3.Control Flow  
#Exercise Baker's Match

'''
#1
num_people = 8

#2
if num_people >= 10:
    num_cookies = num_people*2
#3
elif num_people < 10:
    num_cookies = num_people*3
#4
print ("We will be printing " + str(num_cookies))

'''
#.Control Flow  
#Exercise So Complicated

'''
you = "fall"
u = "crawl"

if you == "fall" and u == "crawl":
    print ("and you break")
elif you == "take" and u == "get":
    print("you turn into")
else:
    print("No, no, no")
'''

#.Control Flow  
#Exercise for Loopin'

'''
#1
num_1 = 1
num_2 = 3

count = 0

for i in range(num_1,num_2+1):
    count = count + i
print ("Sum == " + str(count))

#2

long_text = ("Pneumonoultramicroscopicsilicovolcanoconiosis")
vowels = ('a','e','i','o','u')

for i in long_text:
    for x in vowels:
        if x == i:
            print(i)
   
#or this problem can also be solved like so 

for i in long_text:
    if i in vowels:
        print(i)

'''

#.Control Flow  
#Exercise while Loopin'

'''
#1
num = 200
count = 0
while num > 1:
    num = num/2
    count += 1
    
print(count)

#2
num_1 = 5
num_2 = 2

 

for i in range(num_1,num_2-1,-1):
    print(i)
print("Blast Off!")
'''
