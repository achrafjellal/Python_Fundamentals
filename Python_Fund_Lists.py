import math

#6.Lists 
#Exercise Listin'

 #1 Write a function called largest_num which will take in a list of numbers and return the largest number from that list. 
 # Do not use any built-in methods to solve this problem.

def largest_num(nums):
     largest = nums[0]
     for i in nums:
         if i > largest:
             largest = i
     return largest
    
#2 Write a function called includes that takes a list of numbers and a number as input. 
# This function returns a boolean indicating whether or not the list contains the number.

def includes(listnums, num):
    for i in listnums:
        if i == num:
            return True
    else:
        return False
         
#3 Write a function called average that takes in a list of numbers 
# and returns a float representing the average value of the those numbers!

def average(listnums):
    total = 0.0
    for i in listnums:
        total += i
    return float(total) / len(listnums)


#4 Write another function called median that takes in a list of numbers 
# and returns a float representing the median from that list.

def median(listnums):
    sortedList = sorted(listnums)
    lenList = len(sortedList)
    
    for i in sortedList:
        if lenList % 2 == 0:
            val1=sortedList[int(lenList/2)]
            val2=sortedList[(int(lenList/2)-1)]
            return (val1+val2) / 2
        else:
            return sortedList[int((lenList-1)/2)]   
            

#5 Write a function called only_a that takes in a list of strings and returns a list of strings that contain the letter 'a'.

def only_a(strlist):
    alist = []
    for i in strlist:
        if 'a' in i:
            alist.append(i)
    return alist
                
#6 Write a function called odd_couple that takes a list and returns a list.
#It:
#Returns a list with the first two odd numbers of the input.
#Returns a list with only one odd number if the input is only one odd number.
#Returns an empty list if the input has no odd numbers

def odd_couple(input):
    newlist = []
    counter = 0
    for num in input:
        if num % 2 != 0:
            newlist.append(num)
            counter += 1
        if counter == 2:
            return newlist
    return newlist

#7 Write a function called overachiever which takes in a list of lists. 
# The sublists contain both a name (string) of a student followed by a float representing his/her/their average for the class. 
# Return the name of the student with the highest exam score.
'''
def overachiever(listoflist):
    highest = 0.0
    name = ''
    for ls in listoflist:
        if (ls[1] > highest):
            highest = ls[1]
            name = ls[0]
    return name
   ''' 
def overachiever(s_list):
  name = ''
  high_score = 0.0 
  for record in s_list:
    if(record[1] > high_score):
      high_score = record[1]
      name = record[0]
  return name          
    


students = [
  ['Maria', 91.5],
  ['George', 47.3],
  ['Anquan', 94.0],
  ['Lucia', 89.2]
]    
overachiever(students)

#8.Write a function called absolute_total which takes in a list of integers. 
# return the sum of the absolute value of each element.

def absolute_total(listint):
    newList = []
    total = 0
    for num in listint:
        newList.append(abs(num))
    for absnum in newList:
        total = total + absnum
    return total

#9.Write a function called sum_of_cubes which takes in a list of integers. return the sum of the cubes of each element.

def sum_of_cubes(listint):
    newList = []
    total = 0
    for num in listint:
        newList.append(num * num * num)
    for cubesum in newList:
        total += cubesum
    return total


#10. Write a function called multiply_by_index which takes in a list of integers. return the sum of the elements multiplied with their list indices. 
# HINT: Loop into the enumerate() function for looping with both access to the element and the index.

def multiply_by_index(listint):
    total = 0
    for idx, num in enumerate(listint):
        total = total + (idx*num)
    return total




    

