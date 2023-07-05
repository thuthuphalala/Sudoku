import time


def printing():
    for i in soduko:
        print (i)

################################################################################################################################
        
def safe(value, r, c):
    
    for i in range(0,9):
        
        if soduko[r][i] == value:
            return False
    
    for i in range(0,9):
        
        if soduko[i][c] == value:
            return False

    rstart = (r//3)*3
    cstart = (c//3)*3
    
    for i in range(rstart,rstart+3):
        for j in range(cstart,cstart+3):
            if soduko[i][j]== value:
                return False
    return True

##################################################################################################################################

def dfs():

    start = time.time() * 1000
    stack = []                                                                  # stacks, arrays needed for the program
    visited = []
    flag = True                                                                 # flag needed to control loops
    status = True
    b = False
    z = 1
    reserve = []
    states = 0
    
    for x in range(0,9):
        for y in range (0,9):
            
            if soduko[x][y] == 0:              
                while status == True :
                    states += 1
                    if safe(z, x, y) == True:
                                                                                # after passing safe function the value gets added to soduko,
                        soduko[x][y] = z
                        stack.append([x,y,z])                                   # forward check list and stack to keep track of nodes we have visited
                        z = 1
                        
                        if not visited :                                        # here we checking no value that was backtracked is left without a value
                            status = False                                      # if the visited stack is populated i populate those nodes before proceeding
                        else:
                            data = visited.pop()
                            x, y  = data
                            continue
                        #status = False
                    else:
                        z += 1
                        while z > 9:                                            # the backtracking process begins
                                visited.append([x,y])                           # keep track of nodes that were visited so we can go back too them later
                                values = stack.pop()                            # getting the previous nodes values
                                x, y , z = values
                                soduko[x][y] = 0
                                z += 1
                                
                                
                                status = True
                        flag = True
                status = True

    end = time.time() * 1000
    runTime = end - start
    print(" Depth-First Search execution Time: ",runTime)
    print("Nodes generated: ",states)
##################################################################################################################################

def forwardCheck():

    start = time.time() * 1000
    stack = []                                                  # stacks, arrays needed for the program
    visited = []
    status = True                                               # flag needed to control loops
    z = 1
    reserve = []
    fixValues = []
    node = 0


    for i in range(0,9):                                       # identifying all the fixed values of the soduko
        for o in range(0,9):                                   # and add them to fixValues array
            if soduko[i][o] > 0:
                fixValues.append([i,o])
    
    for x in range(0,9):
        for y in range (0,9):

            if [x,y] in fixValues:                              #Adds the fixed values on the soduko in the forward check list
                reserve.append(soduko[x][y])
                continue

            while z in reserve:                                 #check if the value isnt in forward check list, if its in it is not parsed through
                    z += 1                                      #only remaining values will be sent through
            
            if soduko[x][y] == 0:              
                while status == True :
                    node += 1
                    if safe(z, x, y) == True:
                        
                        soduko[x][y] = z                        # after passing safe function the value gets added to soduko,                         
                        reserve.append(z)                       # forward check list and stack to keep track of nodes we have visited 
                        stack.append([x,y,z])
                        z = 1

                        if y == 8:                              # when the end of array is reached the reserve list is reset
                            reserve = []
                        
                        if not visited :                        # here we checking no value that was backtracked is left without a value
                            status = False                      # if the visited stack is populated i populate those nodes before proceeding
                        else:
                            tempX = x
                            data = visited.pop()
                            x, y  = data
                            if tempX < x:
                                reserve = []
                            continue

                    else:
                        z += 1
                        while z > 9:                            # if value reaches over 9 it means no value can be assigned
                                tmpX = x                        # the backtracking process begins
                                visited.append([x,y])           # keep track of nodes that were visited so we can go back too them later
                                values = stack.pop()            # getting the previous nodes values 
                                x, y , z = values
                                  
                                soduko[x][y] = 0
                                if tmpX > x:                        # comparing X to determine if program has backtracked to different row
                                    reserve = [1,2,3,4,5,6,7,8,9]   # so we can assign reserve with all values since the row is populated
                                reserve.remove(z)
                                z += 1
                                while z in reserve:                 # forward checking and removing it from being considered
                                    z += 1
                                
                                
                                status = True
                status = True              
        reserve = []               
    end = time.time() * 1000
    runTime = end - start
    print(" Forward Checking execution Time: ",runTime)
    print("Nodes generated: ",node)               

                        
##################################################################################################################################
    return False
if __name__=="__main__":

    print("Please enter a file name for Depth-First search")
    file = input()
    matrix = open(file)
    soduko = []

    for line in matrix:
        soduko.append(line.split())

    for x in range(0,9):
        for y in range (0,9):
            soduko[x][y] = int(soduko[x][y])

    dfs()
    printing()


    print("Please enter a file name for Forward Checking")
    file = input()
    matrix = open(file)
    soduko = []

    for line in matrix:
        soduko.append(line.split())

    for x in range(0,9):
        for y in range (0,9):
            soduko[x][y] = int(soduko[x][y])    

    forwardCheck()
    printing()
