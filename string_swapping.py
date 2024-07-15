'''
a function to print the combinations of the given string input by the user. 

algorithm or logic:
            the swapping will be started from the last and last 2nd character.
            and will go on till the first and second charcater,
            and will stop when the original string will be combined again...
ACB
CAB
CBA
BCA
BAC
ABC         
'''


# ask for string and convert the string into the list for easy swapping 
string = str(input('enter the string: '))
list_o = list(string)

#index variable for the string 
no = len(list_o) 
print(no)

# factorial will be needed as to print combindations factorial time.
fact =  1
for i in range(1, no+1):
    fact = fact * i
print(fact)
# variable for changing the index of the charcter that is to be swap...
n = 1

print(list_o[no-n-1])
# swapping from last 
for k in range(fact):
    for i in list_o:     
        list_o[no-n-1] , list_o[no-n] = list_o[no-n] ,list_o[no-n-1] 
        n = n + 1
        print(list_o)
        if n ==  no :
            n = 1
        break

