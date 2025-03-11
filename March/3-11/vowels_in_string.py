# count the number of vowels in a given string.

def count_vowels(input_string):  # intializing function
    count = 0
    vowels = "aeiouAEIOU"  # intialized vowels

    for x in input_string:  # loop through sliced list
        if x in vowels:  # loop through vowel list
            count += 1  # increment count by one
    return count  # return total count


print(count_vowels("AAuunana"))
