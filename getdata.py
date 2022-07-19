#sometestdatafromGjergjFrate

data=((2008,"anton"),(2009,"kurac"),
      (2060,"frute"),
      (2042,"parisgagné"),
      (2030,"fauci"))


manipulateddata=((2008,"anton"),
                (2009,"fauci"),
                (2060,"anton"),
                (2042,"parisgagné"),
               (2030,"fauci"))

def getdata(somedata):
    """takes your data and assigns the first part of the tuple inside the big tuple to numbers and the second half to names
        -->assumes that part I is int and part II is str"""
    numbers=()
    names=()
    for i in somedata:
        numbers=numbers+(i[0],)
        if i[1] not in names:
            names=names+(i[1],)
    min_numbers=min(numbers)
    max_numbers=max(numbers)
    different_names=len(names)
    return (min_numbers,max_numbers,different_names)

########for testing function type
sorteddata=getdata(data)

print ("\ngetdatafunction gives you:\n"),print(sorteddata)
print ("From "+str(sorteddata[0])+" to "+str(sorteddata[1])+" there are "+str(sorteddata[2])+ " different names")

sorteddate_1=getdata(manipulateddata)
print ("\ngetdatafunction gives you:\n"),print(sorteddate_1)
print ("From "+str(sorteddate_1[0])+" to "+str(sorteddate_1[1])+" there are "+str(sorteddate_1[2])+ " different names")
