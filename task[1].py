#Task One
counter = 0
tries = 4
while tries > 0:
    num = input("Please, Enter The Number\n").strip()
    if num.isdecimal():
        for n in num:
            counter += 1
        print(counter) 
        break      
    else:
        if tries > 1:
            tries -= 1
            print(f"{tries} trials are Remaining. please, Enter Number Not String. ")
        else:
            print("Unfortunately , Your Trials Are Finished")
        
        









