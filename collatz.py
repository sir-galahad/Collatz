numbers={}

def printSequence(start):
    while start > 1 :
        print(f"{start} -> ",end='')
        start=numbers[start]
    print("1.0")

def collatz(start):
    testNum=start
    tmp={}
    
    while(testNum not in numbers and testNum not in tmp):

        if(testNum % 2 == 0):
            nextNum = testNum / 2
        else :
            #nextNum = testNum * 3 + 1
            nextNum = testNum * 1.5 + 0.5
            
        tmp[testNum]=nextNum
        testNum=nextNum
        
    if(testNum in numbers): # if testNum is in numbers then the sequence must go to 1
        numbers.update(tmp)
        if(start % 1000000 == 0):
            print(f"{start} checked")
            printSequence(start) # just to prove that the math is right
        return True
    
    else: # otherwise testNum was in tmp meaning we found a circular sequence
        print(f"Holy shit we solved collatz: {start}")
        return False

            
#initialize 1,2,4    

numbers[1.0] = 4.0
numbers[2.0] = 1.0
numbers[4.0] = 2.0

#start at 3 the first gap in our sequences
start = 3.0

while collatz(start):
    start += 1
    
