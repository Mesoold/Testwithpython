isused = True
while (isused == True):
    n0 = 0
    n1 = 1
    sum = 0
    print("------------------------------------------------------")
    print("-------------Fibonacci number---------------")
    print("-------------MAIN MENU---------------")
    nterm = int(input("What many terms? : "))
    if nterm <= 0 :
        print("plase enter a positive integer")
        continue
    elif nterm == 1 :
        sum = n1
        print("F",nterm,"is",n1)
    else :
        sum = n0
        print("Fibonacci sequence : ")
        for i in range(2,nterm+1, 1) :
            print(n1)
            sum = n0+n1
            n0 = n1
            n1 = sum
        print("F",nterm,"is",sum)
    Back_mainmenu = str(input("Back to main menu [y/n]"))
    if Back_mainmenu == 'y' or Back_mainmenu == 'Y':
        print ("Loading....")
        continue
    elif Back_mainmenu == 'n' or Back_mainmenu == 'N':
        print("EXIT ....") 
        isused = False
        exit(0)
    else :
        print("Please enter [y back to main meun/n Exit]") 
        continue