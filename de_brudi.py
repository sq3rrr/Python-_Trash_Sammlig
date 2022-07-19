print ("""REGLE: JEDES MOL WENN DE PLUG PSYCHT WIRD ERHÖHT SICH SIN STRESSLEVEL""")



asking = input("PLUG: eh, was hesh du gfühl was do lauft? sneg odo normal?: ")
stresslevelvojefe = 0

for i in asking:
    while asking == "sneg" or asking =="wisse" or asking == "cola" or asking == "belo":
        print ("PLUG: nei brate solauft da do nö")
        stresslevelvojefe += 1
        asking = input("PLUG: eh, was hesh du gfühl was do lauft? sneg odo normal?: ")


    while asking == "normal" or asking == "weed" or asking == "kush" or asking == "standard":
        break


    else:
        asking = input("PLUG: eh, was hesh du gfühl was do lauft? sneg odo normal?: ")
if stresslevelvojefe >=10:
    print ("Stresslevel vo Plug: "+str(stresslevelvojefe))
    print ("""DE PLUG ISCH ZU GSTRESST BITTE CHILL""")
else:
    print ("PLUG: Bro max paras weg sneg do lauft nur normal")
    print ("Stresslevel vo Plug: "+str(stresslevelvojefe))


kunde = input ("PLUG: ok ez zeg wer bisch du?_ ")

if kunde == "Elhan" or kunde == "elhan" or kunde == "Edon" or kunde == "edon":
    stresslevelvojefe+=1
    print ("PLUG: Nei alte wa lauft ez do jungs.. solauft da nöd ")
    print (kunde + " Shko në shtëpi. M'u sos durimi.")


print ("PLUG: "+kunde +  "! ,frate, leido hemo nume chline huet, sory")

oha = input("PLUG: Dini optione frate sind: fufi , 20er ------- Bitte schrib wele du wilsch,< fufi >,< 20er>  :\n__: ")

for i in oha:
    if oha == "20er":
        print ("oha max broker")
        stresslevelvojefe += 1
        break


    elif oha == "fufi" or oha == "fu" or oha == "fuf":
        print ("PLUG: geil " + kunde + " , frate so laufts")
        break

    else:
        oha = input("PLUG: Dini optione frate sind: fufi , 20er ------- Bitte schrib wele du wilsch,< fufi >,< 20er>  :\n__: ")


print ("PLUG: oha")


if stresslevelvojefe <= 3:
    print ("PLUG: Mit dir isch chillig chash gern wieder cho.")
else:
     print ("PLUG: "+ kunde + " mit dir schaffe isch ghetto min stresslevel ish " + str(stresslevelvojefe)+ "! ! !")

print ("PLUG: eh tschau " + kunde + " ! ! ! ")
