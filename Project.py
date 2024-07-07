

import csv
import random
import sys
import pandas as pd
region = None
i = 1
date = []
while i <= 31:
           date.append(i)
           i+=1
ADMINS_FILE = open ("project/Admins.csv","r")
check =input ("Are You 'Admin' or 'User'?\n").lower()
while True:
    if (check == 'admin'):
            def ADMIN ():
                    
                    ID =  input ("Enter Your ID: ")
                    Name = input ("Enter Your name: ")
                    Email = input ("Enter Your Email: ")
                    Password = input ("Enter Your Password: ")
                    while True:
                        ADMINS_FILE = open ("project/Admins.csv","r")
                        reader = csv.reader(ADMINS_FILE)
                        next(reader)
                        for row in reader:
                                if ID == row[0] and Name == row [1] and Email == row[2] and Password == row[3]:
                                        ADMINS_FILE.close() 
                                        print (f"HELLO {Name}! ")
                                        def ADE():
                                                while True:
                                                        Vaccine_Center_Check =input ("Do You Want to 'Add' or 'Delete' or 'Search' a Vaccination Centre? ('n' to exit) \n\n").lower()
                                                        if Vaccine_Center_Check == 'n':
                                                                print (f"GoodBye {Name}.")
                                                                sys.exit()
                                                        elif Vaccine_Center_Check == 'add':
                                                                Vaccine_Center_FILE = open ("project/Vaccination_Centers.csv",mode = 'a', newline = '')
                                                                Vaccine_Centre_ID =random.randint(1000, 9999)
                                                                Vaccine_Centre_Name = input ("Enter the Vaccine Centre's Name: ")
                                                                Vaccine_Centre_Address = input ("Enter the Vaccine Centre Address: ")
                                                                List_Vaccines = input ("Enter The list of Vaccines: ")
                                                                print (f"Vaccine Centre '{Vaccine_Centre_Name} ID is: {Vaccine_Centre_ID}'\n\n")

                                                                writer = csv.writer (Vaccine_Center_FILE)
                                                                
                                                                writer.writerow ([Vaccine_Centre_Name,Vaccine_Centre_ID,Vaccine_Centre_Address,List_Vaccines])
                                                                Vaccine_Center_FILE.close()
                                                                
                                                        elif Vaccine_Center_Check == 'delete' or Vaccine_Center_Check == 'del':
                                                                Vaccine_Center_FILE  = open ("project/Vaccination_Centers.csv",'r')
                                                                reader = csv.reader (Vaccine_Center_FILE)
                                                                for rows in reader:
                                                                        print (rows)

                                                                Vaccine_Center_FILE.close()

                                                                
                                                                while True:
                                                                        Vaccine_Center_FILE  = open ("project/Vaccination_Centers.csv",'r')
                                                                        reader = csv.reader (Vaccine_Center_FILE)
                                                                        Name_Removal = input ("\n\nEnter The 'Name' of The Vaccine Center You Want To Remove: \n")    
                                                                        for loop in reader:   

                                                                                if Name_Removal == loop[0]:
                                                                                
                                                                                        
                                                                                        while True:
                                                                                                REMOVE_CHECKER =input (
                                                                                                f"""\nARE TOU SURE TO REMOVE: \nID: {loop[1]}\nNAME: {Name_Removal}\nADDRESS: {loop[2]}\nVACCINE: {loop[3]}?\n(y , n)\n"""
                                                                                                ).lower()
                                                                                                if REMOVE_CHECKER == 'y':

                                                                                                        df = pd.read_csv('project/Vaccination_Centers.csv', index_col= 'NAME')
                                                                                                        df = df.drop(Name_Removal)
                                                                                                        df.to_csv('project/Vaccination_Centers.csv', index=True)
                                                                                                        print (f"{Name_Removal} Center Has Been Removed..\n\n")
                                                                                                        ADE()
                                                                        

                                                                                                elif REMOVE_CHECKER == 'n':
                                                                                                        print ("THE OPERATION HAS BEEN CANCELED..")
                                                                                                        sys.exit()

                                                                                                else:
                                                                                                        print ("\nTRY AGAIN. \n")
                                                        
                                                        elif Vaccine_Center_Check == 'search':
                                                                search1 = input ("Do You Want To Search in 'Vaccination_Centers File' or 'Users File': ").lower()
                                                                if search1 == 'vc':
                                                                        Search_Vaccine = input ("Enter The Name of The Vaccination Center You Want to Search: ")
                                                                        vaccine_search = open ("project/Vaccination_Centers.csv", 'r')
                                                                        reader_Search = csv.reader(vaccine_search)
                                                                        for search in reader_Search:
                                                                                if Search_Vaccine == search [0]:
                                                                                        print (f"id: {search [1]}\nAddress: {search[2]}\nVaccine: {search[3]}")
                                                                elif search1 == 'users':
                                                                        Users_Check = open ("project/Users.csv")
                                                                        reader_USER = csv.reader (Users_Check)
                                                                        for Search_USERS in reader_USER:
                                                                                print (Search_USERS)
                                        ADE()                                                                                                                                
                                        
                        else:
                                print ("\nTRY AGAIN.\n")
                                ID =  input ("Enter Your ID: ")
                                Name = input ("Enter Your name: ")
                                Email = input ("Enter Your Email: ")
                                Password = input ("Enter Your Password: ")
            ADMIN()
    elif (check == 'user'):
            def USERS ():   
                    
                    Acc = input ("Do You Have an Account (y , n)? ").lower()
                    if Acc == 'n':
                            
                            USER = open ("project/Users.csv",mode = 'a', newline = '')
                            print ("FILL THESE FIELD TO Register: \n\n")
                            USER_ID = random.randint(1000, 9999)

                            Name_USER = input ("Enter Your Name: ")
                            Email_USER = input ("Enter Your Email: ")
                            Password_USER = input ("Enter Your Password: ")
                            Phone_Number_USER = input ("Enter Your Phone Number: ")
                            NationaL_ID_USER = input ("Enter Your National ID: ")
                            con = random.choice(date)
                            Date =input(f"Is That Date {con}/01/2024 is Appropriate With You (y , n)? ").lower()

                            while True:
                                def agree():
                                        USER_CHECK = open ("project/Users.csv", 'r')
                                        reader = csv.reader (USER_CHECK)
                                        next (reader)

                                        for Certain in reader:
                                                if Email_USER == Certain [2] or Phone_Number_USER == Certain [4] or NationaL_ID_USER == Certain [5]:
                                                        print ("You Already Have An Appointment.")
                                                        sys.exit()
                                        USER_CHECK.close()
                                                        
                                        print (f"\nYour ID is '{USER_ID}'")
                                        
                                        writer = csv.writer(USER)
                                        writer.writerow([USER_ID,Name_USER,Email_USER,Password_USER,Phone_Number_USER,NationaL_ID_USER,f'{con}/01/2024'])
                                        USER.close()
                     
                                        print ("LOGIN For More Informations.")
                                        sys.exit()
                                if Date == 'y':
                                       agree()
                                       sys.exit()

                                elif Date == 'n':
                                        while True:
                                                con2 = random.choice(date)
                                                Date2 =input(f"Is That Date {con2}/01/2024 is Appropriate With You (y , n)? ").lower()
                                                if Date2 == 'y':
                                                  
                                                        USER_CHECK = open ("project/Users.csv", 'r')
                                                        reader = csv.reader (USER_CHECK)
                                                        next (reader)

                                                        for Certain in reader:
                                                                        if Email_USER == Certain [2] or Phone_Number_USER == Certain [4] or NationaL_ID_USER == Certain [5]:
                                                                                print ("You Already Have An Appointment.")
                                                                                sys.exit()
                                                        USER_CHECK.close()
                                                                                        
                                                        writer = csv.writer(USER)
                                                        writer.writerow([USER_ID,Name_USER,Email_USER,Password_USER,Phone_Number_USER,NationaL_ID_USER,f'{con2}/01/2024'])
                                                        USER.close()
                                                     
                                                        print (f"\nYour ID is '{USER_ID}'")
                                                        print ("LOGIN For More Informations.")

                                                        sys.exit()
                                                elif Date2 == 'n':
                                                       continue
                                                else:
                                                       print ("\nINVALID VALUE\n")

                                else:
                                       while True:
                                              con2 = random.choice(date)
                                              quest = input (f"{con}/01/2024 is Apporpriate With You (y , n)? ").lower()
                                              if quest == 'y':
                                                           print (f"\nOK You Can Get Your Vaccination At {con}/01/2024")
                                                           print (f"\nYour ID is '{USER_ID}'")
                                                           agree()
                                                           
                                        
                                              elif quest == 'n':
                                                             sideQ = input (f"{con2}/01/2024 is Apporpriate With You (y , n)? ")
                                                             if sideQ == 'y':
                                                                         print (f"\nOK You Can Get Your Vaccination At {con2}/01/2024\n\n")
                                                                         USER_CHECK = open ("project/Users.csv", 'r')
                                                                         reader = csv.reader (USER_CHECK)
                                                                         next (reader)

                                                                         for Certain in reader:
                                                                                 if Email_USER == Certain [2] or Phone_Number_USER == Certain [4] or NationaL_ID_USER == Certain [5]:
                                                                                         print ("You Already Have An Appointment.")
                                                                                         sys.exit()
                                                                         USER_CHECK.close()
                                                                                        
                                                                         print (f"\nYour ID is '{USER_ID}'")
                                                                         writer = csv.writer(USER)
                                                                         writer.writerow([USER_ID,Name_USER,Email_USER,Password_USER,Phone_Number_USER,NationaL_ID_USER,f'{con2}/01/2024'])
                                                                         USER.close()

                                                                         sys.exit()
                                                             elif sideQ == 'n':
                                                                            continue
                                                             else:
                                                                 print ("\nINVALID VALUE\n")

                    elif Acc == 'y':                     
                            while True:
                                ID_CHECK = input("Do you Remember Your ID? (y , n)? ").lower()
                                if ID_CHECK == 'y':

                                    while True:
                                        USER = open ("project/Users.csv",'r')
                                        reader = csv.reader(USER)
                                        next (reader)
                                        print ("\n\nFILL THESE FIELD TO LOGIN: \n\n")
                                        USER_ID = input ("Enter Your USER ID: ")
                                        Name_USER = input ("Enter Your Name: ")
                                        Email_USER = input ("Enter Your Email: ")
                                        Password_USER = input ("Enter Your Password: ")
                                        Phone_Number_USER = input ("Enter Your Phone Number: ")
                                        NationaL_ID_USER = input ("Enter Your National ID: ")
                                        for row in reader:
                                            
                                            if USER_ID == row [0] and Name_USER == row[1] and Email_USER == row [2] and Password_USER == row[3] and Phone_Number_USER == row [4] and NationaL_ID_USER == row [5]:
                                                                 
                                                    Vaccine_Center_FILE = open ("project/Vaccination_Centers.csv",'r')
                                                    reader = csv.reader(Vaccine_Center_FILE)
                                            
                                            
                                                    for last in reader:
                                                            print (f"\n\n{last}")
                                                    Vaccine_Center_FILE.close()
                                                    
                                                    while True:
                                                        Vaccine_Center_END = open ("project/Vaccination_Centers.csv",'r')
                                                        reader = csv.reader(Vaccine_Center_END)

                                                        region = input ("\n\nEnter Your Region: ")
                                                        for end in reader:                                                      
                                                                if region == end[2]:
                                                                        con = random.choice(date)
                                                                                            
                                                                        print (
                                                                        f"""\n\nHello {Name_USER}!\n\nYOUR RESERVATION HAS BEEN ACCEPTED YOU CAN GET YOUR '{end[3]}' VACCINE AT '{end[0]} Center AT {row [6]}'"""
                                                                                )
                                                                        sys.exit()

                                                        Vaccine_Center_END.close()
                                                        Vaccine_Center_FILE.close()
                                                        USER.close()
                                                
                                            
                                        else:
                                            print ("\n\nTRY AGAIN..")
                                            
                                elif ID_CHECK == 'n':
                                    NAME_CHECK = input ("Enter Your Name: ")
                                    PASS_CHECK =input ("Enter Your Password: ")
                                    USER = open ("project/Users.csv",'r')
                                    reader = csv.reader(USER)
                                    next (reader)
                                    for check in reader:
                                            if NAME_CHECK == check [1] and PASS_CHECK == check [3]:
                                                print (f"Your ID is: {check[0]}")
                                                sys.exit()
                                            
                                    print ("TRY AGAIN..")

                                else:
                                    print ("\nPLEASE CHOOSE BETWEEN 'y' AND 'n' \n")       

                    else:
                            print ("\nPLEASE CHOOSE BETWEEN 'y' AND 'n' \n")
                            pass
                                
            USERS()
    else:
            print ("Choose Correctly Please..\n")
            check =input ("Are You 'Admin' or 'User'?\n").lower()