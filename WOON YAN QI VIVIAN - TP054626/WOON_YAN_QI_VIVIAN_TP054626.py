def user_login(plogallrec):
    username = input ("Enter username:")
    password = input ("Enter password:")
    flg = 0
    for i in range(len(plogallrec)):
        if username in plogallrec[i][0] and password in plogallrec[i][1]:
            flg = 1
            break
    return flg

def add_user():
    with open("patientlogin.txt","a") as fhplog:
        newrec = []
        username = input("Please enter username:")
        password = input("Please enter password:")
        flag=0
        for i in range (len(plogallrec)):
            if username in plogallrec[i][0]:
                print("\nSIGN UP FAILD! Current username is used.\n")
                flag=1
                break       
        if flag==0:
            newrec.append(username)
            newrec.append(password)
            fhplog.write(":".join(newrec)+"\n")
    return newrec

def staff_login(slogallrec):
    username = input ("Enter username:")
    password = input ("Enter password:")
    flg = 0
    for i in range(len(slogallrec)):
        if username in slogallrec[i][0] and password in slogallrec[i][1]:
            flg = 1
            break
    return flg

def add_patient():
    pallrec = []
    vallrec=[]
    with open("patient.txt","r") as fhp:
        for prec in fhp:
            pinfo = prec.split(":")
            pallrec.append(pinfo)
    with open("vaccination.txt","r") as fhv:
        for vrec in fhv:
            vinfo = vrec.split(":")
            vallrec.append(vinfo)
    new_prec = []
    new_vrec=[] 
    while True:
        while True:
            name = input("Enter your name as per IC or passport:")
            name=name.upper()
            name = ''.join(i for i in name if not i.isdigit())
            print("Your name is:"+name)
            choice= input("Press 1 to continue:")
            if choice=="1":
                print()
                break
            else:
                print("Please reenter your name.")
                print()

        bigflag=0
        while bigflag==0:
            malaysian = input("Are you Malaysian? YES/NO:")
            if malaysian == "YES" or malaysian == "yes":
                icpp = input("Enter your IC number: (ex: 123456-78-9999)")
                try:
                    if icpp[6]=="-" and icpp[9]=="-" and len(icpp)==14 and type(int(icpp[:6]))==int and type(int(icpp[7:9]))==int and type(int(icpp[10:]))==int:
                        flag=0
                        for i in range (len(pallrec)):
                            if icpp in pallrec[i][5]:
                                print("This IC already registered!")
                                print()
                                flag=1
                                break
                        if flag==0:
                            print("Your IC is:"+icpp)
                            choice= input("Press 1 to continue:")
                            if choice=="1":
                                print()
                                bigflag=1
                            else:
                                print("Please reenter your IC.")
                                print()
                                flag=1
                    else:
                        print("INVALID INPUT!")
                        print()
                except:
                    print("INVALID INPUT!")
                    print()
                    
            elif malaysian == "NO" or malaysian == "no":
                icpp = input("Enter your passport number:")
                flag=0
                for i in range (len(pallrec)):
                    if icpp in pallrec[i][5]:
                        print("This passport already registered!")
                        print()
                        flag=1
                        break
                if flag==0:
                    print("Your passport is:"+icpp)
                    choice= input("Press 1 to continue:")
                    if choice=="1":
                        print()
                        bigflag=1
                    else:
                        print("Please reenter your passport.")
                        print()
                        flag=1
            else:
                print("INVALID INPUT!")
                print()
        #icpp done!

        #centre done！   
        while True:
            print("Vaccine centre:")
            print("1-VC1")
            print("2-VC2")
            vc_centre = input("Enter your choice:")
            if vc_centre == "1":
                vc_centre="VC1"
                print("Your vaccine centre is:"+vc_centre)
                choice= input("Press 1 to continue:")
                if choice=="1":
                    print()
                    break
                else:
                    print("Please reselect your name.")
                    print()
            elif vc_centre == "2":
                vc_centre="VC2"
                print("Your vaccine centre is:"+vc_centre)
                choice= input("Press 1 to continue:")
                if choice=="1":
                    print()
                    break
                else:
                    print("Please reselect your name.")
                    print()
            else:
                print("INVALID INPUT!")
                print()
        #centre done！

        #age,vccode done！
        bigflag=0
        while bigflag==0:
            flag=0
            while flag==0:
                try:
                    age = int(input("Enter your age:"))
                    if age>=12 and age<18:
                        while True:
                            print("Available vaccine code for your age:")
                            print("1-AF")
                            print("2-CZ")
                            print("3-DM")
                            vc_code = input("Enter your choice:")
                            if vc_code == "1":
                                vc_code="AF"
                                flag=1
                                break
                            elif vc_code == "2":
                                vc_code="CZ"
                                flag=1
                                break
                            elif vc_code == "3":
                                vc_code="DM"
                                flag=1
                                break
                            else:
                                print("INVALID INPUT!")
                                print()
                    elif age>=18 and age<=45:
                        while True:
                            print("Available vaccine code for your age:")
                            print("1-AF")
                            print("2-BV")
                            print("3-CZ")
                            print("4-DM")
                            print("5-EC")
                            vc_code = input("Enter your choice:")
                            if vc_code == "1":
                                vc_code="AF"
                                flag=1
                                break
                            elif vc_code == "2":
                                vc_code="BV"
                                flag=1
                                break
                            elif vc_code == "3":
                                vc_code="CZ"
                                flag=1
                                break
                            elif vc_code == "4":
                                vc_code="DM"
                                flag=1
                                break
                            elif vc_code == "5":
                                vc_code="EC"
                                flag=1
                                break
                            else:
                                print("INVALID INPUT!")
                                print()
                    elif age>=46 and age<=200:
                        while True:
                            print("Available vaccine code for your age:")
                            print("1-AF")
                            print("2-BV")
                            print("3-DM")
                            print("4-EC")
                            vc_code = input("Enter your choice:")
                            if vc_code == "1":
                                vc_code="AF"
                                flag=1
                                break
                            elif vc_code == "2":
                                vc_code="BV"
                                flag=1
                                break
                            elif vc_code == "3":
                                vc_code="DM"
                                flag=1
                                break
                            elif vc_code == "4":
                                vc_code="EC"
                                flag=1
                                break
                            else:
                                print("INVALID INPUT!")
                                print()
                    else:
                        print("Sorry, there's no vaccine available for you.")
                        print()
                except:
                    print("INVALID INPUT!!!")
                    print()
                    
            while flag==1:
                print("Your age is:"+str(age))
                print("Your vaccine code is:"+vc_code)
                choice= input("Press 1 to continue:")
                if choice=="1":
                    print()
                    bigflag=1
                    break
                else:
                    print("Please reselect your age and vaccine code.")
                    print()
                    flag=0
        #age,vccode done！

        #contact done!
        while True:
            contact = input("Enter your mobile number:(ex. 012-23456789)")
            try:
                if contact[:2]=="01" and contact[3]=="-" and type(int(contact[4:]))==int and len(contact)==11 or len(contact)==12:
                    print("Your contact is:"+contact)
                    choice= input("Press 1 to continue:")
                    if choice=="1":
                        print()
                        break
                    else:
                        print("Please reenter your mobile number.")
                        print()
                else:
                    print("INVALID INPUT!")
                    print()
            except:
                print("INVALID INPUT!")
                print()
        #contact done!
            
        #email done!
        while True:
            email = input("Enter your e-mail address:")
            flag=0
            cnt=0
            for i in email:
                if i=="@":
                    flag=1
                    break
                else:
                    cnt=cnt+1
            if cnt!=0 and flag==1:
                for i in email[cnt+2:-1]:
                    if i==".":
                        flag=2
                        break
            if flag==2:
                print("Your email is:"+email)
                choice= input("Press 1 to continue:")
                if choice=="1":
                    print()
                    break
                else:
                    print("Please reenter your email.")
                    print()
                    
            else:
                print("INVALID INPUT!")
                print()
        #email done!
        

        today = datetime.datetime.today()
        d1 = today + datetime.timedelta(days=3)
        d1date = d1.strftime("%d/%m/%Y")
        if vc_code == "AF":
            d2 = d1 + datetime.timedelta(days=14)
            d2date = d2.strftime("%d/%m/%Y")
        elif vc_code == "BV":
            d2 = d1 + datetime.timedelta(days=21)
            d2date = d2.strftime("%d/%m/%Y")
        elif vc_code == "CZ":
            d2 = d1 + datetime.timedelta(days=21)
            d2date = d2.strftime("%d/%m/%Y")
        elif vc_code == "DM":
            d2 = d1 + datetime.timedelta(days=28)
            d2date = d2.strftime("%d/%m/%Y")
        elif vc_code == "EC":
            d2date = "NONE"

        print("Name          :"+name)
        print("Age           :"+str(age))
        print("Vaccine Centre:"+vc_centre)
        print("Vaccine Code  :"+vc_code)
        print("Contact       :"+contact)
        print("Email         :"+email)
        print()
        print("Make sure your information are correct.")
        print("Once registration done, only contact and email can be changed.")
        choose=input("Press 1 to continue. Press 2 to exit registration. Otherwise, restart the registration:")
        if choose=="1":
            print()
            break
        elif choose=="2":
            print("exiting to menu...")
            break
        else:
            print("RESTART REGISTRATION:")
            print()
    
    if choose=="1":        
        print("REGISTRATION SUCCESSFUL!")
        print()
        pid_code = "P"+vc_code
        pid = get_new_id(pid_code)
        print("Patient ID:"+pid)
        print("Dose 1    :"+d1date)
        print("Dose 2    :"+d2date)
        print("REMINDER: Patient ID is important when having vaccination.")
        print()
        with open("vaccination.txt","a") as fh:
            #[0:pid,1:centre,2:code,3:D1,4:d1date,5:no,6:d1batch,7:D2,8:d2date,9:no,10:d2batch,11:status]
            new_vrec.append(pid)
            new_vrec.append(vc_centre)
            new_vrec.append(vc_code)
            new_vrec.append("D1")
            new_vrec.append(d1date)
            new_vrec.append("NO")
            new_vrec.append("N/A")
            new_vrec.append("D2")
            new_vrec.append(d2date)
            new_vrec.append("NO")
            new_vrec.append("N/A")
            new_vrec.append("NEW")
            new_vrec.append(icpp)
            fh.write(":".join(new_vrec)+"\n")
        with open("patient.txt","a") as fh:
            new_prec.append(name)
            new_prec.append(str(age))
            new_prec.append(pid)
            new_prec.append(vc_centre)
            new_prec.append(vc_code)
            new_prec.append(icpp)
            new_prec.append(contact)
            new_prec.append(email)
            fh.write(":".join(new_prec)+"\n")
    else:
        print("Registration Failed.")
        
    return new_prec, new_vrec
