
# coding: utf-8

# In[ ]:

height = [ [0,1,1,0], [0,1,1,0], [0,1,1,0], [0,1,1,0], [0,1,1,0] ] 

isBlue = [ [False,False,False,False], [False,False,False,False], 
        [False,False,False,False], [False,False,False,False],
        [False,False,False,True] ] 

isOn = [ [False,False,False,False], [False,False,False,False], 
        [False,False,False,False], [False,False,False,False],
        [False,False,False,True] ] 


x = 0 
y = 0 
yon = 0 
direction = { 0:'north', 1:'east', 2:'south', 3:'west' }

maxX = len(height)-1 
maxY = len(height[0])-1
    
def heightDifferenceForward():
     if yon == 0 and y<maxY:
        return height[x][y+1] - height[x][y] 
     elif yon == 1 and x<maxX:
        return height[x+1][y] - height[x][y] 
     elif yon == 2 and y>0:
        return height[x][y-1] - height[x][y] 
     elif yon == 3 and x>0:
        return height[x-1][y] - height[x][y] 
     else:
        return 0

komut = ""
while  komut != "q":
    print ("Enter a command for lbot:")
    komut = input()
    
    if komut == ">": 
        print ("I am turning right.")
        yon = (yon+1)%4

    elif komut == "<": 
        print ("I am turning left.")
        yon = (yon-1)%4
                
    elif komut == "^": 
        print ("I am moving forward.")
        if yon == 0 and y < maxY: 
                y = y+ 1
        elif yon == 1 and x < maxX:
                x = x + 1                  
        elif yon == 2 and y > 0:                     
                y = y - 1
        elif yon == 3 and x > 0:
                x = x - 1

    elif komut=="@":
        if (isBlue[x][y] == True):
            print ("I am switching on or off.")
            if (isOn[x][y] == True):
                isOn[x][y] == False
            else:
                isOn[x][y] = True
        else:
            print("You are trying to light up a gray box. I cannot do it.")

    elif komut != "q":
            print("This command is not known.")
        
print("As I exit now, my orientat,on is ",direction[yon])


# In[ ]:



