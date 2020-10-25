long_string = "accenture argentina" 
count = {}

for letter in long_string :
    if letter in count.keys() :  
	    count[letter] += 1
    else:
        count[letter] = 1

print ("I found the following  letters")  
print (str(count))

