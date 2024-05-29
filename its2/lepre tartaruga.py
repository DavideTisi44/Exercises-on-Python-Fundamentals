import random

def printPositions(ptur,phar):
    
    l=["-"]*70

    if ptur!=phar:
        
        l[ptur-1] = "T"
        l[phar-1] = "H"

    else:

        l[phar-1] = "OUCH!!!"

    return l


def turtleMove(n,pos):

    if 1 <= n <= 5:
        
        return pos+3
    
    if 6 <= n <= 7:
        
        if pos>6:
         
            return pos-6
        
        else:

            return 1
        
    if 8 <= n <= 10:
        
        return pos+1
    
def hareMove(n,pos):

    if 1 <= n <= 2:
        
        return pos
    
    if 3 <= n <= 4:
        
        return pos+9
    
    if n == 5:

        if pos>12:
            
            return pos-12
        
        else:
            
            return 1
    
    if 6 <= n <= 8:
        
        return pos+1
    
    if 9 <= n <= 10:
        
        if pos>2:
            
            return pos-2
        
        else:

            return 1

ptur = 1
phar = 1   

while True:

    n=random.randint(1,10)

    ptur=turtleMove(n,ptur)
    phar=hareMove(n,phar)

    if ptur<70 and phar<70:

        print(printPositions(ptur,phar))

    elif ptur>=70 and phar>=70:

        print("IT'S A TIE")

        break

    elif ptur>=70:

        print("TORTOISE WINS || VAY!!!")

        break

    else:
        print("HARE WINS || YUCH!!!")

        break
