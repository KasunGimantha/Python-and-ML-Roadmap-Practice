# Challenge 1: Write a function that:

# Accepts any number of integers

# Returns the sum, average, and max value

# Use *args to handle input

        
def any_num(*args):
    
    if not args:
        return None
    else:
        sum_val = sum(args)
        average = sum(args)/len(args)
        max_value = max(args)
        
        output = {'sum':sum_val,'average':average,'max':max_value}
        
        return output
    

print(any_num(4,1,2,3,6,8))
