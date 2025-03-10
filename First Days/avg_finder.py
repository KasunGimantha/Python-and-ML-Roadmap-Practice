original_list = [] #declare original list

for x in range(5): #loop untill 5 inputs 
    input_item = input("Enter number to add to list(up to 5 numbers)") #store inputs inside input_item as a items
    original_list.append(int(input_item)) #append items into original_list
    
def calculate_average(num_list): #declare function adding a parameter
    
    if num_list:
        summ = sum(num_list)  #calculating sum
        avg = summ/len(num_list) #calculating average
        print(avg) 
    else:
        print("Null List!!")

calculate_average(original_list) #passing inputed list to function