#ADD PATIENT DONE


def get_new_id(eid):
    with open("id.txt","r") as fh:
        idlist=fh.readline()
    if eid == "PAF":
        ind=0
    elif eid == "PBV":
        ind=1
    elif eid == "PCZ":
        ind=2
    elif eid == "PDM":
        ind=3
    elif eid == "PEC":
        ind=4
    else:
        ind=5
    sep_idlist = idlist.split(":")
    nextid = sep_idlist[ind]
    newid = str(int(nextid[3:])+1)
    if len(newid) == 1:
        nextid = nextid[:3]+"00000"+newid
    elif len(newid) == 2:
        nextid = nextid[:3]+"0000"+newid
    elif len(newid) == 3:
        nextid = nextid[:3]+"000"+newid
    elif len(newid) == 4:
        nextid = nextid[:3]+"00"+newid
    elif len(newid) == 5:
        nextid = nextid[:3]+"0"+newid
    elif len(newid) == 6:
        nextid = nextid[:3]+newid
    sep_idlist[ind]=nextid
    idlist=":".join(sep_idlist)
    with open("id.txt","w") as fh:
        fh.write(idlist)
    return nextid


def modify_patient(pallrec):
    searchname = input("Please enter name to search:")
    searchicpp = input("Please enter IC or PASSPORT NO to search:")
    cnt=0
    for i in range (len(pallrec)):
        if searchname in pallrec[i][0] and searchicpp in pallrec[i][5]:
            print("Please confirm this is you before make any changes:")
            print("Name      :",pallrec[i][0])
            print("Patient ID:",pallrec[i][2])
            print("1-Contact -",pallrec[i][6])
            print("2-Email   -",pallrec[i][7])
            while True:
                idx = input("Enter the no of field to modify:")
                if idx=="1":
                    while True:
                        contact = input("Enter your mobile number:(ex. 012-23456789)")
                        try:
                            if contact[:2]=="01" and contact[3]=="-" and type(int(contact[4:]))==int and len(contact)==11 or len(contact)==12:
                                print("Your contact is:"+contact)
                                choice= input("Press 1 to continue:")
                                if choice=="1":
                                    pallrec[i][6]=contact
                                    print()
                                    break
                                else:
                                    print("Please reenter your mobile number.")
                                    print()
                            else:
                                print("INVALID INPUT!")
                                print()
                        except:
                            print("INVALID INPUT!")
                            print()
                    break
                elif idx=="2":
                    while True:
                        email = input("Enter your e-mail address:")
                        flag=0
                        cnt=0
                        for j in email:
                            if j=="@":
                                flag=1
                                break
                            else:
                                cnt=cnt+1
                        if cnt!=0 and flag==1:
                            for j in email[cnt+2:-1]:
                                if j==".":
                                    flag=2
                                    break
                        if flag==2:
                            print("Your email is:"+email)
                            choice= input("Press 1 to continue:")
                            if choice=="1":
                                pallrec[i][7]=email
                                print()
                                break
                            else:
                                print("Please reenter your email.")
                                print()
                                
                        else:
                            print("INVALID INPUT!")
                            print()
                    break
                else:
                    print("INVALID INPUT!")
            break
        else:
            cnt=cnt+1
    if cnt==len(pallrec):
        print("Record not found!")
        
    with open("patient.txt","w") as fhp:
        for prec in pallrec:
            fhp.write(":".join(prec))
    return pallrec



