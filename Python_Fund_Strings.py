#5.Strings: In Depth 
#Exercise MathyFunctions 

#1
def first_letter(input):
    return input[0]

#2
def last_three(input):
    return input[-3:]

#3
def char_count(single_char,full_string):
    count = 0
    
    for c in full_string.lower():
        if c == single_char:
           count = count + 1
            
       
    return count

#4
def remove_vowels(phrase):
    vowels = ('a','e','i','o','u')
    return_val = ""
    for c in phrase:
        if c.lower() not in vowels:
            return_val += c
    return return_val


        
#5
def hello_goodbye(name,num):
    if num == 1:
        return ("Hello, " + name)
    elif num == 2:
        return ("Goodbye, " + name)

#6
def spooky(boo):
    spookyboo = ''
    boo.lower()
    for idx, ch in enumerate(boo):
        if idx % 2 == 0:
            spookyboo = spookyboo + ch
        else:
            spookyboo = spookyboo + ch.upper() 
    return spookyboo


#7
def initials(full_name):
    name_initials = ''
    name_initials = full_name[0]
    for index, c in enumerate(full_name):
        if c == ' ':
            name_initials = name_initials + full_name[index+1]
    return name_initials


#8
def mixup(name1,name2):
    name1_letter = name1[0]
    name2_letter = name2[0]

    return name2_letter + name1[1:] +" "+ name1_letter + name2[1:]
    

def mixupextended(name1,name2,num=1):  #num=1 makes it a deafult argument which means it will default to 1 if no argument is passed
    name1_letter = name1[0:num]
    name2_letter = name2[0:num]

    return name2_letter + name1[1:] +" "+ name1_letter + name2[1:]

#9
def not_bad(string):
    not_index = string.find('not')
    bad_index = string.find('bad')
    string = string[0:not_index] + 'good' + string[bad_index + 3:]
    return string

#10
def h4cker_sp33k(string):

    new_string = string
    new_string.lower()
    new_string = new_string.replace('a','4')
    new_string = new_string.replace('e','3',len(string))
    new_string = new_string.replace('l','1',len(string))
    new_string = new_string.replace('t','+',len(string))
    return new_string


#11
def same_x_and_o(str):
    count_x = 0
    count_y = 0
    for i in str:
        if i == 'x':
            count_x += 1
    for i in str:
        if i == 'o':
            count_y += 1
    if count_x == count_y:
        return True
    else:
        return False

print(same_x_and_o("xxxxooo"))
            



    
            
        
    