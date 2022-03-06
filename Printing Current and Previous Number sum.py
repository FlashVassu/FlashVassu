print ("Printing current and Previous number sum in a range (10)")
previous=0
current=0
for x in range (11):
    current=x
    sum1=previous+current    
    print("Current Number = "+ str(current)+ " Previous Number = "+ str(previous)+ " Sum= "+ str(sum1))
    previous=current