def modify_login(plogallrec):
    searchname = input("Please enter current username:")
    cnt=0
    for i in range (len(plogallrec)):
        if searchname in plogallrec[i][0]:
            searchpw = input("Please enter current password:")
            if searchpw in plogallrec[i][1]:
                print("Modify field:")
                print("1-username")
                print("2-password")
                while True:
                    choice = input("Please enter your choice:")
                    if choice == "1":
                        while True:
                            newname = input("Please enter your new username:")
                            confirm = input("Please confirm your username:")
                            if newname == confirm:
                                flag=0
                                for i in range (len(plogallrec)):
                                    if newname in plogallrec[i][0]:
                                        print("\nSIGN UP FAILD! Current username is used.\n")
                                        flag=1
                                        break       
                                if flag==0:
                                    plogallrec[i][0]=newname
                                    break
                                else:
                                    print("Please reenter username.")
                            else:
                                print("\nINPUT WRONG!\n")
                        break
                    elif choice == "2":
                        while True:
                            newpw = input("Please enter your new password:")
                            confirm = input("Please confirm your password:")
                            if newpw == confirm:
                                plogallrec[i][1]=newpw
                                break
                            else:
                                print("\nINPUT WRONG!\n")
                        break
                    else:
                        print("\nINVALID INPUT!\n")
            break
        else:
            cnt=cnt+1
    if cnt==len(plogallrec):
        print("Record not found!")
    with open("patientlogin.txt","w") as fhplog:
        for plogrec in plogallrec:
            fhplog.write(":".join(plogrec))
    return plogallrec



