import random
def gameWin(comp,you):
    if comp==you:
           return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True        
                        
                                           




randNo=random.randint(1,3)

if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp="g"
        
print(" Computer Turn:Snake(s) water(w) or Gun(g)?")
you=input(" Your Turn:Snake(s) water(w) or Gun(g)?")
a=gameWin(comp,you)
print(f"Computer choose: {comp}")
print(f"You choose: {you}")
 
if a==None:
    print("The game is tie!")
elif a:
    print("You win")
else:
    print("You lose!")        