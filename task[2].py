#Task 2
numInput = input("Enter Your HEX Number, please.\n")
num = numInput[2:]
#print(f"num = {num}")
if num[0] == 'A' or num[0] =='a':
    n1 = "10"   
elif num[0] == 'B' or num[0] =='b':
    n1 = "11"  
elif num[0] == 'C' or num[0] =='c':
    n1 = "12"  
elif num[0] == 'D' or num[0] =='d':
    n1 = "13"      
elif num[0] == 'E' or num[0] =='e':
    n1 = "14"    
elif num[0] == 'F' or num[0] =='f':
    n1 = "15"     
else:
    n1 = num[0]
#print(f"n1 = {n1}")
if num[1] == 'A' or num[1] =='a':
    n2 = "10"   
elif num[1] == 'B' or num[1] =='b':
    n2 = "11"  
elif num[1] == 'C' or num[1] =='c':
    n2 = "12"  
elif num[1] == 'D' or num[1] =='d':
    n2 = "13"      
elif num[1] == 'E' or num[1] =='e':
    n2 = "14"    
elif num[1] == 'F' or num[1] =='f':
    n2 = "15" 
else:
    n2 = num[1]
#print(f"n2 = {n2}")
x = bin(int(n1)) + bin(int(n2))
y = x[2:6]
z = x[8:]
print(y + z)
