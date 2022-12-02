
                                    # DICE ROLLING GAME #
            

'''This is the programm to find the output when a dice is rolled.And if the input given by the user
matches whith the random output then it will print "HURRAY".'''


import random
x="y"
while x=="y":
    a=random.randint(1,6)
    b=int(input("Enter the Predicted Value"))
    if a==1:
        print("[---------]")
        print("[         ]")
        print("[    0    ]")
        print("[         ]")
        print("[---------]")
        if b==1:
            print("!!!HURRAY!!!")
            print("Predicted Value Matched")
    elif a==2:
        print("[---------]")
        print("[ 0       ]")
        print("[         ]")
        print("[       0 ]")
        print("[---------]")
        if b==2:
            print("!!!HURRAY!!!")
            print("Predicted Value Matched")
    elif a==3:
        print("[---------]")
        print("[         ]")
        print("[ 0  0  0 ]")
        print("[         ]")
        print("[---------]")
        if b==3:
            print("!!!HURRAY!!!")
            print("Predicted Value Matched")
    elif a==4:
        print("[---------]")
        print("[ 0     0 ]")
        print("[         ]")
        print("[ 0     0 ]")
        print("[---------]")
        if b==4:
            print("!!!HURRAY!!!")
            print("Predicted Value Matched")
    elif a==5:
        print("[---------]")
        print("[0       0]")
        print("[    0    ]")
        print("[0       0]")
        print("[---------]")
        if b==5:
            print("!!!HURRAY!!!")
            print("Predicted Value Matched")
    elif a==6:
        print("[---------]")
        print("[ 0  0  0 ]")
        print("[ 0  0  0 ]")
        print("[ 0  0  0 ]")
        print("[---------]")
        if b==6:
            print("!!!HURRAY!!!")
            print("Predicted Value Matched")
    r=input("Do You Want To Continue The Game(Y/N)")
    r=r.lower()
    if r=="y":
        x=r
    elif r=="n":
        print("GAME ENDED")
        x=r
    else:
        print("Enter Only Y or N")
        
        
        
        
    

    
