while True: # creating infinite loop
    userinput=input("Enter date in either (mm/dd/yyyy) or (month date, year) format:")#taking input from user
    splitting=userinput.split()#splitting it to seggregate wether the format is in mm/dd/yyyy or month date, year
    if len(splitting) == 1:# if the user input is in mm/dd/yyyy format
        if '/' in userinput:# making sure its in the correct format
            l = userinput.split('/')#splitting it by / to get date month and year seperatly
            month1=l[0]#making variables and assigning values for month date and year
            date1=l[1]
            year1=l[2]
            if len(year1)==4 and len(date1)<=2 and len(month1)<=2 and 0<=int(date1)<=31 and 0<=int(month1)<=12 and int(year1)>0:#making sure that they dont violate basic date parameters.
                print(year1+'/'+month1+'/'+date1)# putting them in the correct format (yyyy/mm/dd) and printing them
                break#breaking loop if we get correct output
            else:
                print("invalid date format try again.")
        else:
            print("invalid date formt try again.")
    elif len(splitting)==3:# if user input is in month date, year format.
        splitting=userinput.split( )#splitting the input to get individual month, date and year.
        month=splitting[0].upper()#isolating month and making it into upper case to match the dictionary below 
        date1=splitting[1]#isolating the date
        finaldate=date1[0]#removing comma


        thisdict =	{           #dictionary to correspond months with their respective numbers
        "JANUARY": 1,
        "FEBUARY": 2 ,
        "MARCH": 3,
        "APRIL":4,
        "MAY":5,
        "JUNE":6,
        "JULY":7,
        "AUGUST":8,
        "SEPTEMBER":9,
        "OCTOBER":10,
        "NOVEMBER":11,
        "DECEMBER":12
        }
        if len(splitting)==3 and month in thisdict and len(finaldate)<=2 and len(splitting[2]) == 4 and 0<=int(finaldate)<=31 and int(splitting[2])>0:#making sure they dont violate basic date paramenters
            print(splitting[2]+'/'+str(thisdict[month])+'/'+finaldate)# putting them in the correct format (yyyy/mm/dd) and printing. pulling the value of the month from the dictionary.
            break# breaking loop when we get the correct output
        else:
            print("invalid date format try again.")
    else:
        print("invalid date fromat try again.")