def patient_check_status(vallrec):
    #[0:pid,1:centre,2:code,3:D1,4:d1date,5:no,6:d1batch,7:D2,8:d2date,9:no,10:d2batch,11:status]
    searchicpp = input("Registered IC/passport:")
    searchid = input("Patient ID:")
    for i in range (len(vallrec)):
        if searchid in vallrec[i][0] and searchicpp in vallrec[i][12]:
            print("PID      :"+vallrec[i][0])
            print("CENTRE   :"+vallrec[i][1])
            print("VACCINE  :"+vallrec[i][2])
            print("D1 DATE  :"+vallrec[i][4])
            print("D1 STATUS:"+vallrec[i][5])
            print("D2 DATE  :"+vallrec[i][8])
            print("D2 STATUS:"+vallrec[i][9])
            print("VACCINE STATUS:"+vallrec[i][11])
            break


def search_patient_id(pallrec):
    searchname = input("Please enter name to search:")
    searchicpp = input("Please enter IC or PASSPORT NO to search:")
    for i in range (len(pallrec)):
        #if not found?
        if searchname in pallrec[i][0] and searchicpp in pallrec[i][5]:
            print("Name:",pallrec[i][0])
            print("IC/passport:",pallrec[i][5])
            print("Patient ID:",pallrec[i][2])
            print()
            break

