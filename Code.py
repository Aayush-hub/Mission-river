import webbrowser
url = 'https://indiawris.gov.in/wris/#/SWQuality'
print("Url: ",url)
print("0: Enter 0 to see data!")
print("1: Enter 1 to analyze data!")
a = int(input())
if a == 0:
    webbrowser.open_new(url)
elif a == 1:
    print("Class A: Total coliforms less than or equal to 50, ",
    "pH : 6.5-8.5, ","Dissolved Oxygen 6mg/l or more, ",
    "Biochemical Oxygen Demand 5 days 20^C, 2mg/l or less")
    print("Class B: Total Coliforms 500 or less, ",
    "pH : 6.5-8.5, ", "Dissolved Oxygen 5mg/l or more, ",
    "Biochemical Oxygen Demand 5 days 20^C, 3mg/l or less")
    print("Class C: Total Coliforms 5000 or less, ",
    "pH : 6-9, ","Dissolved Oxygen 4mg/l or more, ","Biochemical Oxygen Demand 5 days 20^C, 3mg/l or less ")
    print("Class D: pH : 6.5-8.5, ","Dissolved Oxygen 4mg/l or more, ","Free Ammonia (as N), ",
    "Biochemical Oxygen Demand 5 days 20 ^C, 2mg/l or less")
    print("Class E: pH : 6.0-8.5, ","Electrical Conductivity at 25 ^C micro mhos/cm, maximum 2250, ",
    "Sodium absorption Ratio Max. 26, ","Boron Max. 2mg/l")
    b = input("Enter class of your water quality: ").upper()
    if (b == "A"):
        print("***Drinking Water Source without conventional treatment but after disinfection***")
        print("Solution: Boil water or filter it through fine cloth")
        print ("Uses: Clothes washing, closed system toilet flushing, garden watering and firefighting. It can be used to irrigate food crops that consumed raw or sold to consumers uncooked or processed")
    elif(b == "B"):
        print("***Outdoor bathing (Organised)***")
        print("Solution: Clorination , boiling, Bio-sand filteration")
        print("Uses: Irrigate sports fields, golf courses and dairy cattle grazing land.It can also be used for industrial wash down ")
    elif(b == "C"):
        print("***Drinking water source after conventional treatment and disinfection***")
        print("Solution: Coagulation , Desalination , Sedimentation")
        print("Uses: used for a number of uses including for cooked or processed human food crops including wine grapes and olives.  It can also be used for livestock grazing and fodder and for human food crops grown over a meter above the ground and eaten raw such as apples, pears, table grapes and cherries.  It can be used by councils for specific purposes but there are restrictions around human contact. ")
    elif (b == "D"):
        print("***Propagation of Wild life and Fisheries***")
        print("Solution: Softning , Aeration")
        print("Uses: Used for non-food crops such as instant turf, woodlots and flowers")
    elif (b == "E"):
        print("***Irrigation, Industrial Cooling, Controlled Waste disposal***")
        print("Solution: Membranes ,Adsorption")
        print("Uses: Only for industry cooling and waste disposal")
    else:
        print("Please enter valid type!")  
else:
    print("You entered wrong choice!")
