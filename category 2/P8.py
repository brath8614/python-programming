string = input("Enter the string:")
string=string.lower()
repeat=[]
print("Duplicate characters in a given string: ");  
#Counts each character present in the string  
for i in range(0, len(string)):  
    count = 1
    
    for j in range(i+1, len(string)):
        
        if(string[i] == string[j] and string[i] != ' '):  
            count = count + 1;
            
            #Set string[j] to 0 to avoid printing visited character  
            string = string[:j] + '0' + string[j+1:]  
   
    #A character is considered as duplicate if count is greater than 1  
    if(count > 1 and string[i] != '0'):
        repeat.append(string[i])
        print(string[i],count)
        
print("Number of repeated characters:", len(repeat),repeat)