def display_patient_rec(pallrec):
    print("="*137)
    print("NO".center(10)+"|"+"NAME".center(30)+"|"+"AGE".center(4)+"|"+"PID".center(11)+"|"+"CENTRE".center(8)+"|"+"CODE".center(6)+"|"+"IC/PP".center(16)+"|"+"CONTACT".center(14)+"|"+"EMAIL".center(30))
    print("="*137)
    cnt=1
    for i in range (len(pallrec)):
        print(str(cnt).ljust(10)+"|"+pallrec[i][0].ljust(30)+"|"+pallrec[i][1].center(4)+"|"+pallrec[i][2].center(11)+"|"+pallrec[i][3].center(8)+"|"+pallrec[i][4].center(6)+"|"+pallrec[i][5].center(16)+"|"+pallrec[i][6].ljust(14)+"|"+pallrec[i][7].ljust(30))
        cnt=cnt+1
    print("="*137)


def display_vac_rec(vallrec):
    print("="*140)
    print("NO".center(10)+"|"+"PID".center(11)+"|"+"CENTRE".center(8)+"|"+"CODE".center(6)+"|"+"D1".center(20)+"|"+"D1_STA".center(8)+"|"+"D1_BATCH".center(12)+"|"+"D2".center(20)+"|"+"D2_STA".center(8)+"|"+"D2_BATCH".center(12)+"|"+"STATUS".center(16))
    print("="*140)
    cnt=1
    for i in range (len(vallrec)):
        print(str(cnt).ljust(10)+"|"+vallrec[i][0].center(11)+"|"+vallrec[i][1].center(8)+"|"+vallrec[i][2].center(6)+"|"+vallrec[i][4].ljust(20)+"|"+vallrec[i][5].ljust(8)+"|"+vallrec[i][6].ljust(12)+"|"+vallrec[i][8].ljust(20)+"|"+vallrec[i][9].ljust(8)+"|"+vallrec[i][10].ljust(12)+"|"+vallrec[i][11].ljust(16))
        cnt=cnt+1
    print("="*140)

