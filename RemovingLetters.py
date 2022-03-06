def remove_chars(stringToModify,charsToRemove):
    print("will remove " + str(charsToRemove) + " characters from string"  + stringToModify)
    strLen = len(stringToModify)
    
        
    if (charsToRemove < 0) :
         print("charsToRemove should be more than the string length!")
         return
         
    if (charsToRemove > strLen) :
        print("charsToRemove should be less than the string length!")
    #Home work for vassu. Need to check if the value of charsToRemove is -ve and print appropriate warning
    else:
        print("The modified string is " +stringToModify[charsToRemove:])

remove_chars('pynative',-1 )

