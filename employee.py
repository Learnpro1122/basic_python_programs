# function  to add a entry in the file  
def add_entry():
    f = open('employee.txt', 'a+')

    name = str(input('enter your name: '))
    dept = str(input('enter your department: '))
    age = int(input(('enter your age: ')))
    
    #getting the token number
    with open('employee.txt','r+') as f:
        a = len(f.readlines()) 
        token = a + 1 

    list_e = [token,name,age,dept]

    #setting cursor to new line     
    # write the values to line
    with open('employee.txt' , 'a+') as f:
        f.write(str(list_e))
        f.writelines('\n')



# function to delete a entry 
def del_entry():
    print('''
          you choose to delete your entry....
          please enter your token number....
          ''')
    line_number = int(input('enter the token number: '))
    with open('employee.txt', 'r') as file:
        lines = file.readlines()
    
    if line_number <= 0 or line_number > len(lines):
        print(f"Line {line_number} is out of range. The file has {len(lines)} lines.")
        return
    
    # Replace the specific line
    lines[line_number - 1] = 'this line is deleted.' + '\n'

    #writing the line
    with open('employee.txt', 'w') as file:
        file.writelines(lines)




#edit a entry
def edit_entry():
    #getting token number and seting  cursor to that line
    print('you choosed to edit a entry...')
    line_number =  int(input('enter your token number:  '))
    with open('employee.txt', 'r') as file:
        lines = file.readlines()
    if line_number <= 0 or line_number > len(lines):
        print(f"Line {line_number} is out of range. The file has {len(lines)} lines.")
        return
    
    #puting  the line into a a variable
    line_str =lines[line_number - 1].replace('\n' , '') 
    list_str = list(line_str.split(','))

    print('''
            here are your values for token number {token}:
            1)name : [{name}]
            2)age : [{age}]
            3)department: [{dept}       
            '''.format(token = line_number , name = list_str[1] , age = list_str[2],dept = list_str[3]))
    
    #which value to be edited name,age,department and swaping the old value with updated one
    value_e = int(input('enter the value to be edited(only numeric value): '))
    match value_e :
        case value_e if value_e == 1:  
            value = str(input('enter the new name: '))
            list_str[1] = value
        case value_e if value_e == 2 :
            value = int(input('enter the new age: '))
            list_str[2] = value
        case value_e if value_e == 3:
            value = str(input('enter the new department: '))
            list_str[3] = value  
    print('here are your new values:' ,list_str[0]+','+ list_str[1]+',', list_str[2],','+ list_str[3])

    #setting the new list with updated values
    new_list_str = [int(list_str[0].replace('[','')),list_str[1].replace("'",''),int(list_str[2]),list_str[3].replace(']','')] 

    #converting list into str and adding newline charcter to set the cursor to next line 
    str_list = str(new_list_str) 
    lines[line_number-1] = str_list + '\n'

    with open('employee.txt', 'w') as file:
        file.writelines(lines)
    

#getting values from the user to do particular add,delete,edit a entry
print(
      '''
      thank you for choosing this program
      enter the fucntion you intent to do........
      here are your choices : 
      1.)add a entry 
      2.)edit a entry
      3.)delete a entry 

      enter only numeric value as defined.
      ''')
action  = input('enter your action: ')
match action : 
    case 'edit a entry' | '2':
        edit_entry()
    case 'delete a entry' | '3':
        del_entry()
    case 'add a entry' | '1':
        add_entry()