#DONE S5
def vaccination_administration(vallrec):
    #[0:pid,1:centre,2:code,3:D1,4:d1date,5:no,6:d1batch,7:D2,8:d2date,9:no,10:d2batch,11:status]
    search = input("Patient ID:")
    for i in range (len(vallrec)):
        if search in vallrec[i][0]:
            print("PID      :"+vallrec[i][0])
            print("CENTRE   :"+vallrec[i][1])
            print("VACCINE  :"+vallrec[i][2])
            print("D1 DATE  :"+vallrec[i][4])
            print("D1 STATUS:"+vallrec[i][5])
            print("D2 DATE  :"+vallrec[i][8])
            print("D2 STATUS:"+vallrec[i][9])
            print("VACCINE STATUS:"+vallrec[i][11])
            if vallrec[i][5]=="NO":
                print("D1 vaccination.")
                done = input("Enter 1 when D1 is done:")
                if done == "1":
                    while True:
                        batch=input("Enter vaccine batch number:")
                        print("Vaccine batch number:"+batch)
                        choice=input("Press 1 to continue:")
                        if choice=="1":
                            vallrec[i][6]=batch
                            break
                        else:
                            print("Please reenter vaccine batch number.")
                    vallrec[i][5]="YES"
                    d1 = datetime.datetime.today()
                    d1date = d1.strftime("%d/%m/%Y,%H%M")
                    vallrec[i][4]=d1date
                    if vallrec[i][2] == "AF":
                        d2 = d1 + datetime.timedelta(days=14)
                        vallrec[i][8] = d2.strftime("%d/%m/%Y")
                        print("D2 DATE:"+ vallrec[i][8])
                        vallrec[i][11] = "COMPLETED-D1"
                        print("STATUS:"+vallrec[i][11])
                    elif vallrec[i][2] == "BV":
                        d2 = d1 + datetime.timedelta(days=21)
                        vallrec[i][8] = d2.strftime("%d/%m/%Y")
                        print("D2 DATE:"+ vallrec[i][8])
                        vallrec[i][11] = "COMPLETED-D1"
                        print("STATUS:"+vallrec[i][11])
                    elif vallrec[i][2] == "CZ":
                        d2 = d1 + datetime.timedelta(days=21)
                        vallrec[i][8] = d2.strftime("%d/%m/%Y")
                        print("D2 DATE:"+ vallrec[i][8])
                        vallrec[i][11] = "COMPLETED-D1"
                        print("STATUS:"+vallrec[i][11])
                    elif vallrec[i][2] == "DM":
                        d2 = d1 + datetime.timedelta(days=28)
                        vallrec[i][8] = d2.strftime("%d/%m/%Y")
                        print("D2 DATE:"+ vallrec[i][8])
                        vallrec[i][11] = "COMPLETED-D1"
                        print("STATUS:"+vallrec[i][11])
                    elif vallrec[i][2] == "EC":
                        vallrec[i][8] = "NONE"
                        vallrec[i][9] = "NONE"
                        vallrec[i][10] = "NONE"
                        vallrec[i][11] = "COMPLETED"
                        print("D2 DATE:"+vallrec[i][8])
                        print("STATUS:"+vallrec[i][11])
                    #break
                else:
                    print("D1 vaccination failed.Exiting to menu...")
                    #break
                #break
            #[0:pid,1:centre,2:code,3:D1,4:d1date,5:no,6:d1batch,7:D2,8:d2date,9:no,10:d2batch,11:status]
            elif vallrec[i][5]=="YES" and vallrec[i][9]=="NO":
                print("D2 vaccination.")
                done = input("Enter 1 when D2 is done:")
                if done == "1":
                    while True:
                        batch=input("Enter vaccine batch number:")
                        print("Vaccine batch number:"+batch)
                        choice=input("Press 1 to continue:")
                        if choice=="1":
                            vallrec[i][10]=batch
                            break
                        else:
                            print("Please reenter vaccine batch number.")
                    vallrec[i][9]="YES"
                    vallrec[i][11]="COMPLETED"
                    d2 = datetime.datetime.today()
                    d2date = d2.strftime("%d/%m/%Y,%H%M")
                    vallrec[i][8]=d2date
                    print("STATUS:"+vallrec[i][11])
                    #break
                else:
                    print("D2 vaccination failed.Exiting to menu...")
                    #break
                #break
            else:
                print("Vaccination Completed.")
                #break
            break
    with open("vaccination.txt","w") as fhv:
        for vrec in vallrec:
            fhv.write(":".join(vrec)+"\n")
    return vallrec
#DONE VACCINE ADMIN

#DONE S6
def check_patient_status(vallrec):
    #[0:pid,1:centre,2:code,3:D1,4:d1date,5:no,6:d1batch,7:D2,8:d2date,9:no,10:d2batch,11:status]
        search = input("Patient ID:")
        for i in range (len(vallrec)):
            if search in vallrec[i][0]:
                print("PID      :"+vallrec[i][0])
                print("CENTRE   :"+vallrec[i][1])
                print("VACCINE  :"+vallrec[i][2])
                print("D1 DATE  :"+vallrec[i][4])
                print("D1 STATUS:"+vallrec[i][5])
                print("D2 DATE  :"+vallrec[i][8])
                print("D2 STATUS:"+vallrec[i][9])
                print("VACCINE STATUS:"+vallrec[i][11])
                print()
                break

