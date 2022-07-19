###########################some functions
########################################################################################################################################################################
##########function for checking if inputs are numbers, returns input values does not change the value inside the inputs when returning x,y


def checkifnumber(x,y):
    numbers="0123456789"
    somelist_x=[]
    checkinglist_x=[]
    somelist_y=[]
    checkinglist_y=[]

    for i in x:
        somelist_x.append(i)
        if i in numbers:
            print("x:")
            print(i+" is a number\n")
            checkinglist_x.append(i)
        else:
            print("x:")
            print(i+" is not number")
            break
    for i in y:
        somelist_y.append(i)
        if i in numbers:
            print("y:")
            print(i+" is a number\n")
            checkinglist_y.append(i)
        else:
            print("y:")
            print(i+" is not number")
            break
    if len(somelist_x)==len(checkinglist_x):
        print("\n\n")
        print("x: "+x+" is a number")
    else:
        print("\n\n")
        print("x: "+x+" is not a number")
    if len(somelist_y)==len(checkinglist_y):
        print("\n\n")
        print("y: "+y+" is a number")
    else:
        print("\n\n")
        print("y: "+y+" is not a number")
    return x, y
  
  #for testing this function try:
  test=input("x"), input("y")
  checkifnumber(test[0],test[1])
  print(test)
    
#################################################################################################################################################################