#DONE S7,P5
def check_overall_status(vallrec):
    #[0:pid,1:centre,2:code,3:D1,4:d1date,5:no,6:d1batch,7:D2,8:d2date,9:no,10:d2batch,11:status]
    af=0
    af1=0
    af2=0
    bv=0
    bv1=0
    bv2=0
    cz=0
    cz1=0
    cz2=0
    dm=0
    dm1=0
    dm2=0
    ec=0
    ec1=0
    ec2=0
    vc1=0
    vc2=0
    vc1d1=0
    vc1d2=0
    vc2d1=0
    vc2d2=0
    total=len(vallrec)
    for i in range(total):
        if vallrec[i][2]=="AF":
            af=af+1
            if vallrec[i][11]=="COMPLETED":
                af2=af2+1
            elif vallrec[i][5]=="YES" and vallrec[i][9]=="NO":
                af1=af1+1
        elif vallrec[i][2]=="BV":
            bv=bv+1
            if vallrec[i][11]=="COMPLETED":
                bv2=bv2+1
            elif vallrec[i][5]=="YES" and vallrec[i][9]=="NO":
                bv1=bv1+1
        elif vallrec[i][2]=="CZ":
            cz=cz+1
            if vallrec[i][11]=="COMPLETED":
                cz2=cz2+1
            elif vallrec[i][5]=="YES" and vallrec[i][9]=="NO":
                cz1=cz1+1
        elif vallrec[i][2]=="DM":
            dm=dm+1
            if vallrec[i][11]=="COMPLETED":
                dm2=dm2+1
            elif vallrec[i][5]=="YES" and vallrec[i][9]=="NO":
                dm1=dm1+1
        elif vallrec[i][2]=="EC":
            ec=ec+1
            if vallrec[i][11]=="COMPLETED":
                ec2=ec2+1
            elif vallrec[i][5]=="NO":
                ec1=ec1+1
    for i in range(total):
        if vallrec[i][1]=="VC1":
            vc1=vc1+1
            if vallrec[i][11]=="COMPLETED-D1":
                vc1d1=vc1d1+1
            elif vallrec[i][11]=="COMPLETED":
                vc1d2=vc1d2+1
        elif vallrec[i][1]=="VC2":
            vc2=vc2+1
            if vallrec[i][11]=="COMPLETED-D1":
                vc2d1=vc2d1+1
            elif vallrec[i][11]=="COMPLETED":
                vc2d2=vc2d2+1
    
##        print("Number of registration:",total)
##        print("AF:",af,"(",round(af/total,4)*100,"%)")
##        print("BV:",bv,"(",round(bv/total,4)*100,"%)")
##        print("CZ:",cz,"(",round(cz/total,4)*100,"%)")
##        print("DM:",dm,"(",round(dm/total,4)*100,"%)")
##        print("EC:",ec,"(",round(ec/total,4)*100,"%)")
##        print()
##        print("All dose completed:",af2+bv2+cz2+dm2+ec2,"(",round((af2+bv2+cz2+dm2+ec2)/total,4)*100,"%)")
##        print("AF:",af2,"(",round(af2/af,4)*100,"%)")
##        print("BV:",bv2,"(",round(bv2/bv,4)*100,"%)")
##        print("CZ:",cz2,"(",round(cz2/cz,4)*100,"%)")
##        print("DM:",dm2,"(",round(dm2/dm,4)*100,"%)")
##        print("EC:",ec2,"(",round(e2/ec,4)*100,"%)")
##        print()
##        print("One more dose left:",af1+bv1+cz1+dm1+ec1,"(",round((af1+bv1+cz1+dm1+ec1)/total,4)*100,"%)")
##        print("AF:",af1,"(",round(af1/af,4)*100,"%)")
##        print("BV:",bv1,"(",round(bv1/bv,4)*100,"%)")
##        print("CZ:",cz1,"(",round(cz1/cz,4)*100,"%)")
##        print("DM:",dm1,"(",round(dm1/dm,4)*100,"%)")
##        print("EC:",ec1,"(",round(ec1/ec,4)*100,"%)")

    print("Number of registration:",total)
    print("AF:",af)
    print("BV:",bv)
    print("CZ:",cz)
    print("DM:",dm)
    print("EC:",ec)
    print()
    print("All dose completed:",af2+bv2+cz2+dm2+ec2)
    print("AF:",af2)
    print("BV:",bv2)
    print("CZ:",cz2)
    print("DM:",dm2)
    print("EC:",ec2)
    print()
    print("One more dose left:",af1+bv1+cz1+dm1+ec1)
    print("AF:",af1)
    print("BV:",bv1)
    print("CZ:",cz1)
    print("DM:",dm1)
    print("EC:",ec1)
    print()
    print("Number of patients vaccinated in VC1:",vc1)
    print("Waiting for dose 2:",vc1d1)
    print("Completed vaccination:",vc1d2)
    print()
    print("Number of patients vaccinated in VC2:",vc2)
    print("Waiting for dose 2:",vc2d1)
    print("Completed vaccination:",vc2d2)
    print()
#done check overall status
        
def patient_main_menu():
    plogallrec=[]
    pallrec = []
    vallrec=[]
    with open("patientlogin.txt","r") as fhplog:
        for plogrec in fhplog:
            ploginfo = plogrec.split(":")
            plogallrec.append(ploginfo)
    with open("patient.txt","r") as fhp:
        for prec in fhp:
            pinfo = prec.split(":")
            pallrec.append(pinfo)
    with open("vaccination.txt","r") as fhv:
        for vrec in fhv:
            vinfo = vrec.split(":")
            vallrec.append(vinfo)
    while (True):
        print()
        print("1- Register:")
        print("2- Modify Registration:")
        print("3- Modify Login:")
        print("4- Check Personal Vaccination Status:")
        print("5- Check Overall Vaccination Statistics:")
        print("6- Check Patient ID:")
        print("7- Exit.")
        choice = input("Enter your choice to proceed to next step:")
        print()
        if choice == "1":
            returns=add_patient()
            if returns!=([],[]):
                pallrec.append(returns[0])
                vallrec.append(returns[1])
        elif choice == "2":
            pallrec = modify_patient(pallrec)
        elif choice == "3":
            plogallrec = modify_login(plogallrec)
        elif choice == "4":
            patient_check_status(vallrec)
        elif choice == "5":
            check_overall_status(vallrec)
        elif choice == "6":
            search_patient_id(pallrec)
        elif choice == "7":
            break
        else:
            print("\nINVALID OPTION!\n")

def staff_main_menu():
    pallrec = []
    vallrec=[]
    with open("patient.txt","r") as fhp:
        for prec in fhp:
            pinfo = prec.strip().split(":")
            pallrec.append(pinfo)
    with open("vaccination.txt","r") as fhv:
        for vrec in fhv:
            vinfo = vrec.strip().split(":")
            vallrec.append(vinfo)
    while (True):
        print()
        print("1- Register:")
        print("2- Modify Patient's Registration:")
        print("3- Display All Patients Personal Information:")
        print("4- Display All Patients Vaccination Status:")
        print("5- Vaccination Administration:")
        print("6- Check Patient Vaccination Status:")
        print("7- Check Overall Vaccination Statistics:")
        print("8- Check Patient ID:")
        print("9- Exit.")
        choice = input("Enter your choice to proceed to next step:")
        print()
        if choice == "1":
            returns=add_patient()
            if returns!=([],[]):
                pallrec.append(returns[0])
                vallrec.append(returns[1])
        elif choice == "2":
            pallrec = modify_patient(pallrec)
        elif choice == "3":
            display_patient_rec(pallrec)
        elif choice == "4":
            display_vac_rec(vallrec)
        elif choice == "5":
            vaccination_administration(vallrec)
        elif choice == "6":
            check_patient_status(vallrec)
        elif choice == "7":
            check_overall_status(vallrec)
        elif choice == "8":
            search_patient_id(pallrec)
        elif choice == "9":
            break
        else:
            print("\n\n INVALID OPTION!")



    
#MAIN LOGIC DONEDONE
import datetime

plogallrec=[]
slogallrec=[]
with open("patientlogin.txt","r") as fhplog:
    for plogrec in fhplog:
        ploginfo = plogrec.split(":")
        plogallrec.append(ploginfo)
with open("stafflogin.txt","r") as fhslog:
    for slogrec in fhslog:
        sloginfo = slogrec.strip().split(":")
        slogallrec.append(sloginfo)
##pallrec = []
##vallrec=[]
##with open("patient.txt","r") as fhp:
##    for prec in fhp:
##        pinfo = prec.strip().split(":")
##        pallrec.append(pinfo)
##with open("vaccination.txt","r") as fhv:
##    for vrec in fhv:
##        vinfo = vrec.strip().split(":")
##        vallrec.append(vinfo)

while True:
    print()
    #DONE
    print("1-Login as patient")
    #DONE
    print("2-Sign up as patient")
    #DONE
    print("3-Staff")
    print("4-Exit")
    choice = input("Please select your identity:")
    print()
    if choice == "1":
        valid_user = user_login(plogallrec)
        if valid_user == 1:
            patient_main_menu()
        else:
            print("\nLOGIN FAILED! Username or password wrong.\n")
    elif choice == "2":
        plogallrec.append(add_user())
    elif choice == "3":
        valid_user = staff_login(slogallrec)
        if valid_user == 1:
            staff_main_menu()
        else:
            print("\nLOGIN FAILED! Username or password wrong.\n")
    elif choice == "4":
        print("Exited Program")
        break
    else:
        print("\nINVALID INPUT!!!\n")
